import asyncio

import pytest
import pytest_asyncio
from httpx import AsyncClient


@pytest_asyncio.fixture(scope="module")
async def api_client():
    client = AsyncClient(app=app, base_url="http://localhost:8000/")
    yield client
    await client.aclose()


@pytest.fixture(scope="session")
def event_loop(request):
    """
    Create an instance of the default event loop for each test case.
    This fixture overrides the internal event_loop fixture, and is used to
    avoid the issue presented in: https://github.com/pytest-dev/pytest-asyncio/issues/38
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
