from helper import Helper


class PurchaseRequisitionPage(Helper):
    def create_new_pr(self):
        self.goto("/purchase/requisition/create/manual")
        self.page.fill("[name='date']", "08.02.2023")
        self.page.fill("[name='document_costcenter_19457']", "test")
        self.page.fill("[name='document_costcenter_19458'] [name = 'date']", "08.02.2023")
        self.page.fill("//label[text()='testing 2 ']/following-sibling::div//input[@type='text']", "1")
        self.page.press("//label[text()='testing 2 ']/following-sibling::div//input[@type='text']", "Enter")
        self.page.press("//label[text()='testing 2 ']/following-sibling::div//input[@type='text']", "Enter")
        self.page.click(".btn2.btn2--primary.btn2--large")

