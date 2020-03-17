from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login link is not found"  # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        assert self.browser.find_element(
            *LoginPageLocators.LOGIN_FORM), "login form is not found"  # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        assert self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM), "register form is not found"  # реализуйте проверку, что есть форма регистрации на странице
        assert True

    def register_new_user(self):  #, email, password):
        email = self.browser.find_element(*BasePageLocators.REGISTRATION_EMAIL)
        email.send_keys(str(time.time()) + "@fakemail.org")
        password1 = self.browser.find_element(*BasePageLocators.REGISTRATION_PASSWORD1)
        password1.send_keys(str(time))
        password2 = self.browser.find_element(*BasePageLocators.REGISTRATION_PASSWORD2)
        password2.send_keys(str(time))
        registertion_button = self.browser.find_element(*BasePageLocators.REGISTER_BUTTON)
        registertion_button.click()
