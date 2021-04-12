import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    
    def is_a_product_page(self):
        # проверяем, что мы на странице товара
        self.should_be_product_image()
        self.should_be_add_to_bascket_button()

    def should_be_product_image(self):
        # проеверка наличия изображения товара
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IMAGE), "Product image isn't presrented"
        
    def should_be_add_to_bascket_button(self):
        # проверка наличия кнопки "Добавить в корзину"
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASCKET_BUTTON), "No button for adding to bascket"
    
    def get_product_name(self):
        # получение названия товара со страницы
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return name
        
    def product_name_in_message_is_equal_product_name(self):
        # проверка того, что после добавления товара в корзину его название в сообщении о добавлении
        # отображается верно
        message_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        assert message_product_name == self.get_product_name(), "Product name in message is not valid"
    
    def get_product_price(self):
        # получение цены товара со страницы
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return price
        
    def product_price_is_equal_basket_cost(self):
        # проверка того, что после добавления товара в корзину стоимость корзины в сообщении о добавлении
        # отображается верно
        message_product_price = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text
        assert message_product_price == self.get_product_price(), "Product price in basket is not valid"
    
    def add_product_to_basket(self):
        # проверка возможности добавления товара
        self.button_find_and_click(*ProductPageLocators.ADD_TO_BASCKET_BUTTON)
        if "promo=offer" in self.browser.current_url:
            self.solve_quiz_and_get_code()
        self.product_name_in_message_is_equal_product_name()
        self.product_price_is_equal_basket_cost() 
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
           
    def should_be_not_dissaperaed_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is dissapeared, but should not be"
       
    def solve_quiz_and_get_code(self):
        # задание от наших любимых учителей ))
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")