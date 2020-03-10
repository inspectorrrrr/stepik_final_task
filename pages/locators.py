from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")  #"#id_login-password"
    REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-email") #"#id_registration-password1", "#id_registration-password2"


class ProductPageLocators():
    ADD = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    ITEM = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ITEM_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner strong")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")