"""
Сделайте разные фикстуры для каждого теста
"""
from selene.support.shared import browser
from model.pages import github_main_page
import pytest


@pytest.fixture()
def desktop_size():
   browser.config.window_width = 1920
   browser.config.window_height = 1080


@pytest.fixture()
def mobile_size():
   browser.config.window_width = 412
   browser.config.window_height = 914


def test_github_desktop(desktop_size):
    github_main_page.given_opened()
    github_main_page.sign_in_dekstop()


def test_github_mobile(mobile_size):
    github_main_page.given_opened()
    github_main_page.sign_in_mobile()
