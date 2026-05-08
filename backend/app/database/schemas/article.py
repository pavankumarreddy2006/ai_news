from datetime import datetime

from pydantic import BaseModel


class ArticleResponse(BaseModel):
    id: int
    title: str
    slug: str
    source: str
    source_url: str
    image_url: str
    category: str
    content_type: str
    summary: str
    easy_summary: str
    why_it_matters: str
    who_should_use_it: str
    beginner_explanation: str
    difficulty_level: str
    reading_time: str
    keywords: str
    ranking_score: float
    trending_score: float
    is_trending: bool
    published_at: datetime

    class Config:
        from_attributes = True

