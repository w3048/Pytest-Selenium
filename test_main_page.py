from pages.main_page import MainPage


def test_guest_should_see_login_loink(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) 
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # inicialization Page Object
    page.open() # method from base_page
    page.go_to_login_page() # method from main_page.py
    
