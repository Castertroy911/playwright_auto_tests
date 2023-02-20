from check_helper import CheckHelper
from Locators.locators import *
from Data.data import *


class PurchaseRequisitionPage(CheckHelper):
    def create_new_pr(self, *approval_flow):
        self.goto(PurchaseRequisitionPageLocators.PR_CREATION_PAGE)
        self.page.fill(PurchaseRequisitionPageLocators.DELIVERY_DATE_LOCATOR, PurchaseRequisitionData.DELIVERY_DATE)
        self.page.click(PurchaseRequisitionPageLocators.DCC_ICF_LOCATOR)
        if approval_flow == 'approval':
            self.page.fill(PurchaseRequisitionPageLocators.DCC_ICF_LOCATOR, PurchaseRequisitionData.APPROVAL_DCC)
        else:
            self.page.fill(PurchaseRequisitionPageLocators.DCC_ICF_LOCATOR, PurchaseRequisitionData.NOT_APPROVAL_DCC)
        self.page.press(PurchaseRequisitionPageLocators.DCC_ICF_LOCATOR, "Enter")
        self.page.click(PurchaseRequisitionPageLocators.CREATE_BUTTON)

