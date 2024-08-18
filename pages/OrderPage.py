import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Final_project.config.ConfigProvider import ConfigProvider


class OrderPage:
    
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.__url = ConfigProvider().get("ui", "base_url")+"order/make"
        self.__wait = WebDriverWait(driver, 5, 0.1)

    @allure.step("Перейти на страницу заказа")
    def go_order(self):
        self.__driver.get(self.__url)

    @allure.step("Выбор доставки курьером")    
    def сhoose_delivery(self):
        return self.__driver.find_element("xpath", '//li[text()="Курьером"]').click()
    
    @allure.step("Добавить комментарий для курьера")    
    def add_comment(self, comment):
        self.__driver.find_element("xpath", '//span[text()="Добавить комментарий для курьера"]').click()
        self.__wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ui-textarea__textarea"))).send_keys(comment)
        return self.__driver.find_element("xpath", '//span[text()="Добавить комментарий для курьера"]').text
     