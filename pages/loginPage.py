from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from utils.config import STORE_PASSWORD


class LoginPage(BasePage):

    PASSWORD_INPUT = (By.NAME, "password")

    ENTER_BUTTON = (
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    def enter_store(self):
        password_field = self.wait_for_element(
            self.PASSWORD_INPUT
        )

        password_field.send_keys(STORE_PASSWORD)

        enter_button = self.wait_for_clickable(
            self.ENTER_BUTTON
        )

        enter_button.click()