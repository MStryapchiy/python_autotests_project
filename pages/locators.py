from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR,"#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE_ON_PRODUCT_PAGE_LINK = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_ON_MESSAGE_LINK = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_NAME_ON_MESSAGE_LINK =(By.XPATH, "//div[@id='messages']/div[1]//strong")
    PRODUCT_NAME_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_main h1")