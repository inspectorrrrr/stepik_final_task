from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_add_to_basket(self):
        self.to_do_add_to_basket()
        self.check_items()
        self.check_price()

    def to_do_add_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD)
        btn.click()

    def check_items(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM).text == self.browser.find_element(
            *ProductPageLocators.ITEM_BASKET).text, "book doesn't match"

    def check_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE).text == self.browser.find_element(
            *ProductPageLocators.PRICE_BASKET).text, "cost doesn't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(), \
            "Success message is presented, but should not be"

    def should_until_not_be_success_message(self):
        assert self.is_disappeared(), \
            "Success message is disappeared, but should be"
