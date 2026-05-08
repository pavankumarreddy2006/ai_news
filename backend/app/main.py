from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from app.api.middleware.error_handler import unhandled_exception_handler
from app.api.routes import categories, health, learn, live, news, preferences, recommendations, search, summary, telegram, tools, trending
from app.api.dependencies.services import content_orchestrator
from app.core.config.settings import get_settings
from app.core.logging.logger import configure_logging
from app.database.session.engine import SessionLocal
from app.database.session.init_db import initialize_database
from app.workers.scheduler import start_scheduler, stop_scheduler

settings = get_settings()
configure_logging()


@asynccontextmanager
async def lifespan(_: FastAPI):
    initialize_database()
    db = SessionLocal()
    try:
        content_orchestrator.run_refresh(db)
    finally:
        db.close()
    start_scheduler()
    yield
    stop_scheduler()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Production-grade AI news, tools, learning, and realtime intelligence platform.",
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url, "http://localhost:5173", "http://127.0.0.1:5173"],
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


@app.websocket("/ws/live-updates")
async def live_updates(websocket: WebSocket):
    await live.live_socket(websocket)

