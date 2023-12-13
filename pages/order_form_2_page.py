import allure

from locators.order_form_2_locators import date_field, rent_time_field, rent_time_drop_down, calendar, scooter_color, \
    comments_field, order_button, confirm_yes_button, order_created_confirm_text


class OrderForm2Page:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполнение(выбор даты) поля Когда привезти самокат')
    def set_date(self, date):
        self.driver.find_element(*date_field).send_keys(date)
        self.driver.find_element(*calendar).click()

    @allure.step('Клик и выбор Срока аренды ')
    def click_rent_time_field(self):
        self.driver.find_element(*rent_time_field).click()
        self.driver.find_element(*rent_time_drop_down).click()

    @allure.step('Выбор цвета самоката')
    def choose_scooter_color(self):
        self.driver.find_element(*scooter_color).click()

    @allure.step('Заполнение поля Комментарий')
    def set_comments(self, comment):
        self.driver.find_element(*comments_field).send_keys(comment)

    @allure.step('Подтверждение кнопкой Заказать')
    def click_order_button(self):
        self.driver.find_element(*order_button).click()

    @allure.step('Подтверждение кнопкой Да')
    def click_confirm_yes_button(self):
        self.driver.find_element(*confirm_yes_button).click()

    @allure.step('Получение текста об успешном оформлении заказа')
    def get_order_created_confirm_text(self):
        return self.driver.find_element(*order_created_confirm_text).text




