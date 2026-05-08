from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.repositories.tool_repository import ToolRepository
from app.database.session.deps import get_db_session

router = APIRouter(prefix="/api/tools", tags=["tools"])
repository = ToolRepository()


@router.get("")
def list_tools(category: str | None = None, db: Session = Depends(get_db_session)):
    return repository.list_tools(db, category=category)

