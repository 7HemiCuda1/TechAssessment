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
        # TODO Clean this up and move to the class.
        self.driver.find_element_by_xpath(self.hp.podiumChatbtn)
        self.driver.close()

    def for_platform(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.driver.maximize_window()
        # TODO Clean this up and move to the class.
        assert self.driver.find_element_by_xpath(self.hp.platformFooterLink)
        self.driver.close()

    def slider_function(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.driver.maximize_window()
        #TODO Clean this up and move to the class.
        try:
            wait = WebDriverWait(self.driver,
                                 10).until(EC.presence_of_element_located((By.ID, self.hp.sliderLeftId))).click()
        finally:
            assert self.driver.find_element_by_xpath(self.hp.sliderImage4).is_displayed()

        try:
            wait = WebDriverWait(self.driver,
                                 10).until(EC.presence_of_element_located((By.ID, self.hp.sliderRightId))).click()
        finally:
            assert self.driver.find_element_by_xpath(self.hp.sliderImage1).is_displayed()

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
            self.driver.close(self.driver)

