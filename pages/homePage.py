from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.basePage import BasePage


class HomePage(BasePage):

    SEARCH_ICON = (By.CSS_SELECTOR, 'summary[aria-label="Search"]')
    SEARCH_BOX = (By.CSS_SELECTOR, 'input[type="search"]')

    FIRST_PRODUCT = (By.CSS_SELECTOR, "ul.product-grid li:first-child a")

    ADD_TO_CART = (By.CSS_SELECTOR, "button[name='add']")

    def search_product(self, product_name):

        self.wait_for_clickable(self.SEARCH_ICON).click()

        search_box = self.wait_for_element(self.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.ENTER)

    def open_first_product(self):

        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "ul.product-grid")
            )
        )

        first_product = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "ul.product-grid a.full-unstyled-link")
            )
        )

        self.driver.execute_script("arguments[0].click();", first_product)

    def add_to_cart(self):

        self.wait_for_clickable(self.ADD_TO_CART).click()