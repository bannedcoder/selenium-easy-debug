from helpers.reusable_browser import *
import pytest
from selenium.webdriver.common.keys import Keys
from venv.cred import cred


@pytest.mark.usefixtures('driver')
class TestBrowserNavigation:

    def test_navigate(self):
        print(self.driver)
        self.driver.get("https://stackoverflow.com/")

    def test_click_on_login_button(self):
        self.driver.find_element_by_xpath("//a[contains(@class, 'login-link')]").click()

    def test_input_email(self):
        self.driver.find_element_by_id("email").send_keys(cred['username'])

    def test_input_password(self):
        self.driver.find_element_by_id("password").send_keys(cred['password'])

    def test_click_on_login(self):
        self.driver.find_element_by_xpath("//button[contains(@id, 'submit-button')]").click()
        time.sleep(3)

    def test_search_for_python(self):
        self.driver.find_element_by_name("q").click()
        self.driver.find_element_by_name("q").send_keys("python")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
