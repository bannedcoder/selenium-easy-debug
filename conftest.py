from helpers.config_helper import get_config
from helpers.reusable_browser import *
from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def driver(request):
    if get_config('env', 'debug') == 'True':
        driver = resume_driver_session()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
