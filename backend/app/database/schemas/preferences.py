from pydantic import BaseModel


class PreferenceRequest(BaseModel):
    session_id: str
    favorite_categories: list[str]
    difficulty_level: str = "Beginner"
    telegram_opt_in: bool = False


class SavedArticleRequest(BaseModel):
    session_id: str
    article_id: int

