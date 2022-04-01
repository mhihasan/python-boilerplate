import httpx
import pytest
from aioresponses import aioresponses
from src.core.config import settings


@pytest.mark.asyncio
async def test_returns_users(client: httpx.AsyncClient, mock_aiohttp: aioresponses):
    users = [{"name": "John", "id": 1, "username": "Doe", "email": "john@doe.com"}]
    mock_aiohttp.get(
        f"{settings.REMOTE_USERS_API}?_page=1&_limit=5", status=200, payload=users
    )

    response = await client.get("/users/")

    assert response.status_code == 200
    assert response.json() == users
