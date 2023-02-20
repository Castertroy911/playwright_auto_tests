from playwright.sync_api import sync_playwright
from pytest import fixture
from Data.data import LoginPageData
from Locators.locators import LoginPageLocators


def pytest_addoption(parser):
    parser.addoption('--base_url', action='store', default='https://precoro.com')


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='session')
def app(get_playwright, request):
    browser = get_playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    base_url = request.config.getoption('--base_url')
    page.goto(base_url)
    page.click(LoginPageLocators.LOG_IN)
    page.fill(LoginPageLocators.USERNAME, LoginPageData.USER_EMAIL)
    page.fill(LoginPageLocators.PASSWORD, LoginPageData.USER_PASSWORD)
    page.click(LoginPageLocators.LOGIN_BUTTON)
    yield page
    browser.close()
