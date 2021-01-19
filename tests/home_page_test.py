import pytest
from time import sleep
from Pages.HomePage import HomePage
from Pages.AuthPage import AuthPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Test_HomePage:
    baseURL = "https://www.podium.com/"

    # TODO: Create the setup and teardown.
    # pytest -s -v --html=Reports/report.html tests/
    # TODO: Add logging

    def chat_button(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.driver.maximize_window()
        self.hp.click_chat_btn()
        #TODO: Add assert for chat form.
        self.driver.close()

    def for_platform(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.driver.maximize_window()
        self.hp.platformFooterLink()
        #TODO: Add assert for new page.
        self.driver.close()

    def slider_function(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.driver.maximize_window()
        try:
            self.hp.click_slider_left()
        finally:
            self.hp.correct_slider_image_displayed(4)
        try:
            self.hp.click_slider_right()
        finally:
            self.hp.correct_slider_image_displayed(1)

        self.driver.close()

    def test_login_page_navigation(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.driver.maximize_window()
        try:
            self.hp.click_login_btn()

        finally:
            self.lp = AuthPage(self.driver)
            self.driver.close()

