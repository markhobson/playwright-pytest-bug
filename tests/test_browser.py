from playwright.sync_api import Page
from pytest_flask.live_server import LiveServer


def test_server(live_server: LiveServer, page: Page):
    pass


def test_browser(live_server: LiveServer, my_server: LiveServer, page: Page):
    pass
