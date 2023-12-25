import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_locators import *
from pages.base_page import BasePage


class OrderPage(BasePage):


    @allure.step('Заполнение поля Имя')
    def set_name(self, name):
        self.send_keys(name_field, name)

    @allure.step('Заполнение поля Фамилия')
    def set_surname(self, surname):
        self.send_keys(surname_field,surname)

    @allure.step('Заполнение поля Адрес')
    def set_address(self, address):
        self.send_keys(address_field,address)

    @allure.step('Заполнение(выбор) поля Станция метро')
    def click_station_field(self,station):
        self.click(station_field)
        self.wait_for_visibility(list_of_stations)
        self.send_keys(station_field,station)
        self.click(station_name)

    @allure.step('Заполнение поля Телефон')
    def set_phone_number(self, phone_number):
        self.send_keys(phone_number_field,phone_number)

    @allure.step('Подтверждение кнопкой Далее')
    def click_button_next(self):
        self.click(button_next)

    @allure.step('Ожидание второй страницы формы заказа')
    def wait_for_load_order_form_2_header(self):
        self.wait_for_visibility(order_form_2_header)

    @allure.step('Заполнение(выбор даты) поля Когда привезти самокат')
    def set_date(self, date):
        self.send_keys(date_field,date)
        self.click(calendar)

    @allure.step('Клик и выбор Срока аренды ')
    def click_rent_time_field(self):
        self.click(rent_time_field)
        self.click(rent_time_drop_down)

    @allure.step('Выбор цвета самоката')
    def choose_scooter_color(self):
        self.click(scooter_color)

    @allure.step('Заполнение поля Комментарий')
    def set_comments(self, comment):
        self.send_keys(comments_field,comment)

    @allure.step('Подтверждение кнопкой Заказать')
    def click_order_button(self):
        self.click(order_button)

    @allure.step('Подтверждение кнопкой Да')
    def click_confirm_yes_button(self):
        self.click(confirm_yes_button)

    @allure.step('Получение текста об успешном оформлении заказа')
    def get_order_created_confirm_text(self):
        return self.get_text(order_created_confirm_text)
