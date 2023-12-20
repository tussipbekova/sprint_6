import allure
from selenium import webdriver

from pages.main_page import MainPage
from pages.order_page import OrderPage



class TestOrderOnHeader:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка кнопки «Заказать» вверху страницы')
    @allure.description('На главной странице проверяем что при клике на кнопку «Заказать» заполняется форма заказа и успешно создается')
    def test_order_on_header(self):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        main_page = MainPage(self.driver)
        #ожидаем загрузки главной страницы
        main_page.wait_for_load_home_page()
        #кликаем по кнопке Заказать
        main_page.click_header_order_button()
        #ожидаем появления заголовка первой страницы заказа
        main_page.wait_for_load_order_form_1_header()

        order_form_1_page = OrderPage(self.driver)
        #заполняем поле Имя
        order_form_1_page.set_name('Алина')
        # заполняем поле Фамилия
        order_form_1_page.set_surname('Аскарова')
        # заполняем поле адрес
        order_form_1_page.set_address('Усачева,8')
        #кликаем на поле станция
        order_form_1_page.click_station_field('Преображенская площадь')
        # заполняем поле телефон
        order_form_1_page.set_phone_number('87017778899')
        #кликаем по кнопке Далее
        order_form_1_page.click_button_next()
        #ожидаем появления заголовка второй страницы заказа
        order_form_1_page.wait_for_load_order_form_2_header()

        order_form_2_page = OrderPage(self.driver)
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