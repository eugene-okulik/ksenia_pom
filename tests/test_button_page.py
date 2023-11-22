from time import sleep


def test_button(button_page):
    button_page.open_page()
    button_page.click_button()
    button_page.check_result_text()


def test_like_a_button(button_page):
    button_page.open_page()
    button_page.click_requirements()
    button_page.check_requirement_displayed()
