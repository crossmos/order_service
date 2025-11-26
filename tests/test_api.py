import aiohttp
import pytest


@pytest.mark.asyncio
async def test_order_create(order_json):
    async with aiohttp.ClientSession() as session:
        r = await session.post(
            "http://localhost:8000/api/orders",
            data=order_json,
        )
    response_json = await r.json()
    assert response_json["status"] == "published"
