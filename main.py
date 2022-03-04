from helpers.reusable_browser import *
import pytest


@pytest.mark.usefixtures('driver')
class TestBrowserNavigation:

    def test_navigate(self):
        print(self.driver)
        self.driver.get("https://stackoverflow.com/")

    def test_click_on_login_button(self):
        self.driver.find_element_by_xpath("//a[contains(@class, 'login-link')]").click()

    def test_input_email(self):
        self.driver.find_element_by_id("email").send_keys("username")

    def test_input_password(self):
        self.driver.find_element_by_id("password").send_keys("username")
