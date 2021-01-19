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
    @pytest.mark.links
    def test_chat_link(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.driver.maximize_window()
        self.hp.click_chat_btn()
        #TODO: Add assert for chat form.
        self.driver.close()

    @pytest.mark.links
    def test_for_platform_link(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.driver.maximize_window()
        self.hp.platformFooterLinkId()
        #TODO: Add assert for new page.
        self.driver.close()

    @pytest.mark.functionality
    def test_slider_function(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.driver.maximize_window()
        self.hp.click_slider_left()
        self.hp.correct_slider_image_displayed(4)
        self.hp.click_slider_right()
        self.hp.correct_slider_image_displayed(1)

        self.driver.close()
    @pytest.mark.functionality
    def test_login_page_navigation(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        #This may not be needed since i am starting the container in maximized mode. and setting the window size.
        self.driver.maximize_window()

        self.hp.click_login_btn()
        #Check that the Auth page loaded.
        self.lp = AuthPage(self.driver)
        self.lp.isEmailinputDisplayed()
        self.driver.close()

