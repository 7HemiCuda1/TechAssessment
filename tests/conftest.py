import os
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--disable-gpu")
    chrome_prefs = {}
    options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    #TODO: make this support for windows too.
    driver = webdriver.Chrome(options=options)
    #executable_path='/usr/src/app/chromedriver',
    return driver

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

def pytest_addoption(parser):
    parser.addoption('--browser')



