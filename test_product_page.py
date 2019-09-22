from .pages.product_page import ProductPage


def test_add_to_cart_btn_should_work(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_shopping_cart()
    page.should_be_after_adding_to_cart()


def test_guest_should_see_add_to_cart_btn(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_btn()
