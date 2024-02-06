from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


class BookPageLocators:
    URL = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME_IN_MSG = (By.XPATH, '//div[@class = "alert alert-safe alert-noicon alert-success  fade in"][1]')
    CART_PRICE = (By.CLASS_NAME, 'basket-mini pull-right hidden-xs')


    

