from functools import lru_cache
from pathlib import Path

from pydantic import AliasChoices, Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[4]
BACKEND_DIR = BASE_DIR / "backend"
ROOT_ENV_FILE = BASE_DIR / ".env"
BACKEND_ENV_FILE = BACKEND_DIR / ".env"
DEFAULT_SQLITE_PATH = BACKEND_DIR / "data" / "ai_news.db"


class Settings(BaseSettings):
    app_name: str = "AI News Platform"
    app_env: str = "development"
    app_version: str = "2.0.0"
    api_prefix: str = "/api"
    secret_key: str = Field(default="development-secret-key", validation_alias="SECRET_KEY")
    database_url: str = f"sqlite:///{DEFAULT_SQLITE_PATH.as_posix()}"
    frontend_url: str = "http://localhost:5173"
    frontend_preview_url: str = ""
    cors_allowed_origins: str = ""
    openai_api_key: str = ""
    telegram_bot_token: str = ""
    telegram_default_chat_id: str = Field(
        default="",
        validation_alias=AliasChoices("TELEGRAM_CHAT_ID", "TELEGRAM_DEFAULT_CHAT_ID"),
    )
    telegram_digest_hour: int = 8
    telegram_digest_minute: int = 0
    telegram_digest_timezone: str = "Asia/Calcutta"
    news_refresh_minutes: int = 20
    cleanup_hours: int = 48
    max_news_items_per_source: int = 12
    enable_background_jobs: bool = True
    enable_live_updates: bool = True
    request_timeout_seconds: float = 12.0

    model_config = SettingsConfigDict(
        env_file=(BACKEND_ENV_FILE, ROOT_ENV_FILE),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @computed_field
    @property
    def is_production(self) -> bool:
        return self.app_env.lower() == "production"

    @computed_field
    @property
    def allowed_cors_origins(self) -> list[str]:
        configured = [
            origin.strip().rstrip("/")
            for origin in self.cors_allowed_origins.split(",")
            if origin.strip()
        ]
        defaults = [
            self.frontend_url.rstrip("/"),
            self.frontend_preview_url.rstrip("/"),
            "http://localhost:5173",
            "http://127.0.0.1:5173",
        ]
        return list(dict.fromkeys([origin for origin in [*configured, *defaults] if origin]))


@lru_cache
def get_settings() -> Settings:
    return Settings()
