import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def browser_management():
    browser.config.timeout = 10
    browser.config.base_url = 'https://github.com'
    browser.config.browser_name = 'chrome'
    yield
    browser.close()
