from base.basedriver import Basedriver

class Registrationpage(Basedriver):
    GENDER_MALE_RADIO_BTN = "//*[@id='gender-male']"
    GENDER_FEMALE_RADIO_BTN = "//*[@id='gender-female']"
    FIRSTNAME_FIELD = "//*[@id='FirstName']"
    LASTNAME_FIELD = "//*[@id='LastName']"
    EMAIL_FIELD = "//*[@id='LastName']"
    COMPANY_NAME_FIELD = "//*[@id='Company']"
    NEWSLETTER_CHECKBOX = "//*[@id='Newsletter']"
    PASSWORD_FIELD = "//*[@id='Password']"
    CONFIRM_PASSWORD_FIELD = "//*[@id='ConfirmPassword']"
    REGISTER_BTN = "//*[@id='register-button']"

    def __init__(self, driver):
        super().__init__(driver)

    def select_gender(self, gender):
        if gender == 'Male':
            self.click_on_element(self.GENDER_MALE_RADIO_BTN)
        else:
            self.click_on_element(self.GENDER_FEMALE_RADIO_BTN)

    def enter_first_name(self, fname):
        self.send_keys(self.FIRSTNAME_FIELD, fname)
    
    def enter_last_name(self, lname):
        self.send_keys(self.LASTNAME_FIELD, lname)
    
    def enter_email(self, email_id):
        self.send_keys(self.EMAIL_FIELD, email_id)

    def enter_company_name(self, company):
        self.send_keys(self.COMPANY_NAME_FIELD, company)
    
    def newsletter_required(self, req = False):
        checkbox = self.wait_until_element_is_visible(self.NEWSLETTER_CHECKBOX)
        if req == True:
            if not checkbox.is_selected():
                checkbox.click()
        else:
            if checkbox.is_selected():
                checkbox.click()
    
    def enterpassword(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)
        self.send_keys(self.CONFIRM_PASSWORD_FIELD, password)
    
    def click_on_register(self):
        self.click_on_element(self.REGISTER_BTN) 
