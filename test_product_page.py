import time
import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException


default_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

@pytest.mark.logined_user
class TestUserAddToBasketFromProductPage():

    '''здесь собраны тесты для авторизованного пользователя'''
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, link = default_link):
        ''' фикстура открывает страницу регистрации, регит юзера и 
        проверяет его залогиненность '''
        self.page = BasePage(browser, link)
        self.page.open()
        self.page.go_to_login_page()
        self.page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()
        

    def test_user_cant_see_success_message(self, browser, link = default_link): 
        # Открываем страницу товара 
        self.page = ProductPage(browser, link)
        self.page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        self.page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link = default_link):
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.is_a_product_page()
        self.page.add_product_to_basket()
        self.page.product_name_in_message_is_equal_product_name()
        self.page.product_price_is_equal_basket_cost()
    
    
list_offer_codes = [str(i) for i in range(6, 9) if i != 7]
# Checking offer codes only from 6 to 8!
list_offer_codes.append('pytest.param("7", marks=pytest.mark.xfail)')
@pytest.mark.parametrize('offer_codes', list_offer_codes)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, offer_codes):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_codes}'
    page = ProductPage(browser, link)
    page.open()
    page.is_a_product_page()
    page.add_product_to_basket()
    page.product_name_in_message_is_equal_product_name()
    page.product_price_is_equal_basket_cost()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link = default_link): 
    # Открываем страницу товара 
    page = ProductPage(browser, link)
    page.open()
    # Добавляем товар в корзину 
    page.add_product_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()
 

def test_guest_cant_see_success_message(browser, link = default_link): 
    # Открываем страницу товара 
    page = ProductPage(browser, link)
    page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()
 
 
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link = default_link): 
    # Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
    # Добавляем товар в корзину
    page.add_product_to_basket()    
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_be_not_dissaperaed_success_message()
    
    
def test_guest_should_see_login_link_on_product_page(browser, link = default_link):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    

@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser, link= default_link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    newPage = LoginPage(browser, browser.current_url)
    newPage.should_be_login_page()
    
    
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link= default_link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_to_buy()
    basket_page.should_be_empty_message()