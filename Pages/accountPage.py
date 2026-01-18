from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class AccountsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # 15-second wait for elements

        # Locators
        self.account_dropdown = (By.ID, "accountSelect")  # use ID for stability
        self.deposit_btn = (By.XPATH, "//button[@ng-click='deposit()']")
        self.amount_input = (By.XPATH, "//input[@ng-model='amount']")
        self.submit_deposit_btn = (By.XPATH, "//button[@type='submit']")
        self.deposit_success_msg = (By.XPATH, "//span[@class='error ng-binding']")  # adjust if needed
        self.balance_text = (By.XPATH, "//div[@class='center']/strong[2]")  # to get balance

    # Select account by index (works for <select>)
    def select_account_by_index(self, index):
        # Wait until the dropdown is visible
        self.wait.until(EC.visibility_of_element_located(self.account_dropdown))
        select_element = Select(self.driver.find_element(*self.account_dropdown))
        select_element.select_by_index(index)

    # Click deposit button
    def click_deposit_Btn(self):
        self.wait.until(EC.element_to_be_clickable(self.deposit_btn)).click()

    # Enter deposit amount
    def account_deposit(self, amount):
        input_field = self.wait.until(EC.visibility_of_element_located(self.amount_input))
        input_field.clear()
        input_field.send_keys(str(amount))

    # Click submit deposit button
    def clickSubmitDepBtn(self):
        self.wait.until(EC.element_to_be_clickable(self.submit_deposit_btn)).click()

    # Get deposit success message
    def get_deposit_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.deposit_success_msg)).text

    # Get current account balance
    def get_current_balance(self):
        balance_elem = self.wait.until(EC.visibility_of_element_located(self.balance_text))
        return float(balance_elem.text.strip())
