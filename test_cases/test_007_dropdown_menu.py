from test_cases.test_case_with_selenium import TestCaseWithSelenium
from utilities.read_properties import ReadConfig


class TestDropdownMenu(TestCaseWithSelenium):
    def setUp(self) -> None:
        super().setUp()

        # perform a successful login
        self.login_page.login_with_standard_username_and_password()

        # open drop-down-menu
        self.inventory_page.click_dropdown_menu()

    # test dropdown menu functionality

    def test_dropdown_menu_elements_displayed(self):
        # dropdown menu should be opened and all elements visible
        condition = self.inventory_page.check_if_dropdown_menu_visible()
        screenshot_name = "test_dropdown_menu_elements_displayed.png"
        self.assert_and_take_screenshot_if_failed(condition, screenshot_name)

    def test_dropdown_menu_close_button(self):
        # close the dropdown menu by clicking 'X' button
        self.inventory_page.click_dropdown_menu_close_button()

        # dropdown menu should be closed - not visible
        condition = self.inventory_page.check_if_dropdown_menu_visible()
        screenshot_name = "test_dropdown_menu_close_button.png"
        self.assert_and_take_screenshot_if_failed(not condition, screenshot_name)

    def tearDown(self) -> None:
        self.driver.quit()
