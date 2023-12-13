import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_locators import header_order_button, training_simulator, order_form_1_header, middle_order_button, \
    cookies, logo_scooter, logo_Yandex


class MainPage:

    def __init__(self, driver):
        self.driver = driver
    @allure.step('Ожидаем загрузки главной страницы')
    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(training_simulator))

    @allure.step('Кликаем по кнопке Заказать вверху страницы')
    def click_header_order_button(self):
        self.driver.find_element(*header_order_button).click()

    @allure.step('Кликаем по кнопке Заказать внизу страницы')
    def click_order_in_middle_page(self):
        self.driver.find_element(*middle_order_button).click()

    @allure.step('Ожидаем загрузки первой страницы формы заказа')
    def wait_for_load_order_form_1_header(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(order_form_1_header))

    @allure.step('Принимаем куки')
    def click_cookies(self):
        self.driver.find_element(*cookies).click()

    @allure.step('Кликаем по лого Самокат')
    def click_logo_Scooter(self):
        self.driver.find_element(*logo_scooter).click()

    @allure.step('Кликаем по лого Яндекс')
    def click_logo_Yandex(self):
        self.driver.find_element(*logo_Yandex).click()
