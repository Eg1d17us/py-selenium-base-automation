from env_variables import *
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from asserts.checkout_success_asserts import CheckoutPageAsserts


class SmokeTests(LoginPage):
    def setUp(self, **kwargs):
        super().setUp()
        LoginPage.login_to_website(self, valid_user_name, valid_pass)

    def test_TC_0001_login_and_logout(self):
        LoginPage.log_out(self)

    def test_TC_0002_buy_one_random_product(self):
        HomePage.select_one_random_product(self)
        HomePage.proceed_to_cart(self)
        CartPage.checkout_and_finish_order(self)
        CheckoutPageAsserts.verify_order_complete_page_elements(self)
