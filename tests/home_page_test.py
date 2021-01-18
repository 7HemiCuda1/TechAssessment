import pytest
from time import sleep
from Pages.HomePage import HomePage


class Test_HomePage:
    baseURL = "https://www.podium.com/"

    # TODO: Create the setup and teardown.
    # pytest -s -v --html=Reports/report.html tests/
    # TODO: Add logging

    def test_chat_form_button(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        sleep(0.50)
        self.driver.find_element_by_xpath(self.hp.podiumChatbtn)
        self.driver.close()

    def test_platform_navigation(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        sleep(0.50)
        self.driver.find_element_by_xpath(self.hp.platformFooterLink).click()
        assert self.driver.current_url.contains("interaction-platform")
        self.driver.close()

    def test_slider_function(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        sleep(0.50)
        self.driver.find_element_by_id(self.hp.sliderLeftId).click()
        assert self.driver.find_element_by_xpath(self.hp.sliderImage4).is_displayed()
        self.driver.find_element_by_id(self.hp.sliderRightId).click()
        assert self.driver.find_element_by_xpath(self.hp.sliderImage1).is_displayed()
        self.driver.close()

    def test_login_page_navigation(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        sleep(0.50)
        self.driver.find_element_by_xpath(self.hp.loginHeader).click()

        self.driver.close()

