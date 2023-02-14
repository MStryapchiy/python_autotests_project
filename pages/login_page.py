from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "This is not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fomakinev.ru"
        password = "aaa333sss"
        email_link = self.browser.find_element(*LoginPageLocators.EMAIL_FORM_LINK)
        password_link = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM_LINK)
        cpassword_link = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FORM_LINK)
        email_link.send_keys(email)
        password_link.send_keys(password)
        cpassword_link.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_LINK).click()
    
        

