from base.basedriver import Basedriver

class Navbar(Basedriver):
    REGISTER_BTN = "//*[@class='header-links']//*[text()='Register']"
    LOGIN_BTN = "//*[@class='header-links']//*[text()='Log in']"
    WISHLIST_BTN = "//*[@class='header-links']//*[text()='Wishlist']"
    SHOPPING_CART_BTN = "//*[@class='header-links']//*[text()='Shopping cart']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_register(self):
        self.click_on_element(self.REGISTER_BTN)

    def click_on_login(self):
        self.click_on_element(self.LOGIN_BTN)

    def click_on_wishlist(self):
        self.click_on_element(self.WISHLIST_BTN)
    
    def click_on_shopping_cart(self):
        self.click_on_element(self.SHOPPING_CART_BTN)


    
    

