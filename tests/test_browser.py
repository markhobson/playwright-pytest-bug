from playwright.sync_api import Page
from pytest_flask.live_server import LiveServer


def test_page(page: Page):
    pass


def test_server_and_page(live_server: LiveServer, page: Page):
    pass
