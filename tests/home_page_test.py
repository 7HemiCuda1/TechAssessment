import pytest
from time import sleep
from Pages.HomePage import HomePage
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
        self.driver.find_element_by_xpath(self.hp.podiumChatbtn)
        self.driver.close()

    def for_platform(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.driver.maximize_window()
        assert self.driver.find_element_by_xpath(self.hp.platformFooterLink)
        self.driver.close()

    def slider_function(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.driver.maximize_window()
        self.driver.find_element_by_id(self.hp.sliderLeftId)
        assert self.driver.find_element_by_xpath(self.hp.sliderImage4).is_displayed()
        self.driver.find_element_by_id(self.hp.sliderRightId).click()
        assert self.driver.find_element_by_xpath(self.hp.sliderImage1).is_displayed()
        self.driver.close()

    def test_login_page_navigation(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.driver.maximize_window()
        try:
            wait = WebDriverWait(self.driver,
                                 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                    self.hp.loginHeader ))).click()

        finally:
            #result = self.driver.find_element_by_xpath(self.hp.loginHeader)
            assert self.driver.find_element_by_xpath(self.hp.loginPageFormid).is_displayed()
            self.driver.close()

