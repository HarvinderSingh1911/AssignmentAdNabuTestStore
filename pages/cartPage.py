from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.basePage import BasePage



class CartPage(BasePage):

    CART_QUANTITY = (By.CSS_SELECTOR, "input.quantity__input")

    def validate_cart_quantity(self, expected_qty=1):
        """Validate product quantity in cart"""

        quantity_input = self.wait.until(
            EC.visibility_of_element_located(self.CART_QUANTITY)
        )

        actual_qty = int(quantity_input.get_attribute("value"))

        assert actual_qty == expected_qty, (
            f"Expected quantity {expected_qty}, but got {actual_qty}"
        )

        print("cart quantity is correct:", actual_qty)