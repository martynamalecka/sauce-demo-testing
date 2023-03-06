from test_cases.test_case_with_selenium import TestCaseWithSelenium
from utilities.read_properties import ReadConfig


class TestAddToCart(TestCaseWithSelenium):
    def setUp(self) -> None:
        super().setUp()

        # perform a successful login
        self.login_page.login_with_standard_username_and_password()

    # test shopping cart functionality

    def test_add_to_cart(self):
        # add one item to the cart and go to the shopping cart
        self.inventory_page.click_add_to_cart()
        self.inventory_page.click_shopping_cart()

        # the item should be displayed in the cart
        condition = self.shopping_cart_page.is_any_item_displayed()
        screenshot_name = "test_add_to_cart.png"
        self.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def tearDown(self) -> None:
        self.driver.quit()
