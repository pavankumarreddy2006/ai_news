from functools import lru_cache
from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[3]
BACKEND_DIR = BASE_DIR / "backend"
DEFAULT_SQLITE_PATH = BACKEND_DIR / "data" / "ai_news.db"


class Settings(BaseSettings):
    app_name: str = "AI News Platform"
    app_env: str = "development"
    app_version: str = "2.0.0"
    api_prefix: str = "/api"
    database_url: str = f"sqlite:///{DEFAULT_SQLITE_PATH.as_posix()}"
    frontend_url: str = "http://localhost:5173"
    openai_api_key: str = ""
    telegram_bot_token: str = ""
    telegram_default_chat_id: str = ""
    news_refresh_minutes: int = 20
    cleanup_hours: int = 48
    max_news_items_per_source: int = 12
    enable_background_jobs: bool = True
    enable_live_updates: bool = True
    request_timeout_seconds: float = 12.0

    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @computed_field
    @property
    def is_production(self) -> bool:
        return self.app_env.lower() == "production"


@lru_cache
def get_settings() -> Settings:
    return Settings()

