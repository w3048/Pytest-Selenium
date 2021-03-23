from pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.is_a_product_page()
    page.test_guest_can_add_product_to_basket()

     