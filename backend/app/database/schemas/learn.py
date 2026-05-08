from pydantic import BaseModel


class LearnRequest(BaseModel):
    topic: str


class LearnResponse(BaseModel):
    topic: str
    explanation: str
    why_it_matters: str
    steps: list[str]
    examples: list[str]
    difficulty: str

