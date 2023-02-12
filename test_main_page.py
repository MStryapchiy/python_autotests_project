from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/"


class TestItems():
    def test_guest_can_go_to_login_page(self, browser):
        browser.get(link)
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()


# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


# class TestItems():
#     def test_search_for_add_to_bascket_button(self, browser):
#         browser.get(link)
#         browser.implicitly_wait(5)
#         assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
#         time.sleep(30)
