from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.article import Article
from app.database.session.base import Base


class SavedArticle(Base):
    __tablename__ = "saved_articles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    article_id: Mapped[int] = mapped_column(ForeignKey("news_items.id"), nullable=False)
    session_id: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    article: Mapped[Article] = relationship("Article")

