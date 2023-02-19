class LoginPageLocators:
    LOG_IN = ".header__controls-list__link"
    USERNAME = "#username"
    PASSWORD = "#password"
    LOGIN_BUTTON = ".login-form-submit"


class PurchaseRequisitionPageLocators:
    PR_CREATION_PAGE = "/purchase/requisition/create/manual"
    DELIVERY_DATE_LOCATOR = "[name='date']"
    DCC_ICF_LOCATOR = "//label[text()='DCC ']/following-sibling::div//input"
    CREATE_BUTTON = ".btn2.btn2--primary.btn2--large"


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
    CONFIRMATION_POP_UP_BUTTON_YES = "//div[@class='v-dialog__buttons']"
    CONFIRMATION_POP_UP_BUTTON_NO = "//button[@class='v-button v-button--white-danger v-button--full']"

    CONFIRM_DOCUMENT = "//div[@class='btn2-group']//button[@class='btn2 btn2--success btn2--block']"

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