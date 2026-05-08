from sqlalchemy.orm import Session

from app.api.dependencies.services import content_orchestrator
from app.services.websocket.connection_manager import live_connection_manager


async def run_refresh_job(db: Session) -> dict:
    result = content_orchestrator.run_refresh(db)
    await live_connection_manager.broadcast({"type": "refresh", "payload": result})
    return result

