from selenium import webdriver
import pytest
from pages.button_page import ButtonPage
from pages.input_page import InputPage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def demo():
    return 'Demo word'


@pytest.fixture()
def button_page(driver):
    return ButtonPage(driver)


@pytest.fixture()
def input_page(driver):
    return InputPage(driver)
