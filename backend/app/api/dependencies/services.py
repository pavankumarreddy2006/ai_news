from app.services.aggregators.content_orchestrator import ContentOrchestrator
from app.services.ai_processing.learn_service import LearnService
from app.services.analytics.search_service import SearchService
from app.services.recommendation.recommendation_service import RecommendationService
from app.services.telegram.telegram_service import TelegramService

content_orchestrator = ContentOrchestrator()
learn_service = LearnService()
search_service = SearchService()
recommendation_service = RecommendationService()
telegram_service = TelegramService()

