from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"       

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click() 
       
    def get_book_name(self):
        return self.get_text_of_element(*ProductPageLocators.BOOK_NAME)

    def get_price(self):   
        return self.get_text_of_element(*ProductPageLocators.PRICE)

    def should_be_msg_about_adding_to_basket(self, book_name, price):
        msg = self.get_text_of_element(*ProductPageLocators.SUCCESS_MESSAGE)
        book_name_in_msg = self.get_text_of_element(*ProductPageLocators.BOOK_NAME_IN_MSG)
        price_msg = self.get_text_of_element(*ProductPageLocators.PRICE_MSG)
        assert "has been added to your basket." in msg, f"Message 'has been added to your basket' is absent. Message: {msg}" 
        assert book_name == book_name_in_msg, f"Book title in the message is incorrect. \
            Book title: {book_name}, book name in the message: {book_name_in_msg}"
        assert price in price_msg, f"Book price in the message is incorrect. Book price: {price}, message: {price_msg}"
