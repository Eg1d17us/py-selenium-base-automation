from seleniumbase import BaseCase
from env_variables import saucedemo_login_url
from pages.locators_page import LoginPageLocators, HomePageLocators
import time


class LoginPage(BaseCase):
    def login_to_website(self, user_name, password,):
        self.open(saucedemo_login_url)
        self.maximize_window()
        self.send_keys(LoginPageLocators.user_name_input, user_name)
        self.send_keys(LoginPageLocators.pass_input, password)
        self.click(LoginPageLocators.login_btn)
        self.wait_for_element_visible(HomePageLocators.products_page_title)

    def log_out(self):
        self.click(HomePageLocators.hamburger_btn)
        self.wait_for_element_visible(HomePageLocators.logout_btn)
        self.click(HomePageLocators.logout_btn)
        self.wait_for_element_visible(LoginPageLocators.user_name_input)
        self.wait_for_element_visible(LoginPageLocators.pass_input)


