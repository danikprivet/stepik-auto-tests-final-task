from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_url(self):
        assert self.is_url_correct("http://selenium1py.pythonanywhere.com/ru/accounts/login/"), "Link isn't correct"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Element isn't present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Element isn't present"
