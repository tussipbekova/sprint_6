from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_form_1_locators import name_field, surname_field, address_field, station_field, phone_number_field, \
    button_next, list_of_stations, station_name, order_form_2_header


class OrderForm1Page:

    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(*name_field).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*surname_field).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*address_field).send_keys(address)

    def click_station_field(self,station):
        self.driver.find_element(*station_field).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(list_of_stations))
        self.driver.find_element(*station_field).send_keys(station)
        self.driver.find_element(*station_name).click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(*phone_number_field).send_keys(phone_number)

    def click_button_next(self):
        self.driver.find_element(*button_next).click()

    def wait_for_load_order_form_2_header(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(order_form_2_header))