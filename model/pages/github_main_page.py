from selene.support.shared import browser
from selene import have


def given_opened():
    browser.open('/')


def sign_in_dekstop():
    browser.element('a[href="/login"]').click()
    browser.element('h1').should(have.text('Sign in to GitHub'))


def sign_in_mobile():
    browser.element('.flex-1 button[aria-label="Toggle navigation"]').click()
    sign_in_dekstop()

