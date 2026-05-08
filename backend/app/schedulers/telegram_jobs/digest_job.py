from sqlalchemy.orm import Session

from app.api.dependencies.services import telegram_service
from app.database.repositories.news_repository import NewsRepository
from app.services.websocket.connection_manager import live_connection_manager

news_repository = NewsRepository()


async def run_telegram_job(db: Session) -> dict:
    result = await telegram_service.send_digest(db, news_repository.list_news(db, limit=5))
    await live_connection_manager.broadcast({"type": "telegram", "payload": result})
    return result

