from datetime import datetime

from fastapi import APIRouter
from sqlalchemy import text

from app.core.config.settings import get_settings
from app.database.session.engine import SessionLocal, active_database_backend

router = APIRouter(tags=["health"])
settings = get_settings()


@router.get("/health")
def health():
    database_status = "ok"
    try:
        db = SessionLocal()
        try:
            db.execute(text("SELECT 1"))
        finally:
            db.close()
    except Exception:
        database_status = "degraded"
    return {
        "status": "ok" if database_status == "ok" else "degraded",
        "environment": settings.app_env,
        "database": database_status,
        "database_backend": active_database_backend,
        "live_updates_enabled": settings.enable_live_updates,
        "background_jobs_enabled": settings.enable_background_jobs,
        "timestamp": datetime.utcnow(),
    }
