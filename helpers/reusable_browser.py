import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from helpers.config_helper import *


def create_driver_session():
    caps = DesiredCapabilities.CHROME
    caps['loggingPrefs'] = {'performance': 'ALL'}
    chrome_options = Options()
    driver = webdriver.Chrome(
        options=chrome_options,
        desired_capabilities=caps,
        executable_path=get_config('driver_path')
    )
    driver.maximize_window()
    set_config('session', 'session_id', driver.session_id)
    set_config('session', 'ce_url', driver.command_executor._url)
    time.sleep(60000)


def resume_driver_session():
    session_id = get_config('session', 'session_id')
    ce_url = get_config('session', 'ce_url'),
    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
    # Save the original function so we can revert our patch
    org_command_execute = RemoteWebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == 'newSession':
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)

    # Patch the function before creating the driver object
    RemoteWebDriver.execute = new_command_execute
    # Create the driver
    new_driver = webdriver.Remote(command_executor=ce_url, desired_capabilities={})
    new_driver.session_id = session_id
    # Replace the patched function with original function
    RemoteWebDriver.execute = org_command_execute
    return new_driver
