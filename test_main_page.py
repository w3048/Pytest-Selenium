import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


default_link = 'http://selenium1py.pythonanywhere.com/'

@pytest.mark.login_guest
class TestLoginFromMainPage():

    '''здесь тесты наличия ссылки на форму логина и перехода на нее'''
    
    def test_guest_should_see_login_link(self, browser, link=default_link):
        ''' тест падает с этой ссылкой, с дефолтной все норм- селектор битый на странице
        http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer
        с дефолтной все норм- селектор битый на странице'''
        page = MainPage(browser, link) 
        page.open()
        page.should_be_login_link()

        
    def test_guest_can_go_to_login_page(self, browser, link=default_link):
        ''' тест падает с этой ссылкой, 
        http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer
        с дефолтной все норм- селектор битый на странице'''
        page = MainPage(browser, link) # inicialization Page Object
        page.open() # method from base_page
        page.go_to_login_page()   
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
 
 
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link=default_link):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_to_buy()
    basket_page.should_be_empty_message()
