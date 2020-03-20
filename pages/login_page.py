from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login link is not found"
        assert True

    def should_be_login_form(self):
        assert self.browser.find_element(
            *LoginPageLocators.LOGIN_FORM), "login form is not found"
        assert True

    def should_be_register_form(self):
        assert self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM), "register form is not found"
        assert True

    def register_new_user(self, email, password):
        email_reg = self.browser.find_element(*BasePageLocators.REGISTRATION_EMAIL)
        email_reg.send_keys(email)
        password1 = self.browser.find_element(*BasePageLocators.REGISTRATION_PASSWORD1)
        password1.send_keys(password)
        password2 = self.browser.find_element(*BasePageLocators.REGISTRATION_PASSWORD2)
        password2.send_keys(password)
        reg_button = self.browser.find_element(*BasePageLocators.REGISTER_BUTTON)
        reg_button.click()
