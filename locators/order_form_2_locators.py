from selenium.webdriver.common.by import By

date_field = [By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"]

calendar = [By.XPATH, ".//div[@class = 'react-datepicker__week'] /div[text()='14']"]

rent_time_field = [By.CLASS_NAME, "Dropdown-placeholder"]

rent_time_drop_down = [By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() = 'сутки']"]

scooter_color = [By.XPATH, ".//input[@id = 'black']"]

comments_field = [By.XPATH, ".//div[@class = 'Input_InputContainer__3NykH']/input[@placeholder = 'Комментарий для курьера']"]

order_button = [By.XPATH, ".//div[@class = 'Order_Buttons__1xGrp'] /button[text()='Заказать']"]

confirm_yes_button = [By.XPATH, ".//div[@class = 'Order_Buttons__1xGrp'] /button[text()='Да']"]

order_created_confirm_text = [By.XPATH,".//div[@class = 'Order_ModalHeader__3FDaJ']"]
