from fastapi import APIRouter

from app.api.v1.endpoints.main import router as main_router

api_router = APIRouter()
api_router.include_router(main_router, tags=["health"])
