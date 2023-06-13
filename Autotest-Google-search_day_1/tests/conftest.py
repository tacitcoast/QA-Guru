import pytest
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def browser_size():
    browser.config.window_width = 1024
    browser.config.window_height = 768
