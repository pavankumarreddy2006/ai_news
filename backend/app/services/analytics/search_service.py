from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.database.models.ai_tool import AITool
from app.database.models.article import Article


class SearchService:
    def search(self, db: Session, query: str) -> dict:
        q = f"%{query}%"
        articles = db.execute(
            select(Article).where(
                or_(
                    Article.title.ilike(q),
                    Article.summary.ilike(q),
                    Article.keywords.ilike(q),
                    Article.category.ilike(q),
                )
            ).limit(20)
        ).scalars().all()
        tools = db.execute(
            select(AITool).where(
                or_(
                    AITool.name.ilike(q),
                    AITool.category.ilike(q),
                    AITool.features.ilike(q),
                )
            ).limit(20)
        ).scalars().all()
        return {"news": articles, "tools": tools}

