import pytest

from faststream import TestApp
from faststream.nats import TestNatsBroker


@pytest.mark.asyncio
async def test_basic():
    from examples.nats.e03_publisher import app, broker, handler, response_handler

    async with TestNatsBroker(broker):
        async with TestApp(app):
            handler.mock.assert_called_once_with("Hi!")
            response_handler.mock.assert_called_once_with("Response")
