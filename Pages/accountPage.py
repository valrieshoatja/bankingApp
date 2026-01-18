from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Pages.basePage import BasePage


class AccountsPage(BasePage):

    ACCOUNT_SELECT = (By.ID, "accountSelect")

    DEPOSIT_TAB = (By.XPATH, "//button[@ng-click='deposit()']")
    WITHDRAW_TAB = (By.XPATH, "//button[@ng-click='withdrawl()']")

    AMOUNT_INPUT = (By.XPATH, "//input[@ng-model='amount']")
    SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")

    SUCCESS_MSG = (By.XPATH, "//span[contains(text(),'Successful')]")

    BALANCE_TEXT = (By.XPATH, "(//strong[@class='ng-binding'])[2]")

    TRANSACTIONS_TAB = (By.XPATH, "//button[@ng-click='transactions()']")

    def select_account_by_index(self, index):
        dropdown = self.wait.until(lambda d: d.find_element(*self.ACCOUNT_SELECT))
        Select(dropdown).select_by_index(index)

    def get_current_balance(self):
        balance = self.get_text(self.BALANCE_TEXT)
        return int(balance)

    def click_deposit_tab(self):
        self.click(self.DEPOSIT_TAB)

    def click_withdraw_tab(self):
        self.click(self.WITHDRAW_TAB)

    def enter_amount(self, amount):
        self.type(self.AMOUNT_INPUT, amount)

    def click_submit(self):
        self.click(self.SUBMIT_BTN)

    def deposit_amount(self, amount):
        self.click_deposit_tab()
        self.enter_amount(amount)
        self.click_submit()

    def withdraw_amount(self, amount):
        self.click_withdraw_tab()
        self.enter_amount(amount)
        self.click_submit()

    def is_transaction_successful(self):
        return "Successful" in self.get_text(self.SUCCESS_MSG)

    def open_transactions(self):
        self.click(self.TRANSACTIONS_TAB)

    def click_deposit_Btn(self):
        pass
