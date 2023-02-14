from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_LINK), \
        "Add to basket button is not existed"
    
    def click_to_backet_button(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        add_to_basket_button.click()
    
    def get_product_price_on_product_page(self):
        pr_price = self.get_element_value(*ProductPageLocators.PRODUCT_PRICE_ON_PRODUCT_PAGE_LINK)
        return pr_price
    
    def get_product_price_in_message(self):
        price = self.get_element_value(*ProductPageLocators.PRODUCT_PRICE_ON_MESSAGE_LINK)
        return price

    def should_be_product_price_in_messege(self):
        assert self.get_product_price_on_product_page() == self.get_product_price_in_message(), \
        "There is no product price in message" 

    def get_product_name_on_product_page(self):
        pr_name = self.get_element_value(*ProductPageLocators.PRODUCT_NAME_ON_PRODUCT_PAGE)
        return pr_name
    
    def get_product_name_in_message(self):
        name = self.get_element_value(*ProductPageLocators.PRODUCT_NAME_ON_MESSAGE_LINK)
        return name
    
    def should_be_product_name_in_messege(self):
        assert self.get_product_name_on_product_page() == self.get_product_name_in_message(), \
        "There is no product name in message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ON_PRODUCT_PAGE), \
        "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_ON_PRODUCT_PAGE), \
        "Not disappeared, but should be"
