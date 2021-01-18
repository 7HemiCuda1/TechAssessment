from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HomePage:
    watchDemoBox = '//*[@id="theme-white"]/nav/div/div[2]/ul/li[2]/a'
    loginHeader = '//*[@id="theme-white"]/nav/div/div[2]/ul/li[1]/a'
    podiumChatbtn = '//*[@id="main"]/div/div/div/div/button'
    platformFooterLink = '//*[@id="colophon"]/section/div[1]/div[2]/div[1]/a[1]'
    podiumChatText = '//*[@id="ComposeMessage"]/div[1]/div/div'
    podiumChatName = '//*[@id="Name"]'
    podiumChatMobileNumber = '//*[@id="ComposeMessage"]/form/div[3]/div[2]'
    podiumChatMessage = '//*[@id="ComposeMessage"]/form/div[3]/div[2]/div[4]'
    sliderRight = '//*[@id="right-arrow-video"]/svg'
    sliderLeft = '//*[@id="left-arrow-video"]/svg'
    sliderLeftId = 'left-arrow-video'
    sliderRightId = 'right-arrow-video'
    sliderImage1 = '//*[@id="video-1-img"]'
    sliderImage2 = '//*[@id="video-2-img"]'
    sliderImage3 = '//*[@id="video-3-img"]'
    sliderImage4 = '//*[@id="video-4-img"]'


    # podiumChatSend = "//*[@id="ComposeMessage"]/form/div[2]/div[2]/button/div"

    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element_by_xpath(self.podiumChatName).clear()
        self.driver.find_element_by_xpath(self.podiumChatName).send_keys(name)

    def set_phone(self, phone):
        self.driver.find_element_by_xpath(self.podiumChatMobileNumber).clear()
        self.driver.find_element_by_xpath(self.podiumChatMobileNumber).send_keys(phone)

    def set_message(self, message):
        self.driver.find_element_by_xpath(self.podiumChatMessage).clear()
        self.driver.find_element_by_xpath(self.podiumChatMessage).send_keys(message)

    def click_watch_demo(self):
        self.driver.find_element_by_xpath(self.watchDemoBox).click()

    def click_login_btn(self):
        wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.loginHeader ))).click()

    def click_platform_btn(self):
        self.driver.find_element_by_xpath(self.platformFooterLink).click()

    def click_podium_chat_btn(self):
        self.driver.find_element_by_xpath(self.podiumChatbtn).click()

    def click_slider_right(self):
        self.driver.find_element_by_xpath(self.sliderRight).click()

    def click_slider_left(self):
        self.driver.find_element_by_xpath(self.sliderLeft).click()

    def slider_image(self, num) -> bool:
        try:
            self.driver.find_element_by_xpath(self.slider_image + num)
            return True
        except:
            return False

    def click_chat_btn(self):
        self.driver.find_element_by_xpath(self.podiumChatbtn)
