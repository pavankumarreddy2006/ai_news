import asyncio
from types import SimpleNamespace

import pytest

from app.database.session.engine import SessionLocal
from app.database.session.init_db import initialize_database
from app.services.telegram.telegram_service import TelegramService


initialize_database()


@pytest.fixture
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_build_digest_limits_to_five_items():
    service = TelegramService()
    articles = [
        SimpleNamespace(title=f"Title {index}", easy_summary=f"Summary {index}")
        for index in range(1, 8)
    ]

    message = service.build_digest(articles)

    assert "Title 1" in message
    assert "Title 5" in message
    assert "Title 6" not in message


def test_send_digest_queues_when_bot_token_missing(monkeypatch, db_session):
    service = TelegramService()
    monkeypatch.setattr("app.services.telegram.telegram_service.settings.telegram_bot_token", "")
    monkeypatch.setattr("app.services.telegram.telegram_service.settings.telegram_default_chat_id", "")

    result = asyncio.run(
        service.send_digest(
            db_session,
            [SimpleNamespace(title="AI Update", easy_summary="Plain English summary")],
        )
    )

    assert result["sent"] == 0
    assert result["status"] == "queued"
    assert result["reason"] == "Missing TELEGRAM_BOT_TOKEN."
