from .Pages.main_page import MainPage
from .Pages.base_page import BasePage
from .Pages.login_page import LoginPage
from .Pages.product_page import ProductPage
from .Pages.basket_page import BasketPage
import time
from selenium.common.exceptions import NoSuchElementException
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='known issue')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)    
    page.open()   

    book_name = page.get_book_name()
    price = page.get_price()

    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_msg_about_adding_to_basket(book_name, price)

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link() 
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_the_basket()
    basket_page.should_be_msg_about_empty_basket()

def test_guest_cant_see_success_message(browser):    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)    
    page.open()  
    page.should_not_be_success_message()

@pytest.mark.xfail(reason='known issue')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)    
    page.open()  
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail(reason='known issue')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)    
    page.open()  
    page.add_to_basket()
    page.success_message_should_disappear()

@pytest.mark.user_tests
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.page = LoginPage(browser, link)
        self.page.open()
        email = str(time.time()) + "@fakemail.org"
        self.page.register_new_user(email, "test123test123")
        #self.page.login_user("test@ya.ru", "test123test123")

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open() 
        product_page.should_be_authorized_user()

        book_name = product_page.get_book_name()
        price = product_page.get_price()

        product_page.add_to_basket()
        product_page.should_be_msg_about_adding_to_basket(book_name, price)

        basket_page = BasketPage(browser, link) 
        basket_page.remove_items_from_basket()

    def test_user_cant_see_success_message(self, browser):    
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)    
        product_page.open()  
        product_page.should_be_authorized_user()
        product_page.should_not_be_success_message()
