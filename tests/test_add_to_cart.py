from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.cartPage import CartPage

from utils.config import BASE_URL, PRODUCT_NAME


class TestAddToCart:

    def setup_method(self):
        self.driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            )
        )

        self.driver.maximize_window()
        self.driver.get(BASE_URL)

    def teardown_method(self):
        self.driver.quit()

    def test_search_and_add_to_cart(self):

        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        cart_page = CartPage(self.driver)


        login_page.enter_store()

        home_page.search_product(PRODUCT_NAME)

        home_page.open_first_product()

        home_page.add_to_cart()
        cart_page.validate_cart_quantity(1)

        print("TEST PASSED")
        
if __name__ == "__main__":

    test = TestAddToCart()

    test.setup_method()

    try:
        test.test_search_and_add_to_cart()

    finally:
        test.teardown_method()