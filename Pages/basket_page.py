from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are present, while they should not be"

    def should_be_msg_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "There are no message about empty basket, while it should be"
