from selenium.webdriver.common.by import By

name_field = [By.XPATH, ".//input[@placeholder = '* Имя']"]

surname_field = [By.XPATH, ".//input[@placeholder = '* Фамилия']"]

address_field = [By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"]

list_of_stations = [By.CLASS_NAME, "select-search__select"]

station_field = [By.XPATH, ".//input[@placeholder = '* Станция метро']"]

station_name = [By.XPATH, ".//li[@class = 'select-search__row'] / button"]

phone_number_field = [By.XPATH,".//input[@placeholder = '* Телефон: на него позвонит курьер']"]

button_next = [By.XPATH, ".//div[@class = 'Order_NextButton__1_rCA'] / button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"]

order_form_2_header = [By.XPATH, ".//div[@class = 'Order_Header__BZXOb']"]