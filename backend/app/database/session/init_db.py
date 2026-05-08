from app.database.models import ai_tool, article, category, notification, saved_article, telegram_user, trending_topic, user_preference  # noqa: F401
from app.database.session.base import Base
from app.database.session.engine import engine


def initialize_database() -> None:
    Base.metadata.create_all(bind=engine)

