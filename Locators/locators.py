class LoginPageLocators:
    LOG_IN = ".header__controls-list__link"
    USERNAME = "#username"
    PASSWORD = "#password"
    LOGIN_BUTTON = ".login-form-submit"
    TRIAL_BUTTON = "//a[contains(@href, 'get-a-trial')]"
    TRIAL_FULL_NAME = "//input[@id='company_request_trial_userFirstName']"
    TRIAL_EMAIL = "//input[@id='company_request_trial_email']"
    TRIAL_PHONE = "//input[@id='company_request_trial_phone']"
    TRIAL_COMPANY_NAME = "//input[@id='company_request_trial_companyName']"
    TRIAL_NUMBER_OF_USERS = "//select[@id='company_request_trial_countUsers']"
    CREATE_TRIAL_BUTTON = "//button[@class='signup-submit new-btn new-btn--primary new-btn--rounded']"


class CreateDocumentsPageLocators:
    DELIVERY_DATE_LOCATOR = "[name='date']"
    DCC_ICF_LOCATOR = "//label[text()='DCC ']/following-sibling::div//input"
    CREATE_BUTTON = ".btn2.btn2--primary.btn2--large"
    POST_TO_WAREHOUSE_OPTION = "//label[contains(text(), 'Post to Warehouse')]/ancestor::div[@class='input-wrap']" \
                               "//div[@class='vue-treeselect__input-container']/input"
    CREATE_WAREHOUSE_REQUEST = "//a[@class='btn2 btn2--success btn2--block btn2--large']"


class DocumentsPageLocators:
    CREATION_DATE = "//h4[text()='Creation Date']/following-sibling::span"

    ADD_NOTE = "//button[contains(text(), 'Add Note')]"
    SAVED_NOTE = "//div[@class='view-note']/p"
    ADD_COMMENT = "//button[contains(text(), 'Add comment')]"
    SAVED_COMMENT = "//div[@class='link_text']/p"
    ENTER_TEXT_FIELD = "//div[@class='ql-editor ql-blank']"
    SAVE_NOTE_BUTTON = "//button[@class='btn2 btn2--success btn2--block' and @type='submit']"
    SAVE_COMMENT_BUTTON = "//button[@id='save_button_comment']"

    ADD_ITEMS_BUTTON = "//button[@class='btn2 btn2--primary inline_button']"
    ADD_ITEMS_WITH_PRICE_BUTTON = \
        "//span[contains(text(), 'USD')]/ancestor::td/following-sibling::td/div[@class = 'add_from_catalog_button']"
    CLOSE_ADD_ITEMS_FORM = "//span[@class='icon-icon_cancel']"
    ITEMS_LIST = "//tr[@class='listItem']"
    DELETE_BUTTON = "//button[@class='el-tooltip remove_button']"
    CONFIRMATION_POP_UP_BUTTON_YES = "//div[@class='v-dialog__buttons']/a"
    CONFIRMATION_POP_UP_BUTTON_NO = "//button[@class='v-button v-button--white-danger v-button--full']"

    CONFIRM_DOCUMENT = "//div[@class='btn2-group']//a[@class='btn2 btn2--success btn2--block']"

    STATUS_DRAFT = "open"
    STATUS_APPROVED = "approved"
    STATUS_RECEIVED = "received"
    STATUS_COMPLETED = "purchased"
    STATUS_PAID = "paid"
    STATUS_NOT_BILLED = "need_create_bill"
    STATUS_PENDING_CONFIRMATION = "awaiting_confirmation"
    STATUS_PREPAID = "prepaid"
    STATUS_PENDING = "pending"
    STATUS_REJECTED = "denied"
    STATUS_CANCELED = "canceled"


class InventoryPageLocators:
    OPEN_WAREHOUSE = "//tbody//td[5]"
    EDIT_BUTTON = "//button[@class='el-tooltip edit_button']"
    QTY = "//td[text()='1']//following-sibling::td//input[@name='quantity_0']"
    QTY_SAVED_VALUE = "//td[text()='1']/following-sibling::td[6]//b"
    MINIMUM_STOCK_LVL = "//td[text()='1']//following-sibling::td//input[@name='minimumStockLevel_0']"
    MINIMUM_STOCK_LVL_SAVED_VALUE = "//td[text()='1']/following-sibling::td[7]//b"
    REORDER_TO = "//td[text()='1']//following-sibling::td//input[@name='reorderTo_0']"
    REORDER_TO_SAVED_VALUE = "//td[text()='1']/following-sibling::td[8]//b"
    NEED_TO_ORDER = "//td[text()='1']/following-sibling::td[9]//b"
    SAVE_BUTTON = "//button[@class='el-tooltip edit_button accepted']"
    CANCEL_BUTTON = "//button[@class='el-tooltip remove_button done']"
    YELLOW_CIRCLE_LOW_STOCK = "//span[@class='el-tooltip dot warning']"
    RED_CIRCLE_LOW_STOCK = "//span[@class='el-tooltip dot alert']"
