from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies.services import telegram_service
from app.database.repositories.news_repository import NewsRepository
from app.database.schemas.telegram import TelegramSubscriptionRequest
from app.database.session.deps import get_db_session

router = APIRouter(prefix="/api/telegram", tags=["telegram"])
news_repository = NewsRepository()


@router.post("/subscribe")
def subscribe(payload: TelegramSubscriptionRequest, db: Session = Depends(get_db_session)):
    user = telegram_service.subscribe(db, payload.chat_id, payload.username, payload.first_name)
    return {"message": "Telegram subscription saved.", "user": user}


@router.post("/send-digest")
async def send_digest(db: Session = Depends(get_db_session)):
    top_articles = news_repository.list_news(db, limit=5)
    return await telegram_service.send_digest(db, top_articles)

