"""
Переопределите параметр с помощью indirect
"""
from selene.support.shared import browser
from model.pages import github_main_page
import pytest


@pytest.fixture()
def browser_conf(request):
    window_size = request.param
    browser.config.window_width = window_size[0]
    browser.config.window_height = window_size[1]


@pytest.mark.parametrize('browser_conf', [[1920, 1080]], indirect=True)
def test_github_desktop(browser_conf):
    github_main_page.given_opened()
    github_main_page.sign_in_dekstop()


@pytest.mark.parametrize('browser_conf', [[412, 914]], indirect=True)
def test_github_mobile(browser_conf):
    github_main_page.given_opened()
    github_main_page.sign_in_mobile()
