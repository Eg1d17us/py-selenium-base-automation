from seleniumbase import BaseCase
from pages.locators_page import HomePageLocators, CartPageLocators
import random


class HomePage(BaseCase):
    def select_one_random_product(self, return_index: bool = False):
        number_of_products = len(self.find_visible_elements(HomePageLocators.product_tile))
        random_num = HomePage.generate_random_num(self, 1, number_of_products)
        self.click(HomePageLocators.random_add_to_cart_btn.format(random_num))
        if return_index:
            return random_num
        else:
            pass

    def generate_random_num(self, from_num, to_num):
        return random.randint(from_num, to_num)

    def proceed_to_cart(self):
        self.click(HomePageLocators.cart_btn)
        self.wait_for_element_visible(CartPageLocators.cart_page_title)

    def close_side_menu(self):
        self.click(HomePageLocators.close_side_menu_btn)
        self.wait_for_element_not_visible(HomePageLocators.close_side_menu_btn)
