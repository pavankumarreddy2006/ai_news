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
    backend_url: str = "http://127.0.0.1:10000"
    cors_allowed_origins: str = ""
    openai_api_key: str = ""
    openrouter_api_key: str = ""
    reddit_client_id: str = ""
    reddit_client_secret: str = ""
    reddit_user_agent: str = "ai-news-platform"
    github_token: str = ""
    youtube_api_key: str = ""
    producthunt_token: str = ""
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
    fetch_interval_minutes: int = Field(default=20, validation_alias=AliasChoices("FETCH_INTERVAL_MINUTES", "NEWS_REFRESH_MINUTES"))
    delete_old_news_hours: int = Field(default=48, validation_alias=AliasChoices("DELETE_OLD_NEWS_HOURS", "CLEANUP_HOURS"))
    max_news_items_per_source: int = 12
    enable_background_jobs: bool = True
    enable_live_updates: bool = True
    request_timeout_seconds: float = 12.0
    openai_rss: str = "https://openai.com/news/rss.xml"
    techcrunch_ai_rss: str = "https://techcrunch.com/category/artificial-intelligence/feed/"
    verge_ai_rss: str = "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml"
    anthropic_rss: str = "https://www.anthropic.com/news/rss.xml"
    huggingface_rss: str = "https://huggingface.co/blog/feed.xml"
    google_ai_rss: str = "https://blog.google/technology/ai/rss/"
    deepmind_rss: str = "https://deepmind.google/discover/blog/rss.xml"
    nvidia_ai_rss: str = "https://blogs.nvidia.com/blog/category/ai/feed/"
    reddit_subreddits: str = "artificial,OpenAI,ChatGPT,MachineLearning,singularity,LocalLLaMA,StableDiffusion,ArtificialInteligence,ClaudeAI,AItools,Futurology,technology"
    github_topics: str = "ai,llm,agents,rag,automation,openai,langchain,generative-ai,machine-learning"
    google_searches: str = "latest AI news,trending AI tools,best free AI tools,AI coding tools,AI video tools,AI productivity tools,AI startups,viral AI tools,AI workflows"
    youtube_channels: str = "Two Minute Papers,Matt Wolfe,AI Explained,Fireship,NetworkChuck,Liam Ottley,Wes Roth,The AI Grid"
    ai_blogs: str = "OpenAI Blog,Anthropic Blog,Google AI Blog,DeepMind Blog,NVIDIA AI Blog,Hugging Face Blog,Stability AI Blog,Midjourney Updates,Perplexity Blog"
    tech_news: str = "TechCrunch AI,The Verge AI,VentureBeat AI,Ars Technica AI,Wired AI,Analytics India Magazine,Towards Data Science,AI News"
    ai_tool_sources: str = "Futurepedia,There's An AI For That,Product Hunt,GitHub,Reddit"
    ai_ranking_keywords: str = "GPT,OpenAI,Claude,Gemini,Llama,AI Agent,AI Automation,AI Workflow,AI Startup,AI Coding"

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

    @computed_field
    @property
    def refresh_interval_minutes(self) -> int:
        return self.fetch_interval_minutes

    @computed_field
    @property
    def retention_hours(self) -> int:
        return self.delete_old_news_hours


@lru_cache
def get_settings() -> Settings:
    return Settings()
