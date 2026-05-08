from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies.services import recommendation_service
from app.database.repositories.news_repository import NewsRepository
from app.database.repositories.tool_repository import ToolRepository
from app.database.session.deps import get_db_session

router = APIRouter(prefix="/api/recommendations", tags=["recommendations"])
news_repository = NewsRepository()
tool_repository = ToolRepository()


@router.get("")
def recommendations(db: Session = Depends(get_db_session)):
    return recommendation_service.build_payload(
        news_repository.list_news(db, limit=8),
        tool_repository.list_tools(db, limit=12),
    )
