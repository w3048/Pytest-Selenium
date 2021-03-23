from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверяем, что в адресе страницы упоминается login
        assert 'login' in self.browser.current_url, "Login URL isn't valid"

    def should_be_login_form(self):
        # проверяем есть ли форма входа
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form isn't presented"

    def should_be_register_form(self):
        # проверяем есть ли форма регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form isn't presented"