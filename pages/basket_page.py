from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_message(self):
        # проверяем наличие сообщения, что в корзине пусто
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Basket is not empty"
        
    def should_not_be_items_to_buy(self):
        # проверяем, что в корзине пусто
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), "In basket are items, but must be empty" 
