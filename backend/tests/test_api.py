from fastapi.testclient import TestClient

from app.api.dependencies.services import content_orchestrator
from app.database.session.engine import SessionLocal
from app.database.session.init_db import initialize_database
from app.main import app

client = TestClient(app)

initialize_database()
db = SessionLocal()
try:
    content_orchestrator.run_refresh(db)
finally:
    db.close()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_news_route():
    response = client.get("/api/news")
    assert response.status_code == 200


def test_live_route():
    response = client.get("/api/live")
    assert response.status_code == 200
