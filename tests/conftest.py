import os
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    options = Options()
    options.add_argument("--no-sandbox")
    #options.add_argument("--headless")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    chrome_prefs = {}
    options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
#executable_path='/usr/src/app/chromedriver'
    driver = webdriver.Chrome(options=options)
    return driver

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

def pytest_addoption(parser):
    parser.addoption('--browser')


