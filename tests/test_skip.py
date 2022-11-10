"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from model.pages import github_main_page
from selene.support.shared import browser


def check_size_before_test(data, type_test):
    if data[2] != type_test:
        pytest.skip(f'This isn\'t {type_test}')
    browser.config.window_width = data[0]
    browser.config.window_height = data[1]


@pytest.mark.parametrize('browser_size', [(1920, 1080, 'desktop'), (412, 914, 'mobile')], ids=['desktop', 'mobile'])
def test_github_desktop(browser_size):
    check_size_before_test(browser_size, 'desktop')
    github_main_page.given_opened()
    github_main_page.sign_in_dekstop()


@pytest.mark.parametrize('browser_size', [(1920, 1080, 'desktop'), (412, 914, 'mobile')], ids=['desktop', 'mobile'])
def test_github_mobile(browser_size):
    check_size_before_test(browser_size, 'mobile')
    github_main_page.given_opened()
    github_main_page.sign_in_mobile()
