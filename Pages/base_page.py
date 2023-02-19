from playwright.sync_api import Page
from Locators.locators import *
from Data.data import *


class BasePage:
    def __init__(self, app: Page):
        self.page = app
