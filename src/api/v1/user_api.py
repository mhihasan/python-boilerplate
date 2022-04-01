from fastapi import APIRouter

from src.schemas import user_schema
from src.services import user_service

router = APIRouter()


@router.get("/users/", response_model=list[user_schema.User])
async def get_users(page: int = 1, limit: int = 5):
    return await user_service.fetch_users(page, limit)
