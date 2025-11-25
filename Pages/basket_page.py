from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasketPage(BasePage):

    def remove_items_from_basket(self):
        self.go_to_basket()
        number_of_books = self.browser.find_element(*BasketPageLocators.NUMBER_OF_BOOKS_IN_BASKET)
        number_of_books.clear()
        number_of_books.send_keys("0")
        update_button = self.browser.find_element(*BasketPageLocators.UPDATE_BUTTON)
        update_button.click()

        #waiting until books are removed from the basket
        timeout = 5
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(BasketPageLocators.EMPTY_BASKET))

    def should_not_be_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are present, while they should not be"

    def should_be_msg_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "There are no message about empty basket, while it should be"
