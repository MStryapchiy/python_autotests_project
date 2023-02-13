from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    price = page.get_product_price_on_product_page()
    name = page.get_product_name_on_product_page()
    print(price, name)
    page.click_to_backet_button()
    page.solve_quiz_and_get_code()
    price1 = page.get_product_price_in_message()
    pr_name = page.get_product_name_in_message()
    print(price1, pr_name)   
    page.should_be_product_price_in_messege()
    page.should_be_product_name_in_messege()

    # time.sleep(60)


# test_guest_can_add_product_to_basket()

