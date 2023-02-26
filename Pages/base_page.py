from playwright.sync_api import Page
from Data.data import LoginPageData
from Data.data import *
from Locators.locators import *
from playwright.sync_api import TimeoutError
import pytest


class BasePage:
    def __init__(self, app=Page):
        self.page = app

    def base_url(self):
        return LoginPageData.BASE_URL_D_PRECORO