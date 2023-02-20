from helper import Helper
from base_page import *


class LoginPage(Helper):
    def create_trial(self):
        self.goto("/")
        self.page.click(LoginPageLocators.TRIAL_BUTTON)
        self.page.fill(LoginPageLocators.TRIAL_FULL_NAME, LoginPageData.TRIAL_NAME)
        self.page.fill(LoginPageLocators.TRIAL_EMAIL, LoginPageData.TRIAL_EMAIL)
        self.page.fill(LoginPageLocators.TRIAL_PHONE, LoginPageData.TRIAL_PHONE)
        self.page.fill(LoginPageLocators.TRIAL_COMPANY_NAME, LoginPageData.TRIAL_COMPANY_NAME)
        self.page.select_option(LoginPageLocators.TRIAL_NUMBER_OF_USERS, LoginPageData.TRIAL_NUMBER_OF_USERS)
        self.page.click(LoginPageLocators.CREATE_TRIAL_BUTTON)