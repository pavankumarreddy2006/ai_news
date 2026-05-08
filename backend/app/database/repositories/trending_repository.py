from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.trending_topic import TrendingTopic


class TrendingRepository:
    def list_topics(self, db: Session, limit: int = 10) -> list[TrendingTopic]:
        return db.execute(select(TrendingTopic).order_by(TrendingTopic.score.desc()).limit(limit)).scalars().all()

    def replace_all(self, db: Session, topics: list[TrendingTopic]) -> None:
        db.query(TrendingTopic).delete()
        for topic in topics:
            db.add(topic)

