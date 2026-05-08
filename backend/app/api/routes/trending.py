from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.repositories.news_repository import NewsRepository
from app.database.repositories.trending_repository import TrendingRepository
from app.database.session.deps import get_db_session

router = APIRouter(prefix="/api/trending", tags=["trending"])
topic_repository = TrendingRepository()
news_repository = NewsRepository()


@router.get("")
def list_trending(db: Session = Depends(get_db_session)):
    return {
        "topics": topic_repository.list_topics(db),
        "stories": news_repository.list_trending(db),
    }

