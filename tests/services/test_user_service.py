import aiohttp
import pytest
from aioresponses import aioresponses

from src.core.config import settings
from src.services.user_service import fetch_users


class TestFetchUsers:
    @pytest.mark.asyncio
    async def test_should_return_users(
        self, mock_aiohttp: aioresponses, aiohttp_session: aiohttp.ClientSession
    ) -> None:
        user = {"name": "John", "id": 1, "username": "Doe", "email": "john@doe.com"}
        mock_aiohttp.get(
            f"{settings.REMOTE_USERS_API}?_page=1&_limit=5",
            status=200,
            payload=[user],
        )

        response = await fetch_users()
        assert response == [user]
