from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "#product_gallery")
    ADD_TO_BASCKET_BUTTON =(By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > .price_color")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages :nth-child(1) > div > strong")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages :nth-child(3) > div > p > strong")