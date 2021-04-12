from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators


class BasePage():
    ''' class methods are in an alphabetical order'''
    
    def __init__(self, browser, url, timeout=10):
        # инициализация объекта с параметрами self.browser и self.url
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def button_find_and_click(self, how, what):
        # просто ищем элемент и кликаем
        self.browser.find_element(how, what).click()
    
    def go_to_basket(self):
        basket_link_button = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link_button.click()
        
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
        
    def is_element_present(self, how, what):
        # проверка наличия элемента
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
        
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
        
    def open(self):
        # открываем нужную страницу в браузере
        self.browser.get(self.url)
        
    def get_element_from_page(self, how, what):
        # извлечение элемента со страницы
        self.browser.find_element(how, what)
        
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"