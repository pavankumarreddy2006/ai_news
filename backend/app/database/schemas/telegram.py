from pydantic import BaseModel


class TelegramSubscriptionRequest(BaseModel):
    chat_id: str
    username: str = ""
    first_name: str = ""

