import allure
import pytest
from selenium import webdriver

from data.Data import questions_and_answers_list
from pages.main_page  import MainPage


class TestImportantQuestions:
    driver = None


    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка вопросов и ответов на главной странице')
    @allure.description('На главной странице проверяем что при клике на вопрос открывается соответствующий ответ')
    @pytest.mark.parametrize('question_locator,answer_locator, answer_text', questions_and_answers_list)
    def test_questions_and_answers(self, question_locator, answer_locator, answer_text):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        important_question_page = MainPage(self.driver)

        # ожидаем появления на странице Вопросы о важном
        important_question_page.wait_for_load_home_page()

        # скролим до вопрос 1
        important_question_page.scrolldown_to_question_field(question_locator)

        # ожидаем кликабельность вопроса
        important_question_page.wait_for_clickable_question(question_locator)

        #кликаем по вопросу
        important_question_page.click_question(question_locator)

        # ожидаем появления на странице ответа на вопрос
        important_question_page.wait_for_load_answer(answer_locator)

        # находим и извлекаем ответ
        actual_answer = important_question_page.get_answer_field(answer_locator)

        assert actual_answer == answer_text


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
