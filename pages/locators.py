from selenium.webdriver.common.by import By

    
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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default")
    
class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, ".col-sm-6.h3")