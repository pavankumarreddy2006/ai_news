import os


# Keep backend tests self-contained instead of depending on a running local Postgres instance.
os.environ.setdefault("DATABASE_URL", "sqlite:///./backend/data/test_ai_news.db")
