from Pages.base_page import *


@pytest.fixture(scope='session')
def go_to_the_warehouse(app, base_page):
    app.goto(base_page.base_url() + InventoryPageData.INVENTORY_PAGE)
    app.click(InventoryPageLocators.OPEN_WAREHOUSE)
