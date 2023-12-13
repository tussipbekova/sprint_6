import allure
import pytest
from selenium import webdriver

from pages.important_questions_page import ImportantQuestionsPage
from locators.important_questions_locators import *


class TestImportantQuestions:
    driver = None

    # Блок Вопросы о важном на главной странице
    questions_and_answers_list = [[questions_1_field, answer_1_field, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
                                  [questions_2_field, answer_2_field, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
                                  [questions_3_field, answer_3_field, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
                                  [questions_4_field, answer_4_field, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
                                  [questions_5_field, answer_5_field, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
                                  [questions_6_field, answer_6_field, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
                                  [questions_7_field, answer_7_field,'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
                                  [questions_8_field, answer_8_field, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']]

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка вопросов и ответов на главной странице')
    @allure.description('На главной странице проверяем что при клике на вопрос открывается соответствующий ответ')
    @pytest.mark.parametrize('question_locator,answer_locator, answer_text', questions_and_answers_list)
    def test_questions_and_answers(self, question_locator, answer_locator, answer_text):

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        important_question_page = ImportantQuestionsPage(self.driver)

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

        # сравниваем ответ
        expected_answer = answer_text

        assert actual_answer == expected_answer


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
