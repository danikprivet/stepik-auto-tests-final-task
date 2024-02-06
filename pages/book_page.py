from .base_page import BasePage
from .locators import BookPageLocators


class BookPage(BasePage):

    def add_to_the_cart(self):
        self.browser.find_element(*BookPageLocators.ADD_TO_BASKET_BUTTON).click()

    def name_of_added_book_should_be_right(self):
        book_name_in_msg = self.is_element_present(*BookPageLocators.BOOK_NAME_IN_MSG)
        if book_name_in_msg:
            book_name_text_in_msg = self.browser.find_element(*BookPageLocators.BOOK_NAME_IN_MSG).text
            assert book_name_text_in_msg.__contains__("The shellcoder's handbook"), "Text didn't match"

    def price_should_be_equal_to_the_cart(self):
        cart_price = self.is_element_present(*BookPageLocators.CART_PRICE)
        if cart_price:
            assert cart_price.__contains__("9,99"), "Text didn't match"
