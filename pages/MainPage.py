import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from config.ConfigProvider import ConfigProvider
from data.DataProvider import DataProvider

class MainPage:
    
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.__url = ConfigProvider().get_ui_url()
        self.__data = DataProvider()
    
    @allure.step("Добавить куки авторизации")
    def add_cookie(self):
        cookie = {
            "name":"BK_ACCESS_TOKEN",
            "value": self.__data.get_token()
        }
        self.__driver.add_cookie(cookie)
   
    @allure.step("Перейти на главную страницу")
    def go_main(self):
        self.__driver.get(self.__url)
        
    @allure.step("Получить текущий URL")    
    def get_current_url(self) -> str:
        return self.__driver.current_url
    
    @allure.step("Найти имя пользователя")    
    def user_name(self):
        return self.__driver.find_element(By.CSS_SELECTOR, ".user-button-container__text").text

    @allure.step("Ввести значение для поиска")    
    def find_search_field(self, search_book):
        self.__driver.find_element(By.CSS_SELECTOR, ".search-form__input search-form__input--search").send_keys(search_book)

    @allure.step("Получить список книг")    
    def get_books_list(self):
        return self.__driver.find_element(By.CSS_SELECTOR, ".product-list app-catalog__products")

    @allure.step("Добавить книгу в корзину")    
    def add_book_to_cart(self):
        self.__driver.find_element("xpath", '//button[text()="  Купить "]').click()

    @allure.step("Перейти в корзину")    
    def go_to_cart(self):
        self.__driver.find_elements(By.CSS_SELECTOR, ".user-button-container__text").click()
