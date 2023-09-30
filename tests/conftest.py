from typing import Generator

import pytest
from pytest_flask.live_server import LiveServer
from flask import Flask


@pytest.fixture(scope="session")
def my_server(request: pytest.FixtureRequest) -> Generator[LiveServer, None, None]:
    app = Flask("app")
    server = LiveServer(app, "localhost", 8080, True)
    server.start()
    yield server
    server.stop()
