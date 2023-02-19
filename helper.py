from Pages.base_page import *
from checker_helper import CheckerHelper
from base_helper import BaseHelper


"""В этом хелпере описаны вспомогательные функции, которые могут быть полезны при автоматизации. Например наличие 
элемента на странице, наличие текста на странице. В соновном все функции должны возвращать булевое значение, чтобы
потом их можно было использовать в конструкции assert"""


class Helper(BaseHelper, CheckerHelper):
    def __init__(self, *args, **kwargs):
        super(Helper, self).__init__(*args, **kwargs)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(BasePageData.BASE_URL + endpoint)

    def presence_of_element_located(self, locator):
        try:
            self.page.locator(locator).wait_for(timeout=10000)
        except TimeoutError:
            return False
        return True

