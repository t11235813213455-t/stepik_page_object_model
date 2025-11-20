from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")

class MainPageLocators():
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():    
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) div")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_NAME_IN_MSG = (By.CSS_SELECTOR, "#messages div:first-child div strong")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRICE_MSG = (By.CSS_SELECTOR, "#messages div:nth-child(3) p:nth-child(1)")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET = (By.CSS_SELECTOR, ".content p")
