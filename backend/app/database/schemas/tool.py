from datetime import datetime

from pydantic import BaseModel


class ToolResponse(BaseModel):
    id: int
    name: str
    slug: str
    website_url: str
    category: str
    pricing: str
    features: str
    simple_explanation: str
    ai_ranking: float
    popularity_score: float
    official: bool
    created_at: datetime

    class Config:
        from_attributes = True

