from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.repositories.news_repository import NewsRepository
from app.database.repositories.tool_repository import ToolRepository
from app.database.repositories.trending_repository import TrendingRepository
from app.database.session.deps import get_db_session
from app.services.websocket.connection_manager import workflow_state

router = APIRouter(prefix="/api/workflow", tags=["workflow"])
news_repository = NewsRepository()
tool_repository = ToolRepository()
trending_repository = TrendingRepository()


@router.get("")
def get_workflow_status(db: Session = Depends(get_db_session)):
    state = workflow_state.snapshot()
    trending = trending_repository.list_topics(db, limit=10)
    return {
        **state,
        "counts": {
            "articles": news_repository.count_news(db),
            "tools": tool_repository.count_tools(db),
            "trending_topics": len(trending),
        },
        "summary": {
            "coverage": "AI news, tools, launches, tutorials, and discussions.",
            "telegram_schedule": "Daily morning digest.",
            "cleanup_window_hours": state.get("last_cleanup_result", {}).get("retention_hours", 48),
        },
    }
