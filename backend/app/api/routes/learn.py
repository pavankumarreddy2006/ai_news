from fastapi import APIRouter

from app.api.dependencies.services import learn_service
from app.database.schemas.learn import LearnRequest

router = APIRouter(prefix="/api/learn", tags=["learn"])


@router.post("")
def learn(payload: LearnRequest):
    return learn_service.explain(payload.topic)

