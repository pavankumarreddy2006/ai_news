from sqlalchemy.orm import Session

from app.api.dependencies.services import content_orchestrator
from app.core.config.settings import get_settings
from app.services.websocket.connection_manager import live_connection_manager

settings = get_settings()


async def run_cleanup_job(db: Session) -> int:
    removed = content_orchestrator.cleanup(db, settings.retention_hours)
    await live_connection_manager.broadcast({"type": "cleanup", "payload": {"removed": removed}})
    return removed
