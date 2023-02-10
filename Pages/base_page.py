from playwright.sync_api import Page


class BasePage:
    def __init__(self, app: Page):
        self.page = app
