from collections.abc import Generator, AsyncGenerator

import aiohttp
import httpx as httpx
import pytest
from aioresponses import aioresponses

from src.main import app


@pytest.fixture
def mock_aiohttp() -> Generator[aioresponses, None, None]:
    with aioresponses() as m:
        yield m


@pytest.fixture
async def aiohttp_session() -> AsyncGenerator[aiohttp.ClientSession, None]:
    async with aiohttp.ClientSession() as session:
        yield session


@pytest.fixture
async def client() -> AsyncGenerator[httpx.AsyncClient, None]:
    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
