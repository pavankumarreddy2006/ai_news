from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database.repositories.news_repository import NewsRepository
from app.database.session.deps import get_db_session

router = APIRouter(prefix="/api/news", tags=["news"])
repository = NewsRepository()


@router.get("")
def list_news(
    limit: int = Query(default=30, ge=1, le=100),
    category: str | None = None,
    db: Session = Depends(get_db_session),
):
    return repository.list_news(db, limit=limit, category=category)

