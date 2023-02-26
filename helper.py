from Pages.base_page import *
from playwright.sync_api import TimeoutError


"""В этом хелпере описаны вспомогательные функции, которые могут быть полезны при автоматизации. Например наличие 
элемента на странице, наличие текста на странице. В соновном все функции должны возвращать булевое значение, чтобы
потом их можно было использовать в конструкции assert"""


class Helper(BasePage):
    def __init__(self, *args, **kwargs):
        super(Helper, self).__init__(*args, **kwargs)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url() + endpoint)

    def presence_of_element_located(self, locator, timeout=10000):
        try:
            self.page.locator(locator).wait_for(timeout=timeout)
        except TimeoutError:
            return False
        return True

    def element_is_not_present(self, locator, timeout=10000):
        try:
            self.page.wait_for_selector(locator, state='detached', timeout=timeout)
        except TimeoutError:
            return False
        return True






