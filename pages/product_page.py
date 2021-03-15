from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    def is_a_product_page(self):
        self.should_be_product_image()
        self.should_be_add_to_bascket_button()

    def should_be_product_image(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IMAGE), "Product image isn't presrented"
        
    def should_be_add_to_bascket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASCKET_BUTTON), "No button for adding to bascket"
        
    def add_to_bascket(self):
        self.button_find_and_click(*ProductPageLocators.ADD_TO_BASCKET_BUTTON)
    
    def solve_quiz_and_get_code(self):
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