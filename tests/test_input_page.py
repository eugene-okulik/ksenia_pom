import pytest
import allure


@allure.story('Input')
@pytest.mark.parametrize('text', ['sdfsdfsdf', 'fghfghfghfgh', 'erertert'])
def test_enter_text(input_page, text):
    input_page.open_page()
    input_page.enter_text_into_field_and_submit(text=text)
    input_page.check_result_text_is(text)
