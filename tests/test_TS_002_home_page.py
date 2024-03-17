from env_variables import *
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.locators_page import HomePageLocators
from asserts.home_page_asserts import HomePageAsserts
from pages.generic_functions_page import Generic
from testData.texts_urls_btns import HomePageTexts, Buttons, Sorting



class HomePageTests(HomePage):
    def setUp(self, **kwargs):
        super().setUp()
        LoginPage.login_to_website(self, valid_user_name, valid_pass)

    def test_TC_0003_side_menu_on_of_and_content_check(self):
        self.click(HomePageLocators.hamburger_btn)
        HomePageAsserts.verify_side_menu_contains_all_expected_items(self)
        HomePage.close_side_menu(self)

    def test_TC_0004_verify_about_btn_navigation_on_the_side_menu(self):
        self.click(HomePageLocators.hamburger_btn)
        HomePageAsserts.verify_navigation_of_btn(self, Buttons.about_btn)

    def test_TC_0005_verify_copyright_text_on_the_footer_menu(self):
        Generic.scroll_to_and_verify_text(self, HomePageLocators.copyright_txt, HomePageTexts.copyright_text)

    def test_TC_0006_verify_social_network_btn_navigation_on_the_footer_menu(self):
        HomePageAsserts.verify_navigation_of_btn(self, Buttons.twitter_btn)
        HomePageAsserts.verify_navigation_of_btn(self, Buttons.facebook_btn)
        HomePageAsserts.verify_navigation_of_btn(self, Buttons.linkedin_btn)

    def test_TC_0007_product_can_be_added_and_removed_to_cart_from_PL(self):
        index_of_the_prod = HomePage.select_one_random_product(self, True)
        Generic.scroll_to_and_verify_text(
            self,
            HomePageLocators.remove_from_cart_btn,
            HomePageTexts.remove_from_cart_btn)
        self.click(HomePageLocators.remove_from_cart_btn)
        Generic.scroll_to_and_verify_text(
            self,
            HomePageLocators.random_add_to_cart_btn.format(index_of_the_prod),
            HomePageTexts.add_to_cart_btn)

    def test_TC_0008_random_number_of_products_added_to_cart_displays_the_number_label_on_the_cart_icon(self):
        number_of_products_selected = HomePage.select_random_number_of_products(self, True)
        Generic.scroll_to_and_verify_text(self, HomePageLocators.cart_badge, number_of_products_selected)
        print(number_of_products_selected)

    def test_TC_0009_products_can_be_sorted_by_name_and_by_price(self):
        HomePage.sort_by_name_and_verify_sorting(self, Sorting.NameDescending)
        HomePage.sort_by_name_and_verify_sorting(self, Sorting.NameAscending)
        HomePage.sort_by_price_and_verify_sorting(self, Sorting.PriceAscending)
        HomePage.sort_by_price_and_verify_sorting(self, Sorting.PriceDescending)
