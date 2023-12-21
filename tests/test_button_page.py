from time import sleep
import allure


@allure.title('Button works')
@allure.feature('Button')
@allure.story('Button')
def test_button(button_page):
    button_page.open_page()
    with allure.step('CLick button'):
        button_page.click_button()
    with allure.step('Check result text'):
        button_page.check_result_text()


@allure.feature('Button')
@allure.story('like a button')
def test_like_a_button(button_page):
    button_page.open_page()
    button_page.click_requirements()
    button_page.check_requirement_displayed()
