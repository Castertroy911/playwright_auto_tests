from check_helper import CheckHelper
from base_page import *


class PurchaseRequisitionPage(CheckHelper):
    def create_new_pr(self, approval_flow):
        self.goto(CreateDocumentsData.PR_CREATION_PAGE)
        self.page.fill(CreateDocumentsPageLocators.DELIVERY_DATE_LOCATOR, CreateDocumentsData.DELIVERY_DATE)
        self.page.click(CreateDocumentsPageLocators.DCC_ICF_LOCATOR)
        if approval_flow == 'approval':
            self.page.fill(CreateDocumentsPageLocators.DCC_ICF_LOCATOR, CreateDocumentsData.APPROVAL_DCC)
        else:
            self.page.fill(CreateDocumentsPageLocators.DCC_ICF_LOCATOR, CreateDocumentsData.NOT_APPROVAL_DCC)
        self.page.press(CreateDocumentsPageLocators.DCC_ICF_LOCATOR, "Enter")
        self.page.click(CreateDocumentsPageLocators.CREATE_BUTTON)