import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_locators import *


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполнение поля Имя')
    def set_name(self, name):
        self.driver.find_element(*name_field).send_keys(name)

    @allure.step('Заполнение поля Фамилия')
    def set_surname(self, surname):
        self.driver.find_element(*surname_field).send_keys(surname)

    @allure.step('Заполнение поля Адрес')
    def set_address(self, address):
        self.driver.find_element(*address_field).send_keys(address)

    @allure.step('Заполнение(выбор) поля Станция метро')
    def click_station_field(self,station):
        self.driver.find_element(*station_field).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(list_of_stations))
        self.driver.find_element(*station_field).send_keys(station)
        self.driver.find_element(*station_name).click()

    @allure.step('Заполнение поля Телефон')
    def set_phone_number(self, phone_number):
        self.driver.find_element(*phone_number_field).send_keys(phone_number)

    @allure.step('Подтверждение кнопкой Далее')
    def click_button_next(self):
        self.driver.find_element(*button_next).click()

    @allure.step('Ожидание второй страницы формы заказа')
    def wait_for_load_order_form_2_header(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(order_form_2_header))

    @allure.step('Заполнение(выбор даты) поля Когда привезти самокат')
    def set_date(self, date):
        self.driver.find_element(*date_field).send_keys(date)
        self.driver.find_element(*calendar).click()

    @allure.step('Клик и выбор Срока аренды ')
    def click_rent_time_field(self):
        self.driver.find_element(*rent_time_field).click()
        self.driver.find_element(*rent_time_drop_down).click()

    @allure.step('Выбор цвета самоката')
    def choose_scooter_color(self):
        self.driver.find_element(*scooter_color).click()

    @allure.step('Заполнение поля Комментарий')
    def set_comments(self, comment):
        self.driver.find_element(*comments_field).send_keys(comment)

    @allure.step('Подтверждение кнопкой Заказать')
    def click_order_button(self):
        self.driver.find_element(*order_button).click()

    @allure.step('Подтверждение кнопкой Да')
    def click_confirm_yes_button(self):
        self.driver.find_element(*confirm_yes_button).click()

    @allure.step('Получение текста об успешном оформлении заказа')
    def get_order_created_confirm_text(self):
        return self.driver.find_element(*order_created_confirm_text).text
