from Pages.warehouse_request_page import WarehouseRequestPage
from Locators.locators import *
import pytest


@pytest.mark.smoke
class TestCreateWarehouseRequest:
    def test_create_warehouse_request(self, app):
        wr = WarehouseRequestPage(app)
        wr.create_new_wr('not_approval')
        wr.check_document_status(DocumentsPageLocators.STATUS_DRAFT)
        wr.check_creation_date()
        wr.add_note()
        wr.check_note_saved()
        wr.add_comment()
        wr.check_comment_saved()
        wr.add_item_from_catalog_with_price()
        wr.check_item_added()
        wr.delete_item()
        wr.check_item_deleted()
        wr.add_item_from_catalog_with_price()
        wr.confirm_document()
        wr.check_document_status(DocumentsPageLocators.STATUS_APPROVED)

