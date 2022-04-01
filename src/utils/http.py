from typing import Any, Optional

import aiohttp


async def fetch(
    session: aiohttp.ClientSession, url: str, params: Optional[dict[str, Any]] = None
) -> Any:
    async with session.get(url, params=params or {}) as response:
        if response.status != 200:
            raise Exception(f"Error on fetching with status: {response.status}")

        return await response.json()
