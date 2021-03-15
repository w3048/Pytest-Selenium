from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "#product_gallery")
    ADD_TO_BASCKET_BUTTON =(By.CSS_SELECTOR, "#add_to_basket_form")
    