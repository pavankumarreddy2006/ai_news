from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.notification import Notification
from app.database.models.saved_article import SavedArticle
from app.database.models.telegram_user import TelegramUser
from app.database.models.user_preference import UserPreference


class UserRepository:
    def upsert_preferences(
        self,
        db: Session,
        session_id: str,
        favorite_categories: list[str],
        difficulty_level: str,
        telegram_opt_in: bool,
    ) -> UserPreference:
        preference = db.scalar(select(UserPreference).where(UserPreference.session_id == session_id))
        categories = ",".join(favorite_categories)
        if preference:
            preference.favorite_categories = categories
            preference.difficulty_level = difficulty_level
            preference.telegram_opt_in = telegram_opt_in
        else:
            preference = UserPreference(
                session_id=session_id,
                favorite_categories=categories,
                difficulty_level=difficulty_level,
                telegram_opt_in=telegram_opt_in,
            )
            db.add(preference)
        db.flush()
        return preference

    def save_article(self, db: Session, session_id: str, article_id: int) -> SavedArticle:
        saved = SavedArticle(session_id=session_id, article_id=article_id)
        db.add(saved)
        db.flush()
        return saved

    def list_saved_articles(self, db: Session, session_id: str) -> list[SavedArticle]:
        return db.execute(select(SavedArticle).where(SavedArticle.session_id == session_id)).scalars().all()

    def register_telegram_user(self, db: Session, chat_id: str, username: str, first_name: str) -> TelegramUser:
        existing = db.scalar(select(TelegramUser).where(TelegramUser.chat_id == chat_id))
        if existing:
            return existing
        user = TelegramUser(chat_id=chat_id, username=username, first_name=first_name)
        db.add(user)
        db.flush()
        return user

    def list_active_telegram_chat_ids(self, db: Session) -> list[str]:
        return db.execute(select(TelegramUser.chat_id).where(TelegramUser.is_active.is_(True))).scalars().all()

    def create_notification(self, db: Session, channel: str, title: str, message: str, status: str) -> Notification:
        notification = Notification(channel=channel, title=title, message=message, status=status)
        db.add(notification)
        db.flush()
        return notification

