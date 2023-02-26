import datetime


class LoginPageData:
    BASE_URL_PRECORO = "https://precoro.com"
    BASE_URL_D_PRECORO = "https://d.precoro.com"

    TRIAL_NAME = "trial_autotest"
    TRIAL_EMAIL = f"trial_autotest{datetime.datetime.today()}@qwerty.com"
    TRIAL_PHONE = "+380000000000"
    TRIAL_COMPANY_NAME = f"trial_autotest{datetime.datetime.today()}"
    TRIAL_NUMBER_OF_USERS = "Only me"


class CreateDocumentsData:
    PR_CREATION_PAGE = "/purchase/requisition/create/manual"
    WR_CREATION_PAGE = "/warehouse/request/create"
    DELIVERY_DATE = datetime.datetime.today().strftime("%m.%d.%Y")
    NOT_APPROVAL_DCC = "Option 1"
    APPROVAL_DCC = "ApprovalDCC"


class DocumentsPageData:
    NOTE_TEXT = "Autotest note"
    COMMENT_TEXT = "Autotest comment"


class InventoryPageData:
    INVENTORY_PAGE = "/manage/inventory"
    QTY = "50"
    LOW_QTY = "10"
    REORDER_TO = "20"
    MINIMUM_STOCK_LVL = "15"
