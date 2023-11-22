from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InputPage(BasePage):
    page_url = '/elements/input/simple'

    def enter_text_into_field_and_submit(self, text):
        text_input = self.driver.find_element(By.NAME, 'text_string')
        text_input.send_keys(text)
        text_input.submit()

    def check_result_text_is(self, text):
        assert self.driver.find_element(By.ID, 'result-text').text == text
