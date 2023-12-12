from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.important_questions_locators import training_simulator


class ImportantQuestionsPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(training_simulator))

    def scrolldown_to_question_field(self, question_locator):
        element = self.driver.find_element(*question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_clickable_question(self, question_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(question_locator))

    def click_question(self, question_locator):
        self.driver.find_element(*question_locator).click()

    def wait_for_load_answer(self, answer_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(answer_locator))

    def get_answer_field(self, answer_locator):
        return self.driver.find_element(*answer_locator).text


