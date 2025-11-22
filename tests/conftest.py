import pytest
from selene import browser


@pytest.fixture
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 12
    browser.config.base_url = "https://demowebshop.tricentis.com"

    yield
    browser.quit()