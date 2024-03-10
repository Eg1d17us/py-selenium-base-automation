from seleniumbase import BaseCase


class Generic(BaseCase):
    def scroll_to_and_verify_text(self, locator, text_to_assert):
        self.scroll_into_view(locator)
        self.assert_text(text_to_assert, locator)

    def verify_button_navigates_to_url(self, locator, url_to_assert, new_tab_is_opened:bool):
        if new_tab_is_opened == False:
            self.click(locator)
            self.assert_url(url_to_assert)
        elif new_tab_is_opened == True:
            self.switch_to_default_tab()
            self.click(locator)
            self.switch_to_newest_tab()
            self.assert_url(url_to_assert)

