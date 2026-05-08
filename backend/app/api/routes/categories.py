from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.constants.categories import DEFAULT_CATEGORIES
from app.database.repositories.news_repository import NewsRepository
from app.database.session.deps import get_db_session

router = APIRouter(prefix="/api/categories", tags=["categories"])
repository = NewsRepository()


@router.get("")
def list_categories(db: Session = Depends(get_db_session)):
    discovered = [item for item in repository.get_categories(db) if item]
    return {"categories": list(dict.fromkeys(DEFAULT_CATEGORIES + discovered))}

