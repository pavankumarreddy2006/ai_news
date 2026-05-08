from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.database.models.ai_tool import AITool


class ToolRepository:
    def list_tools(self, db: Session, category: str | None = None, limit: int | None = None) -> list[AITool]:
        query = select(AITool).order_by(AITool.ai_ranking.desc(), AITool.popularity_score.desc())
        if category:
            query = query.where(AITool.category == category)
        if limit:
            query = query.limit(limit)
        return db.execute(query).scalars().all()

    def get_by_slug(self, db: Session, slug: str) -> AITool | None:
        return db.scalar(select(AITool).where(AITool.slug == slug))

    def create(self, db: Session, tool: AITool) -> AITool:
        db.add(tool)
        db.flush()
        return tool

    def count_tools(self, db: Session, category: str | None = None) -> int:
        query = select(func.count()).select_from(AITool)
        if category:
            query = query.where(AITool.category == category)
        return int(db.scalar(query) or 0)
