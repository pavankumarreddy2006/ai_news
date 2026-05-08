from datetime import datetime

import httpx
from sqlalchemy.orm import Session

from app.core.config.settings import get_settings
from app.database.repositories.user_repository import UserRepository

settings = get_settings()


class TelegramService:
    def __init__(self) -> None:
        self.repository = UserRepository()
        self.base_url = f"https://api.telegram.org/bot{settings.telegram_bot_token}"

    def subscribe(self, db: Session, chat_id: str, username: str, first_name: str):
        user = self.repository.register_telegram_user(db, chat_id, username, first_name)
        db.commit()
        db.refresh(user)
        return user

    def build_digest(self, top_articles: list) -> str:
        lines = ["Good morning. Here is your beginner-friendly AI digest:"]
        for item in top_articles[:5]:
            lines.append(f"- {item.title}: {item.easy_summary}")
        return "\n".join(lines)

    async def send_digest(self, db: Session, top_articles: list) -> dict:
        message = self.build_digest(top_articles)
        chat_ids = self.repository.list_active_telegram_chat_ids(db)
        if settings.telegram_default_chat_id and settings.telegram_default_chat_id not in chat_ids:
            chat_ids.append(settings.telegram_default_chat_id)
        sent = 0
        if settings.telegram_bot_token and chat_ids:
            async with httpx.AsyncClient(timeout=10.0) as client:
                for chat_id in chat_ids:
                    response = await client.post(f"{self.base_url}/sendMessage", json={"chat_id": chat_id, "text": message})
                    if response.is_success:
                        sent += 1
        self.repository.create_notification(
            db,
            channel="telegram",
            title="Daily AI Digest",
            message=f"{datetime.utcnow().isoformat()} :: {message}",
            status="sent" if sent else "queued",
        )
        db.commit()
        return {"sent": sent, "message": message}

