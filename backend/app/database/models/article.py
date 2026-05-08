from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.session.base import Base


class Article(Base):
    __tablename__ = "news_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(320), nullable=False)
    slug: Mapped[str] = mapped_column(String(340), unique=True, nullable=False, index=True)
    source: Mapped[str] = mapped_column(String(140), nullable=False, index=True)
    source_url: Mapped[str] = mapped_column(String(600), nullable=False, unique=True)
    image_url: Mapped[str] = mapped_column(String(600), default="")
    category: Mapped[str] = mapped_column(String(120), default="AI News", index=True)
    content_type: Mapped[str] = mapped_column(String(80), default="news")
    summary: Mapped[str] = mapped_column(Text, default="")
    easy_summary: Mapped[str] = mapped_column(Text, default="")
    why_it_matters: Mapped[str] = mapped_column(Text, default="")
    who_should_use_it: Mapped[str] = mapped_column(String(180), default="Beginners")
    beginner_explanation: Mapped[str] = mapped_column(Text, default="")
    difficulty_level: Mapped[str] = mapped_column(String(40), default="Beginner")
    reading_time: Mapped[str] = mapped_column(String(40), default="3 min")
    keywords: Mapped[str] = mapped_column(Text, default="")
    virality_score: Mapped[float] = mapped_column(Float, default=0.0)
    engagement_score: Mapped[float] = mapped_column(Float, default=0.0)
    freshness_score: Mapped[float] = mapped_column(Float, default=0.0)
    beginner_score: Mapped[float] = mapped_column(Float, default=0.0)
    ranking_score: Mapped[float] = mapped_column(Float, default=0.0, index=True)
    trending_score: Mapped[float] = mapped_column(Float, default=0.0)
    is_trending: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    published_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)

