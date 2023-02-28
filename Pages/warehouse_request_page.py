from check_helper import CheckHelper
from Pages.base_page import *


class WarehouseRequestPage(CheckHelper):
    def create_new_wr(self, approval_flow):
        self.goto(CreateDocumentsData.WR_PAGE)
        self.page.click(CreateDocumentsPageLocators.CREATE_WAREHOUSE_REQUEST)
        self.page.fill(CreateDocumentsPageLocators.DELIVERY_DATE_LOCATOR, CreateDocumentsData.DELIVERY_DATE)
        self.page.fill(CreateDocumentsPageLocators.POST_TO_WAREHOUSE_OPTION, CreateDocumentsData.WAREHOUSE_NAME)
        self.page.click(CreateDocumentsPageLocators.DCC_ICF_LOCATOR)
        if approval_flow == 'approval':
            self.page.fill(CreateDocumentsPageLocators.DCC_ICF_LOCATOR, CreateDocumentsData.APPROVAL_DCC)
        else:
            self.page.fill(CreateDocumentsPageLocators.DCC_ICF_LOCATOR, CreateDocumentsData.NOT_APPROVAL_DCC)
        self.page.press(CreateDocumentsPageLocators.DCC_ICF_LOCATOR, "Enter")
        self.page.click(CreateDocumentsPageLocators.CREATE_BUTTON)
