from Pages.base_page import BasePage
from helper import Helper
from base_helper import BaseHelper
from Locators.locators import *
from Data.data import *


"""В этом хелпере описываются все проверки, которые могут быть осуществлены с разными документами, на разных страницах.
К примеру мы хотим проверить, что у документа определенный статус или дата создания. Или хотим проверить, 
что добавился Note/Comment. Можно описать здесь эту логику один раз и потом просто переиспользовать ее для 
разных документов"""


class CheckerHelper(BasePage):
    def __init__(self, *args, **kwargs):
        super(CheckerHelper, self).__init__(*args, **kwargs)
        self.helper1 = Helper()
        self.base_helper = BaseHelper()

    def check_creation_date(self):
        creation_date = self.page.locator(DocumentsPageLocators.CREATION_DATE)
        creation_date = creation_date.text_content()
        assert PurchaseRequisitionData.DELIVERY_DATE == creation_date, "Creation date is invalid"

    def check_document_status(self, status):
        assert self.helper1.presence_of_element_located(f"//span[@class='badge status.{status}']"), \
            f"Document status is not '{status}'"

    def check_note_saved(self):
        assert self.helper1.presence_of_element_located(DocumentsPageLocators.SAVED_NOTE), "Note is not saved"

    def check_comment_saved(self):
        assert self.helper1.presence_of_element_located(DocumentsPageLocators.SAVED_COMMENT), "Comment is not saved"

    def check_item_added(self):
        assert self.helper1.presence_of_element_located(DocumentsPageLocators.ITEMS_LIST), "Item is not added"

    def check_item_deleted(self):
        assert self.helper1.presence_of_element_located(DocumentsPageLocators.ITEMS_LIST) is False, "Item is not deleted"
