import aiohttp

from src.core.config import settings
from src.schemas import user_schema
from src.utils import http


async def fetch_users(page: int = 1, limit: int = 5) -> list[user_schema.User]:
    async with aiohttp.ClientSession() as session:
        users = await http.fetch(
            session, settings.REMOTE_USERS_API, params={"_page": page, "_limit": limit}
        )

    return [user_schema.User(**user) for user in users]
