from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

