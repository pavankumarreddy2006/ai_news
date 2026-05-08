from datetime import datetime

from sqlalchemy import delete, func, select
from sqlalchemy.orm import Session

from app.database.models.article import Article


class NewsRepository:
    def list_news(self, db: Session, limit: int = 30, category: str | None = None) -> list[Article]:
        query = select(Article).order_by(Article.ranking_score.desc(), Article.published_at.desc()).limit(limit)
        if category:
            query = (
                select(Article)
                .where(Article.category == category)
                .order_by(Article.ranking_score.desc(), Article.published_at.desc())
                .limit(limit)
            )
        return db.execute(query).scalars().all()

    def get_by_source_url(self, db: Session, source_url: str) -> Article | None:
        return db.scalar(select(Article).where(Article.source_url == source_url))

    def create(self, db: Session, article: Article) -> Article:
        db.add(article)
        db.flush()
        return article

    def list_trending(self, db: Session, limit: int = 10) -> list[Article]:
        return db.execute(
            select(Article).where(Article.is_trending.is_(True)).order_by(Article.ranking_score.desc()).limit(limit)
        ).scalars().all()

    def get_categories(self, db: Session) -> list[str]:
        return db.execute(select(func.distinct(Article.category))).scalars().all()

    def cleanup_before(self, db: Session, cutoff: datetime) -> int:
        result = db.execute(delete(Article).where(Article.created_at < cutoff))
        return result.rowcount or 0

