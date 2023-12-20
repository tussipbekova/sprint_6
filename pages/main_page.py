import allure

from locators.main_locators import *
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    @allure.step('Ожидание загрузки главной страницы')
    def wait_for_load_home_page(self):
        super().wait_for_visibility(training_simulator)

    @allure.step('Скролл до раздела Вопросы о важном ')
    def scrolldown_to_question_field(self, question_locator):
        element = self.driver.find_element(*question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание до кликабельности вопроса')
    def wait_for_clickable(self, question_locator):
        super().wait_for_clickable(question_locator)

    @allure.step('Клик вопроса')
    def click_question(self, question_locator):
        super().click(question_locator)

    @allure.step('Ожидание до появления ответа')
    def wait_for_load_answer(self, answer_locator):
        super().wait_for_visibility(answer_locator)

    @allure.step('Получение ответа')
    def get_answer_field(self, answer_locator):
        return super().get_text(answer_locator)

    @allure.step('Ожидаем загрузки главной страницы')
    def wait_for_load_home_page(self):
        super().wait_for_visibility(training_simulator)

    @allure.step('Кликаем по кнопке Заказать вверху страницы')
    def click_header_order_button(self):
        super().click(header_order_button)

    @allure.step('Кликаем по кнопке Заказать внизу страницы')
    def click_order_in_middle_page(self):
        super().click(middle_order_button)

    @allure.step('Ожидаем загрузки первой страницы формы заказа')
    def wait_for_load_order_form_1_header(self):
        super().wait_for_visibility(order_form_1_header)

    @allure.step('Принимаем куки')
    def click_cookies(self):
        super().click(cookies)

    @allure.step('Кликаем по лого Самокат')
    def click_logo_Scooter(self):
        super().click(logo_scooter)

    @allure.step('Кликаем по лого Яндекс')
    def click_logo_Yandex(self):
        super().click(logo_Yandex)
