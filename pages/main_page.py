from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_locators import header_order_button, training_simulator, order_form_1_header, middle_order_button, \
    cookies


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(training_simulator))

    def click_header_order_button(self):
        self.driver.find_element(*header_order_button).click()

    def click_order_in_middle_page(self):
        self.driver.find_element(*middle_order_button).click()

    def wait_for_load_order_form_1_header(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(order_form_1_header))

    def click_cookies(self):
        self.driver.find_element(*cookies).click()