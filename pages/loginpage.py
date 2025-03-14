from base.basedriver import Basedriver

class Loginpage(Basedriver):
    EMAIL_FIELD = "//*[@id='Email']"
    PASSWORD_FIELD = "//*[@id='Password']"
    REMEMBER_ME_CHECKBOX = "//*[@id='RememberMe']"
    FORGOT_PASSWORD_BTN = "//*[contains(text(), 'Forgot password')]"
    LOGIN_BTN = "//button[text() = 'Log in']"

    def __init__(self):
        super().__init__(driver)

    def enter_email(self, email_id):
        self.send_keys(self.EMAIL_FIELD, email_id)
    
    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)

    def remember_me(self, select = True):
        checkbox = self.wait_until_element_is_visible(self.REMEMBER_ME_CHECKBOX)
        if select == True:
            if not checkbox.is_selected():
                self.click_on_element(self.REMEMBER_ME_CHECKBOX)
        else:
            if checkbox.is_selected():
                self.click_on_element(self.REMEMBER_ME_CHECKBOX)
    
    def click_on_forgot_password(self):
        self.click_on_element(self.FORGOT_PASSWORD_BTN)
    
    def click_on_login_btn(self):
        self.click_on_element(self.LOGIN_BTN)

    

    
    