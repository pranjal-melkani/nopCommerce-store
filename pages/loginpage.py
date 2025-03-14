from base.basedriver import Basedriver

class Loginpage(Basedriver):
    REGISTER_BTN = "//*[@class='header-links']//*[text()='Login']"
    EMAIL_FIELD = "//*[@id='Email']"
    PASSWORD_FIELD = "//*[@id='Password']"
    REMEMBER_ME_CHECKBOX = "//*[@id='RememberMe']"

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
    
    