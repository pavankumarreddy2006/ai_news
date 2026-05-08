from datetime import datetime, timedelta, timezone

from slugify import slugify
from sqlalchemy.orm import Session

from app.core.constants.categories import DEFAULT_CATEGORIES, TOOL_CATEGORIES
from app.database.models.ai_tool import AITool
from app.database.models.article import Article
from app.database.repositories.news_repository import NewsRepository
from app.database.repositories.tool_repository import ToolRepository
from app.database.repositories.trending_repository import TrendingRepository
from app.services.ai_processing.cleaning_service import CleaningService
from app.services.analytics.trend_service import TrendService
from app.services.aggregators.feed_collector import FeedCollector
from app.services.ranking.ranking_service import RankingService
from app.services.summarization.simple_english_service import SimpleEnglishService


FALLBACK_TOOLS = [
    {
        "name": "ChatGPT",
        "website_url": "https://chatgpt.com",
        "category": "chatbot AI",
        "pricing": "Free + Paid",
        "features": "Writing, coding, research, ideation",
        "simple_explanation": "A general AI assistant for learning, writing, and productivity.",
        "popularity_score": 98,
        "ai_ranking": 98,
    },
    {
        "name": "Cursor",
        "website_url": "https://cursor.com",
        "category": "coding AI",
        "pricing": "Free + Paid",
        "features": "AI coding, chat, editing, refactoring",
        "simple_explanation": "An AI-first code editor that helps developers build faster.",
        "popularity_score": 95,
        "ai_ranking": 96,
    },
    {
        "name": "Runway",
        "website_url": "https://runwayml.com",
        "category": "video AI",
        "pricing": "Paid",
        "features": "Generation, editing, motion tools",
        "simple_explanation": "An AI video platform for creators and production teams.",
        "popularity_score": 92,
        "ai_ranking": 93,
    },
    {
        "name": "Zapier",
        "website_url": "https://zapier.com",
        "category": "automation AI",
        "pricing": "Free + Paid",
        "features": "Automation, AI actions, agents",
        "simple_explanation": "An automation platform that connects apps and AI workflows.",
        "popularity_score": 89,
        "ai_ranking": 90,
    },
]


class ContentOrchestrator:
    def __init__(self) -> None:
        self.collector = FeedCollector()
        self.cleaner = CleaningService()
        self.simplifier = SimpleEnglishService()
        self.ranker = RankingService()
        self.news_repository = NewsRepository()
        self.tool_repository = ToolRepository()
        self.trending_repository = TrendingRepository()
        self.trend_service = TrendService()

    def run_refresh(self, db: Session) -> dict:
        raw = self.collector.fetch_all()
        cleaned = self.cleaner.clean_records(raw)
        stored = 0
        for record in cleaned:
            if self.news_repository.get_by_source_url(db, record["source_url"]):
                continue
            enriched = self.simplifier.enrich(record["title"], record["source"], record["category"])
            scored = self.ranker.score({**record, **enriched})
            self.news_repository.create(
                db,
                Article(
                    title=scored["title"],
                    slug=slugify(scored["title"])[:300],
                    source=scored["source"],
                    source_url=scored["source_url"],
                    image_url=scored["image_url"],
                    category=scored["category"],
                    content_type=scored["content_type"],
                    summary=scored["summary"],
                    easy_summary=scored["easy_summary"],
                    why_it_matters=scored["why_it_matters"],
                    who_should_use_it=scored["who_should_use_it"],
                    beginner_explanation=scored["beginner_explanation"],
                    difficulty_level=scored["difficulty_level"],
                    reading_time=scored["reading_time"],
                    keywords=scored["keywords"],
                    virality_score=scored["virality_score"],
                    engagement_score=scored["engagement_score"],
                    freshness_score=scored["freshness_score"],
                    beginner_score=scored["beginner_score"],
                    ranking_score=scored["ranking_score"],
                    trending_score=scored["trending_score"],
                    is_trending=scored["is_trending"],
                    published_at=scored["published_at"],
                ),
            )
            stored += 1
        self._seed_tools(db)
        articles = self.news_repository.list_news(db, limit=30)
        self.trending_repository.replace_all(db, self.trend_service.build_topics(articles))
        db.commit()
        return {"fetched": len(raw), "stored": stored, "categories": DEFAULT_CATEGORIES, "tool_categories": TOOL_CATEGORIES}

    def cleanup(self, db: Session, hours: int) -> int:
        cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
        removed = self.news_repository.cleanup_before(db, cutoff)
        db.commit()
        return removed

    def _seed_tools(self, db: Session) -> None:
        for tool in FALLBACK_TOOLS:
            slug = slugify(tool["name"])
            if self.tool_repository.get_by_slug(db, slug):
                continue
            self.tool_repository.create(
                db,
                AITool(
                    name=tool["name"],
                    slug=slug,
                    website_url=tool["website_url"],
                    category=tool["category"],
                    pricing=tool["pricing"],
                    features=tool["features"],
                    simple_explanation=tool["simple_explanation"],
                    popularity_score=tool["popularity_score"],
                    ai_ranking=tool["ai_ranking"],
                ),
            )

