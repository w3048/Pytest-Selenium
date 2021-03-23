import pytest
from pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException

list_offer_codes = [str(i) for i in range(0, 10) if i != 7]
list_offer_codes.append('pytest.param("7", marks=pytest.mark.xfail)')
@pytest.mark.parametrize('offer_codes', list_offer_codes)
def test_guest_can_add_product_to_basket(browser, offer_codes):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_codes}'
    page = ProductPage(browser, link)
    page.open()
    page.is_a_product_page()
    page.add_product_to_basket()
    page.product_name_in_message_is_equal_product_name()
    page.product_price_is_equal_basket_cost()

