from pages.book_page import BookPage
from pages.locators import BookPageLocators


def test_guest_can_add_product_to_basket(browser):
    page = BookPage(browser, BookPageLocators.URL)
    page.open()
    page.add_to_the_cart()
    page.solve_quiz_and_get_code()
    page.name_of_added_book_should_be_right()
    page.price_should_be_equal_to_the_cart()
