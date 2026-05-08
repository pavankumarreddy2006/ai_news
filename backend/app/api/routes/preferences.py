from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.repositories.user_repository import UserRepository
from app.database.schemas.preferences import PreferenceRequest, SavedArticleRequest
from app.database.session.deps import get_db_session

router = APIRouter(prefix="/api/preferences", tags=["preferences"])
repository = UserRepository()


@router.post("")
def save_preferences(payload: PreferenceRequest, db: Session = Depends(get_db_session)):
    repository.upsert_preferences(
        db,
        session_id=payload.session_id,
        favorite_categories=payload.favorite_categories,
        difficulty_level=payload.difficulty_level,
        telegram_opt_in=payload.telegram_opt_in,
    )
    db.commit()
    return {"message": "Preferences updated."}


@router.post("/save-article")
def save_article(payload: SavedArticleRequest, db: Session = Depends(get_db_session)):
    repository.save_article(db, payload.session_id, payload.article_id)
    db.commit()
    return {"message": "Article saved."}


@router.get("/saved/{session_id}")
def get_saved_articles(session_id: str, db: Session = Depends(get_db_session)):
    return [item.article for item in repository.list_saved_articles(db, session_id)]

