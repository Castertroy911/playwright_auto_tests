from Pages.base_page import *
from helper import Helper


"""Здесь описываются основные действия, которые могут быть произведены с разными документами, 
на разных страницах. К примеру добавление Note и Comments абсолютно во всех жокументах одинаковое. Можно описать здесь 
эту логику один раз и потом просто переиспользовать ее для разных документов"""


class DocumentPage(Helper):
    def __init__(self, *args, **kwargs):
        super(DocumentPage, self).__init__(*args, **kwargs)

    def add_note(self):
        self.page.click(DocumentsPageLocators.ADD_NOTE)
        self.page.fill(DocumentsPageLocators.ENTER_TEXT_FIELD, DocumentsPageData.NOTE_TEXT)
        self.page.click(DocumentsPageLocators.SAVE_NOTE_BUTTON)

    def add_comment(self):
        self.page.click(DocumentsPageLocators.ADD_COMMENT)
        self.page.fill(DocumentsPageLocators.ENTER_TEXT_FIELD, DocumentsPageData.COMMENT_TEXT)
        self.page.click(DocumentsPageLocators.SAVE_COMMENT_BUTTON)

    def add_item_from_catalog_with_price(self):
        self.page.click(DocumentsPageLocators.ADD_ITEMS_BUTTON)
        self.page.click(DocumentsPageLocators.ADD_ITEMS_WITH_PRICE_BUTTON)
        self.page.click(DocumentsPageLocators.CLOSE_ADD_ITEMS_FORM)

    def delete_item(self):
        self.page.click(DocumentsPageLocators.DELETE_BUTTON)
        self.page.click(DocumentsPageLocators.CONFIRMATION_POP_UP_BUTTON_YES)

    def confirm_document(self):
        self.page.click(DocumentsPageLocators.CONFIRM_DOCUMENT)
        self.page.click(DocumentsPageLocators.CONFIRMATION_POP_UP_BUTTON_YES)
