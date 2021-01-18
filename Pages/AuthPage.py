class AuthPage:
    loginPageFormid = 'emailOrPhoneInput'

    def __init__(self, driver):
        self.driver = driver

    def isEmailinputDisplayed(self):
        assert self.driver.find_element_by_id(self.loginPageFormid).is_displayed()
