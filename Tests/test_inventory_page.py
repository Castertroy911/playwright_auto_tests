import pytest

from Pages.inventory_page import InventoryPage


@pytest.mark.smoke
class TestInventoryPage:
    def test_qty(self, app, go_to_the_warehouse):
        inventory_page = InventoryPage(app)
        inventory_page.add_qty_to_item()
        inventory_page.check_item_qty_saved()

    def test_minimum_stock_lvl(self, app):
        inventory_page = InventoryPage(app)
        inventory_page.add_minimum_stock_lvl()
        inventory_page.check_item_minimum_stock_lvl_saved()

    def test_reorder_to(self, app):
        inventory_page = InventoryPage(app)
        inventory_page.add_reorder_to()
        inventory_page.check_item_reorder_to_value_saved()

    def test_make_item_low_stock(self, app):
        inventory_page = InventoryPage(app)
        inventory_page.make_low_stock_qty()
        inventory_page.check_need_to_order_value()
        inventory_page.check_low_stock_alert()