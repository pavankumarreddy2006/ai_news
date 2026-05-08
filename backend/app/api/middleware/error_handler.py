from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.logging.logger import get_logger

logger = get_logger(__name__)


async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.exception("Unhandled exception on %s: %s", request.url.path, exc)
    return JSONResponse(status_code=500, content={"message": "The platform hit an unexpected issue but stayed online."})

