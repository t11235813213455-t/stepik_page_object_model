from Pages.main_page import MainPage
from Pages.base_page import BasePage
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
import time
from selenium.common.exceptions import NoSuchElementException
import pytest

@pytest.mark.skip
@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='known issue')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)    
    page.open()   
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_msg_about_adding_to_basket(page.get_book_name(), page.get_price())

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)    
    page.open()  
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)    
    page.open()  
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)    
    page.open()  
    page.add_to_basket()
    page.success_message_should_disappear()
