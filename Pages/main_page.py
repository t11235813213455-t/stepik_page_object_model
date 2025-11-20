from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
       