from pathlib import Path

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from app.core.config.settings import get_settings

settings = get_settings()
configured_database_url = settings.database_url
database_url = configured_database_url

if configured_database_url.startswith("sqlite:///"):
    sqlite_path = Path(configured_database_url.replace("sqlite:///", "", 1))
    if not sqlite_path.is_absolute():
        sqlite_path = (Path(__file__).resolve().parents[4] / sqlite_path).resolve()
    sqlite_path.parent.mkdir(parents=True, exist_ok=True)
    database_url = f"sqlite:///{sqlite_path.as_posix()}"
else:
    sqlite_path = DEFAULT_SQLITE_PATH = (Path(__file__).resolve().parents[4] / "backend" / "data" / "ai_news.db")
    sqlite_path.parent.mkdir(parents=True, exist_ok=True)


def _build_engine(target_url: str):
    connect_args = {"check_same_thread": False} if target_url.startswith("sqlite") else {}
    engine_kwargs = {
        "future": True,
        "pool_pre_ping": True,
        "connect_args": connect_args,
    }
    if not target_url.startswith("sqlite"):
        engine_kwargs.update({"pool_recycle": 300, "pool_size": 5, "max_overflow": 10})
    return create_engine(target_url, **engine_kwargs)


engine = _build_engine(database_url)
if not database_url.startswith("sqlite"):
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except SQLAlchemyError:
        database_url = f"sqlite:///{sqlite_path.as_posix()}"
        engine = _build_engine(database_url)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
