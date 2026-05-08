from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config.settings import get_settings

settings = get_settings()
database_url = settings.database_url

if database_url.startswith("sqlite:///"):
    sqlite_path = Path(database_url.replace("sqlite:///", "", 1))
    if not sqlite_path.is_absolute():
        sqlite_path = (Path(__file__).resolve().parents[4] / sqlite_path).resolve()
    sqlite_path.parent.mkdir(parents=True, exist_ok=True)
    database_url = f"sqlite:///{sqlite_path.as_posix()}"

connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}
engine_kwargs = {
    "future": True,
    "pool_pre_ping": True,
    "connect_args": connect_args,
}
if not database_url.startswith("sqlite"):
    engine_kwargs.update({"pool_recycle": 300, "pool_size": 5, "max_overflow": 10})

engine = create_engine(database_url, **engine_kwargs)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
