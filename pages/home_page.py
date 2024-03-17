from seleniumbase import BaseCase
from pages.locators_page import HomePageLocators, CartPageLocators
import random


def generate_random_num(from_num, to_num):
    return random.randint(from_num, to_num)

def get_normalized_prices_array(self):
    default_product_prices_list = []
    normalized_default_product_prices_list = []
    product_prices = self.find_visible_elements(HomePageLocators.product_prices)
    for product in product_prices:
        default_product_prices_list.append(product.text)
    for product in default_product_prices_list:
        element_without_dollar = product.replace('$', '')
        normalized_default_product_prices_list.append(float(element_without_dollar))
    return normalized_default_product_prices_list


class HomePage(BaseCase):
    def select_one_random_product(self, return_index: bool = False):
        number_of_products = len(self.find_visible_elements(HomePageLocators.product_tile))
        random_num = generate_random_num(1, number_of_products)
        self.click(HomePageLocators.random_add_to_cart_btn.format(random_num))
        if return_index:
            return random_num

    def select_random_number_of_products(self, return_number_of_products_selected: bool = False):
        number_of_products = len(self.find_visible_elements(HomePageLocators.product_tile))
        random_num = generate_random_num(1, number_of_products)
        for element in range(1, random_num + 1):
            self.click(HomePageLocators.add_to_cart_btn)
        if return_number_of_products_selected:
            return random_num

    def proceed_to_cart(self):
        self.click(HomePageLocators.cart_btn)
        self.wait_for_element_visible(CartPageLocators.cart_page_title)

    def close_side_menu(self):
        self.click(HomePageLocators.close_side_menu_btn)
        self.wait_for_element_not_visible(HomePageLocators.close_side_menu_btn)

    def sort_by_name_and_verify_sorting(self, sorting_type):
        default_product_list = []
        actual_prod_sorted = []
        products = self.find_visible_elements(HomePageLocators.product_names)
        for product in products:
            default_product_list.append(product.text)
        if sorting_type == "Name (Z to A)":
            default_product_list.reverse()
        if sorting_type == "Name (A to Z)":
            default_product_list.sort()
        expected_prod_sorted = default_product_list
        self.select_option_by_text(HomePageLocators.product_sort_btn, sorting_type)
        products_sorted = self.find_visible_elements(HomePageLocators.product_names)
        for sorted_product in products_sorted:
            actual_prod_sorted.append(sorted_product.text)
        self.assertEqual(expected_prod_sorted, actual_prod_sorted)

    def sort_by_price_and_verify_sorting(self, sorting_type):
        default_prices_list = get_normalized_prices_array(self)
        if sorting_type == "Price (low to high)":
            default_prices_list.sort()
        if sorting_type == "Price (high to low)":
            default_prices_list.reverse()
        expected_prices_sorted = default_prices_list
        self.select_option_by_text(HomePageLocators.product_sort_btn, sorting_type)
        actual_prices_sorted = get_normalized_prices_array(self)
        self.assertEqual(expected_prices_sorted, actual_prices_sorted)


