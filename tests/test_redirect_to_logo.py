import time

import allure
import pytest
from selenium import webdriver

from pages.important_questions_page import ImportantQuestionsPage
from locators.important_questions_locators import *
from pages.main_page import MainPage


class TestOrderOnHeader:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_redirect_to_logo_scooter(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        main_page = MainPage(self.driver)
        # ожидаем загрузки главной страницы
        main_page.wait_for_load_home_page()
        # кликаем по кнопке Заказать
        main_page.click_header_order_button()
        # ожидаем появления заголовка первой страницы заказа
        main_page.wait_for_load_order_form_1_header()
        # кликаем по кнопке Самокат
        main_page.click_logo_Scooter()

        expected_url = 'https://qa-scooter.praktikum-services.ru/'
        assert expected_url == self.driver.current_url

    def test_redirect_to_logo_yandex(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        main_page = MainPage(self.driver)
        # ожидаем загрузки главной страницы
        main_page.wait_for_load_home_page()
        # кликаем по кнопке Самокат
        main_page.click_logo_Yandex()

        assert len(self.driver.window_handles) == 2

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
