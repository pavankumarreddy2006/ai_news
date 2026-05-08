from datetime import datetime

from pydantic import BaseModel


class TrendingTopicResponse(BaseModel):
    id: int
    topic: str
    context: str
    score: float
    velocity: float
    created_at: datetime

    class Config:
        from_attributes = True

