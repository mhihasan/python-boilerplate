from typing import Any, Optional

import aiohttp


async def get(
    session: aiohttp.ClientSession, url: str, params: Optional[dict[str, Any]] = None
) -> Any:
    async with session.get(url, params=params or {}) as response:
        return await response.json()


async def post(session: aiohttp.ClientSession, url: str, json: dict[str, Any]) -> Any:
    async with session.post(url, json=json) as response:
        return await response.json()
