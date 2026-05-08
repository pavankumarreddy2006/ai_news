from datetime import datetime

import httpx
from sqlalchemy.orm import Session

from app.core.config.settings import get_settings
from app.database.repositories.user_repository import UserRepository
from app.services.websocket.connection_manager import workflow_state

settings = get_settings()


class TelegramService:
    def __init__(self) -> None:
        self.repository = UserRepository()

    @property
    def base_url(self) -> str:
        return f"https://api.telegram.org/bot{settings.telegram_bot_token}"

    def subscribe(self, db: Session, chat_id: str, username: str, first_name: str):
        user = self.repository.register_telegram_user(db, chat_id, username, first_name)
        db.commit()
        db.refresh(user)
        return user

    def build_digest(self, top_articles: list) -> str:
        lines = ["Good morning. Here is your beginner-friendly AI digest:"]
        for item in top_articles[:5]:
            lines.append(f"- {item.title}: {getattr(item, 'easy_summary', '')}")
            why_it_matters = getattr(item, "why_it_matters", "")
            if why_it_matters:
                lines.append(f"  Why it matters: {why_it_matters}")
        return "\n".join(lines)

    async def send_digest(self, db: Session, top_articles: list) -> dict:
        message = self.build_digest(top_articles)
        chat_ids = self.repository.list_active_telegram_chat_ids(db)
        if settings.telegram_default_chat_id and settings.telegram_default_chat_id not in chat_ids:
            chat_ids.append(settings.telegram_default_chat_id)
        sent = 0
        status = "queued"
        reason = ""
        if not settings.telegram_bot_token:
            reason = "Missing TELEGRAM_BOT_TOKEN."
        elif not chat_ids:
            reason = "No active Telegram subscribers configured."
        else:
            async with httpx.AsyncClient(timeout=10.0) as client:
                for chat_id in chat_ids:
                    try:
                        response = await client.post(f"{self.base_url}/sendMessage", json={"chat_id": chat_id, "text": message})
                        if response.is_success:
                            sent += 1
                    except httpx.HTTPError as exc:
                        reason = f"Telegram request failed: {exc}"
            status = "sent" if sent else "failed"
            if sent:
                reason = ""
            elif not reason:
                reason = "Telegram API did not accept any messages."
        self.repository.create_notification(
            db,
            channel="telegram",
            title="Daily AI Digest",
            message=f"{datetime.utcnow().isoformat()} :: {message}",
            status=status,
        )
        db.commit()
        workflow_state.update(
            telegram_ready=bool(settings.telegram_bot_token),
            last_digest_at=datetime.utcnow().isoformat(),
            last_digest_result={"sent": sent, "status": status, "reason": reason},
        )
        return {"sent": sent, "message": message, "status": status, "reason": reason}
