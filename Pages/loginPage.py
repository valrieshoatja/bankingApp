from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Pages.basePage import BasePage


class LoginPage(BasePage):

    BTN_CUSTOMER_LOGIN = (By.XPATH, "//button[normalize-space()='Customer Login']")
    USER_SELECT = (By.ID, "userSelect")
    BTN_LOGIN = (By.XPATH, "//button[normalize-space()='Login']")

    def clickCustomerLogin(self):
        self.click(self.BTN_CUSTOMER_LOGIN)

    def selectUserByText(self, customer_name):
        dropdown = self.wait.until(lambda d: d.find_element(*self.USER_SELECT))
        Select(dropdown).select_by_visible_text(customer_name)

    def clickLogin(self):
        self.click(self.BTN_LOGIN)
