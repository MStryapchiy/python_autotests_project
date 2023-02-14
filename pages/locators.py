from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE_LINK = (
        By.XPATH, "//header['container-fluid']/div/div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM_LINK = (By.ID, "id_registration-email")
    PASSWORD_FORM_LINK = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD_FORM_LINK = (By.ID, "id_registration-password2")
    REGISTER_BUTTON_LINK = (By.CSS_SELECTOR, "button[value='Register']")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCTS_IN_BASKET_CLASS = (By.CSS_SELECTOR, "basket-items")


class ProductPageLocators():
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE_ON_PRODUCT_PAGE_LINK = (
        By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_ON_MESSAGE_LINK = (
        By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_NAME_ON_MESSAGE_LINK = (
        By.XPATH, "//div[@id='messages']/div[1]//strong")
    PRODUCT_NAME_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE_ON_PRODUCT_PAGE = (
        By.XPATH, "//div[@id='messages']/div[1]//strong")
