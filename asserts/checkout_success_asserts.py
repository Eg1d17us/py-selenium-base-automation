from seleniumbase import BaseCase
from pages.locators_page import CheckoutCompleteLocators

class CheckoutPageAsserts(BaseCase):
    def verify_order_complete_page_elements(self):
        self.wait_for_element_visible(CheckoutCompleteLocators.checkout_complete_page_title)
        self.wait_for_element_visible(CheckoutCompleteLocators.checkmark_img)
        self.wait_for_element_visible(CheckoutCompleteLocators.thanks_header)
        self.wait_for_element_visible(CheckoutCompleteLocators.description_text)
