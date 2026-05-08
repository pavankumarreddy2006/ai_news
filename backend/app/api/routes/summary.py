from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.article import Article
from app.database.session.deps import get_db_session

router = APIRouter(prefix="/api/summary", tags=["summary"])


@router.get("/{article_id}")
def article_summary(article_id: int, db: Session = Depends(get_db_session)):
    article = db.scalar(select(Article).where(Article.id == article_id))
    if not article:
        raise HTTPException(status_code=404, detail="Article not found.")
    return {
        "title": article.title,
        "summary": article.summary,
        "easy_summary": article.easy_summary,
        "why_it_matters": article.why_it_matters,
        "who_should_use_it": article.who_should_use_it,
        "beginner_explanation": article.beginner_explanation,
        "difficulty_level": article.difficulty_level,
    }

