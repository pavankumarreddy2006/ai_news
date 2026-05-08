from app.database.models.ai_tool import AITool
from app.database.models.article import Article


class RecommendationService:
    def build_payload(self, news: list[Article], tools: list[AITool]) -> dict:
        return {
            "news": news[:5],
            "tools": tools[:5],
        }

