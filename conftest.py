from playwright.sync_api import sync_playwright
from pytest import fixture
from data import BasePageData
from locators import LoginPageLocators


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='session')
def app(get_playwright):
    browser = get_playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(BasePageData.BASE_URL)
    page.click(LoginPageLocators.LOG_IN)
    page.fill(LoginPageLocators.USERNAME, BasePageData.USER_EMAIL)
    page.fill(LoginPageLocators.PASSWORD, BasePageData.USER_PASSWORD)
    page.click(LoginPageLocators.LOGIN_BUTTON)
    yield page
    browser.close()