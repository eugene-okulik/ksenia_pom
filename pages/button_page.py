from pages.base_page import BasePage
from pages.locators import button_page_loc as loc
import allure
from allure_commons.types import AttachmentType


class ButtonPage(BasePage):
    page_url = '/elements/button/simple'
    PAGE_NAME = 'Buttons'

    @allure.step(f'Open page {PAGE_NAME}: {page_url}')
    def open_page(self):
        super().open_page()

    def click_button(self):
        self.click(loc.SUBMIT_BUTTON)
        allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
        # self.find(loc.SUBMIT_BUTTON).click()

    def check_result_text(self):
        assert self.find(loc.RESULT_TEXT).text == 'Submitted'

    @allure.step('Expand requirements')
    def click_requirements(self):
        self.find(loc.REQ_HEADER).click()

    @allure.step('Check that requirements displayed')
    def check_requirement_displayed(self):
        assert self.find(loc.REQ_TEXT).is_displayed()
