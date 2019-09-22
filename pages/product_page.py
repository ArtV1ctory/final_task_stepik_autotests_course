from .base_page import BasePage
from .locators import ProductPageLocator
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
import math


class ProductPage(BasePage):
    def should_be_add_to_cart_btn(self):
        assert self.is_element_present(*ProductPageLocator.ADD_TO_CART_BTN), "Add to cart button is not presented"

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

    def add_to_shopping_cart(self):
        btn = self.browser.find_element(*ProductPageLocator.ADD_TO_CART_BTN)
        btn.click()
        self.solve_quiz_and_get_code()

    def should_be_after_adding_to_cart(self):
        self.should_be_correct_name_of_good_in_cart()
        self.should_be_correct_price_of_good_in_cart()

    def should_be_correct_price_of_good_in_cart(self):
        assert self.browser.find_element(*ProductPageLocator.PRICE_OF_GOOD_IN_ALERT).text \
               == self.browser.find_element(*ProductPageLocator.PRICE_OF_GOOD).text, \
               "The price of the product in the basket does not match the real price of the product!"

    def should_be_correct_name_of_good_in_cart(self):
        assert self.browser.find_element(*ProductPageLocator.NAME_OF_GOOD_IN_ALERT).text \
               == self.browser.find_element(*ProductPageLocator.NAME_OF_GOOD).text, \
               "The name of the product in the alert does not match the real name of the product!"
