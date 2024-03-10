from seleniumbase import BaseCase
from pages.locators_page import CartPageLocators


class CartPage(BaseCase):
    def checkout_and_finish_order(self):
        self.click(CartPageLocators.checkout_btn)
        self.fill(CartPageLocators.first_name_input, "Jonas")
        self.fill(CartPageLocators.last_name_input, "Jonauskas")
        self.fill(CartPageLocators.zip_postal_input, "12345")
        self.click(CartPageLocators.continue_btn)
        self.wait_for_element_visible(CartPageLocators.checkout_overview_page_title)
        self.click(CartPageLocators.finish_btn)
