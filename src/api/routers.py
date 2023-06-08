from fastapi.routing import APIRouter

from src.api.questions import router

routers = APIRouter()

routers.include_router(router, tags=["questions"])
