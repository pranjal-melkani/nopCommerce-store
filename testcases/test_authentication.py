from pages.loginpage import Loginpage

class TestAuthentication:
    def test_valid_login(self, driver):
        lp = Loginpage(driver)
        lp.enter_email('testemail@gmail.com')
        lp.enter_password('Password@123')
        