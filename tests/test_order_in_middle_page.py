import allure
from selenium import webdriver

from data.data import ADDRESS, SURNAME, NAME, STATION, PHONE_NUMBER, DATE, COMMENTS
from pages.main_page import MainPage
from pages.order_page import OrderPage



class TestOrderInMiddlePage:

    @allure.title('Проверка кнопки «Заказать» внизу страницы')
    @allure.description('На главной странице проверяем что при клике на  кнопку «Заказать» заполняется форма и создается заказ')
    def test_order_in_middle_page(self,driver):


        main_page = MainPage(driver)
        #ожидаем загрузки главной страницы
        main_page.wait_for_load_home_page()
        # принимаем Куки
        main_page.click_cookies()
        #кликаем по кнопке Заказать
        main_page.click_order_in_middle_page()
        #ожидаем появления заголовка первой страницы заказа
        main_page.wait_for_load_order_form_1_header()

        order_form_1_page = OrderPage(driver)
        #заполняем поле Имя
        order_form_1_page.set_name(NAME)
        # заполняем поле Фамилия
        order_form_1_page.set_surname(SURNAME)
        # заполняем поле адрес
        order_form_1_page.set_address(ADDRESS)
        #кликаем на поле станция
        order_form_1_page.click_station_field(STATION)
        # заполняем поле телефон
        order_form_1_page.set_phone_number(PHONE_NUMBER)
        #кликаем по кнопке Далее
        order_form_1_page.click_button_next()
        #ожидаем появления заголовка второй страницы заказа
        order_form_1_page.wait_for_load_order_form_2_header()

        order_form_2_page = OrderPage(driver)
        # заполняем поле Когда привезти самокат
        order_form_2_page.set_date(DATE)
        # заполняем поле Срок аренды
        order_form_2_page.click_rent_time_field()
        # выбираем цвет самоката
        order_form_2_page.choose_scooter_color()
        #заполняем поле Комментарий
        order_form_2_page.set_comments(COMMENTS)
        # кликаем по кнопке Заказать
        order_form_2_page.click_order_button()
        # подтверждаем заказ кнопкой Да
        order_form_2_page.click_confirm_yes_button()
        # вытаскиваем текст об оформлении заказа
        actual_text = order_form_2_page.get_order_created_confirm_text()

        assert actual_text.startswith('Заказ оформлен')