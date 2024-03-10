from seleniumbase import BaseCase
from pages.locators_page import HomePageLocators
from pages.generic_functions_page import Generic
from testData.texts_urls_btns import URLs


class HomePageAsserts(BaseCase):
    def verify_side_menu_contains_all_expected_items(self):
        expected_side_menu_elements = ['All Items', 'About', 'Logout', 'Reset App State']
        self.wait_for_element_visible(HomePageLocators.side_menu_items)
        side_menu_items = self.find_visible_elements(HomePageLocators.side_menu_items)
        actual_side_menu_elements = []
        for item in side_menu_items:
            actual_side_menu_elements.append(item.text)
        self.assertEqual(expected_side_menu_elements, actual_side_menu_elements)

    def verify_navigation_of_btn(self, button):
        if button == "About":
            self.click(HomePageLocators.hamburger_btn)
            Generic.verify_button_navigates_to_url(
                self,
                HomePageLocators.about_btn,
                URLs.about_btn_url,
                new_tab_is_opened=False)
        elif button == "Twitter":
            Generic.verify_button_navigates_to_url(
                self,
                HomePageLocators.twitter_btn,
                URLs.saucelabs_twitter_url,
                new_tab_is_opened=True)
        elif button == "Facebook":
            Generic.verify_button_navigates_to_url(
                self,
                HomePageLocators.facebook_btn,
                URLs.saucelabs_facebook_url,
                new_tab_is_opened=True)
        elif button == "Linkedin":
            Generic.verify_button_navigates_to_url(
                self,
                HomePageLocators.linkedin_btn,
                URLs.saucelabs_linkedin_url,
                new_tab_is_opened=True)

