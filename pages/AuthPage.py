import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Final_project.config.ConfigProvider import ConfigProvider

class AuthPage:
    
    def __init__(self, driver: WebDriver) -> None:
        self.__url = ConfigProvider().get("ui", "base_url")
        self.__driver = driver
        
    @allure.step("Перейти на главную страницу")
    def go(self):
        self.__driver.get(self.__url)
    
    @allure.step("Перейти в личный кабинет")
    def login_as(self):
        self.__driver.find_element(By.CLASS_NAME, "user-buttons__icon").click()
        
    @allure.step("Ввести номер телефона")
    def add_phone(self, phone: str):
        self.__driver.find_element(By.CLASS_NAME, "ui-input__input").send_keys(phone)
        self.__driver.find_element("xpath", '//button[text()=" Получить код "]').click()
