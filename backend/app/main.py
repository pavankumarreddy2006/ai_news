import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.api.middleware.error_handler import unhandled_exception_handler
from app.api.routes import categories, health, learn, live, news, preferences, recommendations, search, summary, telegram, tools, trending, workflow
from app.api.dependencies.services import content_orchestrator
from app.core.config.settings import get_settings
from app.core.logging.logger import configure_logging, get_logger
from app.database.session.engine import SessionLocal
from app.database.session.init_db import initialize_database
from app.services.websocket.connection_manager import workflow_state
from app.workers.scheduler import start_scheduler, stop_scheduler

settings = get_settings()
configure_logging()
logger = get_logger(__name__)


async def _run_initial_refresh() -> None:
    db = SessionLocal()
    try:
        result = await asyncio.to_thread(content_orchestrator.run_refresh, db)
        workflow_state.update(last_refresh_result=result)
    except Exception as exc:
        logger.exception("Initial refresh failed: %s", exc)
    finally:
        db.close()


@asynccontextmanager
async def lifespan(_: FastAPI):
    workflow_state.update(app_started=True, live_updates_ready=settings.enable_live_updates)
    initialize_database()
    workflow_state.update(database_ready=True)
    db = SessionLocal()
    try:
        db.execute(text("SELECT 1"))
        workflow_state.update(
            keys_valid=bool(settings.openai_api_key or settings.openrouter_api_key or settings.github_token or settings.telegram_bot_token),
            telegram_ready=bool(settings.telegram_bot_token),
        )
    except Exception as exc:
        logger.exception("Startup initialization failed: %s", exc)
    finally:
        db.close()
    start_scheduler()
    initial_refresh_task = asyncio.create_task(_run_initial_refresh())
    yield
    initial_refresh_task.cancel()
    stop_scheduler()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Production-grade AI news, tools, learning, and realtime intelligence platform.",
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_cors_origins,
    allow_origin_regex=r"https://.*\.onrender\.com",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_exception_handler(Exception, unhandled_exception_handler)

app.include_router(health.router)
app.include_router(news.router)
app.include_router(trending.router)
app.include_router(tools.router)
app.include_router(search.router)
app.include_router(categories.router)
app.include_router(telegram.router)
app.include_router(summary.router)
app.include_router(learn.router)
app.include_router(recommendations.router)
app.include_router(preferences.router)
app.include_router(live.router)
app.include_router(workflow.router)


@app.websocket("/ws/live-updates")
async def live_updates(websocket: WebSocket):
    await live.live_socket(websocket)
