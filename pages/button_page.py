from pages.base_page import BasePage
from pages.locators import button_page_loc as loc


class ButtonPage(BasePage):
    page_url = '/elements/button/simple'

    def click_button(self):
        self.click(loc.SUBMIT_BUTTON)
        # self.find(loc.SUBMIT_BUTTON).click()

    def check_result_text(self):
        assert self.find(loc.RESULT_TEXT).text == 'Submitted'

    def click_requirements(self):
        self.find(loc.REQ_HEADER).click()

    def check_requirement_displayed(self):
        assert self.find(loc.REQ_TEXT).is_displayed()
