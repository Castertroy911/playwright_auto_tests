from check_helper import CheckHelper
from Pages.base_page import *


class InventoryPage(CheckHelper):
    def add_qty_to_item(self):
        self.page.click(InventoryPageLocators.EDIT_BUTTON)
        self.page.fill(InventoryPageLocators.QTY, InventoryPageData.QTY)
        self.page.click(InventoryPageLocators.SAVE_BUTTON)
        self.page.reload()

    def check_item_qty_saved(self):
        saved_qty = self.page.locator(InventoryPageLocators.QTY_SAVED_VALUE).text_content().strip()
        assert saved_qty == InventoryPageData.QTY, "Item QTY is not saved"

    def add_minimum_stock_lvl(self):
        self.page.click(InventoryPageLocators.EDIT_BUTTON)
        self.page.fill(InventoryPageLocators.MINIMUM_STOCK_LVL, InventoryPageData.MINIMUM_STOCK_LVL)
        self.page.click(InventoryPageLocators.SAVE_BUTTON)
        self.page.reload()

    def check_item_minimum_stock_lvl_saved(self):
        saved_minimum_stock_lvl = self.page.locator(InventoryPageLocators.MINIMUM_STOCK_LVL_SAVED_VALUE).\
            text_content().strip()
        assert saved_minimum_stock_lvl == InventoryPageData.MINIMUM_STOCK_LVL, "Item minimum stock lvl isn't saved"

    def add_reorder_to(self):
        self.page.click(InventoryPageLocators.EDIT_BUTTON)
        self.page.fill(InventoryPageLocators.REORDER_TO, InventoryPageData.REORDER_TO)
        self.page.click(InventoryPageLocators.SAVE_BUTTON)
        self.page.reload()

    def check_item_reorder_to_value_saved(self):
        reorder_to_value = self.page.locator(InventoryPageLocators.REORDER_TO_SAVED_VALUE).text_content().strip()
        assert reorder_to_value == InventoryPageData.REORDER_TO, "Reorder To value isn't saved"

    def make_low_stock_qty(self):
        self.page.click(InventoryPageLocators.EDIT_BUTTON)
        self.page.fill(InventoryPageLocators.QTY, InventoryPageData.LOW_QTY)
        self.page.click(InventoryPageLocators.SAVE_BUTTON)
        self.page.reload()

    def check_need_to_order_value(self):
        need_to_order_value_should_be = int(InventoryPageData.REORDER_TO) - int(InventoryPageData.LOW_QTY)
        need_to_order_actual_value = self.page.locator(InventoryPageLocators.NEED_TO_ORDER).text_content().strip()
        assert need_to_order_value_should_be == int(need_to_order_actual_value), "Need to order value isn't correct"

    def check_low_stock_alert(self):
        try:
            red_low_stock = self.presence_of_element_located(InventoryPageLocators.RED_CIRCLE_LOW_STOCK, timeout=3000)
            assert red_low_stock, "Low stock alert icon isn't displayed"
        except TimeoutError:
            pass
        yellow_low_stock = self.presence_of_element_located(InventoryPageLocators.YELLOW_CIRCLE_LOW_STOCK, timeout=3000)
        assert yellow_low_stock, "Low stock alert icon isn't displayed"
