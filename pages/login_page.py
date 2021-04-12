from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators
import time # в начале файла

email = str(time.time()) + "@fakemail.org"
password = str(time.time())

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
        
    def register_new_user(self, email, password):
        # регистрация нового пользователя
        registration_email_form = self.browser.find_element(By.CSS_SELECTOR, '#id_registration-email')
        registration_email_form.send_keys(email)
        registration_password_form = self.browser.find_element(By.CSS_SELECTOR, '#id_registration-password1')
        registration_password_form.send_keys(password)
        registration_confirm_password_form = self.browser.find_element(By.CSS_SELECTOR, '#id_registration-password2')
        registration_confirm_password_form.send_keys(password)
        register_button = self.browser.find_element(By.CSS_SELECTOR, "#register_form > button")
        register_button.click()