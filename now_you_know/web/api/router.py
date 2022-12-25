from fastapi.routing import APIRouter

from now_you_know.web.api import dummy, echo, monitoring, movie, redis

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
api_router.include_router(redis.router, prefix="/redis", tags=["redis"])
api_router.include_router(movie.router, prefix="/movie", tags=["movie"])
