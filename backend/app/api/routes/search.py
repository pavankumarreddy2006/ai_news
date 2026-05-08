from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api.dependencies.services import search_service
from app.database.session.deps import get_db_session

router = APIRouter(prefix="/api/search", tags=["search"])


@router.get("")
def search(query: str = Query(..., min_length=2), db: Session = Depends(get_db_session)):
    return search_service.search(db, query)

