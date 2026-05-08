from app.database.repositories.news_repository import NewsRepository
from app.database.session.engine import SessionLocal
from app.database.session.init_db import initialize_database
from app.services.aggregators.content_orchestrator import ContentOrchestrator


initialize_database()


def test_refresh_seeds_fallback_articles_when_sources_are_empty(monkeypatch):
    orchestrator = ContentOrchestrator()
    monkeypatch.setattr(orchestrator.collector, "fetch_all", lambda: [])

    db = SessionLocal()
    try:
        result = orchestrator.run_refresh(db)
        news = NewsRepository().list_news(db, limit=10)
    finally:
        db.close()

    assert result["fetched"] == 0
    assert news
    assert any(item.source == "AI News Platform" for item in news)
