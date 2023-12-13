import time

import allure
import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.order_form_1_page import OrderForm1Page
from pages.order_form_2_page import OrderForm2Page


class TestOrderInMiddlePage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_order_in_middle_page(self):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        main_page = MainPage(self.driver)
        #ожидаем загрузки главной страницы
        main_page.wait_for_load_home_page()
        # принимаем Куки
        main_page.click_cookies()
        #кликаем по кнопке Заказать
        main_page.click_order_in_middle_page()
        #ожидаем появления заголовка первой страницы заказа
        main_page.wait_for_load_order_form_1_header()

        order_form_1_page = OrderForm1Page(self.driver)
        #заполняем поле Имя
        order_form_1_page.set_name('Маргарита')
        # заполняем поле Фамилия
        order_form_1_page.set_surname('Краснова')
        # заполняем поле адрес
        order_form_1_page.set_address('Ленина,99')
        #кликаем на поле станция
        order_form_1_page.click_station_field('Преображенская площадь')
        # заполняем поле телефон
        order_form_1_page.set_phone_number('87017778899')
        #кликаем по кнопке Далее
        order_form_1_page.click_button_next()
        #ожидаем появления заголовка второй страницы заказа
        order_form_1_page.wait_for_load_order_form_2_header()

        order_form_2_page = OrderForm2Page(self.driver)
        # заполняем поле Когда привезти самокат
        order_form_2_page.set_date('14.12.2023')
        # заполняем поле Срок аренды
        order_form_2_page.click_rent_time_field()
        # выбираем цвет самоката
        order_form_2_page.choose_scooter_color()
        #заполняем поле Комментарий
        order_form_2_page.set_comments('Просьба позвонить заранее')
        # кликаем по кнопке Заказать
        order_form_2_page.click_order_button()
        # подтверждаем заказ кнопкой Да
        order_form_2_page.click_confirm_yes_button()
        # вытаскиваем текст об оформлении заказа
        actual_text = order_form_2_page.get_order_created_confirm_text()

        assert actual_text.startswith('Заказ оформлен')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()