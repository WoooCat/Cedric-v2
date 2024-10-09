from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse

import logging

from src.exceptions.exceptions import BaseAppException


logger = logging.getLogger(__name__)


class ExceptionHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        try:
            response = await call_next(request)
            return response
        except BaseAppException as exc:
            logger.error(f"Custom exception: {exc.message}")
            return JSONResponse(
                status_code=exc.status_code,
                content={"detail": exc.message},
            )
        except Exception as exc:
            logger.error(f"Unhandled exception: {str(exc)}")
            return JSONResponse(
                status_code=500,
                content={"detail": "An internal server error occurred."},
            )
