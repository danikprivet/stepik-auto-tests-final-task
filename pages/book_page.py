from .base_page import BasePage
from .locators import BookPageLocators
from selenium.webdriver.common.by import By


class BookPage(BasePage):

    def add_to_the_cart(self):
        self.browser.find_element(*BookPageLocators.ADD_TO_BASKET_BUTTON).click()

    def name_of_added_book_should_be_right(self):
        element = self.is_element_present(By.XPATH,
                                          '//div[@class = "alert alert-safe alert-noicon alert-success  fade in"][1]')
        if element:
            text = self.browser.find_element(By.XPATH,
                                             '//div[@class = "alert alert-safe alert-noicon alert-success  fade in"][1]').text
            assert text.__contains__("The shellcoder's handbook"), "Text didn't match"

    def price_should_be_equal_to_the_cart(self):
        element = self.is_element_present(By.CLASS_NAME,
                                          'basket-mini pull-right hidden-xs')
        if element:
            text = self.browser.find_element(By.CLASS_NAME, 'basket-mini pull-right hidden-xs')
            assert text.__contains__("9,99"), "Text didn't match"
