from playwright.sync_api import sync_playwright
from pytest import fixture
from Data.data import *
from Locators.locators import *
from Pages.base_page import BasePage


@fixture(scope='session')
def base_page():
    return BasePage()


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='session')
def app(get_playwright, base_page):
    browser = get_playwright.chromium.launch(headless=False)
    context = browser.new_context(http_credentials={"username": "tester", "password": "563282367"})
    page = context.new_page()
    page.goto(base_page.base_url())
    page.click(LoginPageLocators.LOG_IN)
    page.fill(LoginPageLocators.USERNAME, LoginPageData.USER_EMAIL)
    page.fill(LoginPageLocators.PASSWORD, LoginPageData.USER_PASSWORD)
    page.click(LoginPageLocators.LOGIN_BUTTON)
    yield page
    browser.close()

