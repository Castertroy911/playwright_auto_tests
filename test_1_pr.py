from Pages.purchase_requisition_page import PurchaseRequisitionPage


class TestPurchaseRequisition:
    def test_create_pr(self, app):
        pr = PurchaseRequisitionPage(app)
        pr.create_new_pr()