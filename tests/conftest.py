import pytest
from flask import Flask


@pytest.fixture(scope="session")
def app() -> Flask:
    return Flask("app")
