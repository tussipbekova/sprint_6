import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.important_questions_locators import training_simulator


class ImportantQuestionsPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки главной страницы')
    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(training_simulator))

    @allure.step('Скролл до раздела Вопросы о важном ')
    def scrolldown_to_question_field(self, question_locator):
        element = self.driver.find_element(*question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание до кликабельности вопроса')
    def wait_for_clickable_question(self, question_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(question_locator))

    @allure.step('Клик вопроса')
    def click_question(self, question_locator):
        self.driver.find_element(*question_locator).click()

    @allure.step('Ожидание до появления ответа')
    def wait_for_load_answer(self, answer_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(answer_locator))

    @allure.step('Получение ответа')
    def get_answer_field(self, answer_locator):
        return self.driver.find_element(*answer_locator).text


