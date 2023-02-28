from Pages.purchase_requisition_page import PurchaseRequisitionPage
from Locators.locators import *
import pytest


@pytest.mark.smoke
class TestCreatePurchaseRequisition:
    def test_create_pr(self, app):
        pr = PurchaseRequisitionPage(app)
        pr.create_new_pr('not_approval')
        pr.check_document_status(DocumentsPageLocators.STATUS_DRAFT)
        pr.check_creation_date()
        pr.add_note()
        pr.check_note_saved()
        pr.add_comment()
        pr.check_comment_saved()
        pr.add_item_from_catalog_with_price()
        pr.check_item_added()
        pr.delete_item()
        pr.check_item_deleted()
        pr.add_item_from_catalog_with_price()
        pr.confirm_document()
        pr.check_document_status(DocumentsPageLocators.STATUS_APPROVED)
