from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def basket_empty(self):
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY), "basket is not empty"

    def basket_not_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_NOT_EMPTY), "product not in basket"
