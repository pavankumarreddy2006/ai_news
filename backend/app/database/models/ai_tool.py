from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.session.base import Base


class AITool(Base):
    __tablename__ = "ai_tools"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(180), unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(220), unique=True, nullable=False, index=True)
    website_url: Mapped[str] = mapped_column(String(600), nullable=False)
    category: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    pricing: Mapped[str] = mapped_column(String(80), default="Free")
    features: Mapped[str] = mapped_column(Text, default="")
    simple_explanation: Mapped[str] = mapped_column(Text, default="")
    ai_ranking: Mapped[float] = mapped_column(Float, default=0.0, index=True)
    popularity_score: Mapped[float] = mapped_column(Float, default=0.0)
    official: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

