from Pages.base_page import BasePage
from data import BasePageData


class Helper(BasePage):
    def __init__(self, *args, **kwargs):
        super(Helper, self).__init__(*args, **kwargs)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(BasePageData.BASE_URL + endpoint)
