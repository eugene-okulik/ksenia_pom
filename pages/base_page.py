import allure
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = 'https://www.qa-practice.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened for abstract page')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.driver.find_element(*locator).click()
