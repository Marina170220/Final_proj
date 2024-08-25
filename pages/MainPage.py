import allure
from selenium.webdriver.common.by import By
from selenium import webdriver

from Final_proj.data.DataProvider import DataProvider
from Final_proj.test_config import *

class MainPage:
    
    def __init__(self, browser: webdriver, data: DataProvider, add_cookie) -> None:
        self.__driver = browser
        self.__url = ui_url
        self.__data = data
        self.__cookie = add_cookie
    
   
    @allure.step("Перейти на главную страницу")
    def go_main(self):
        self.__driver.get(self.__url)

        
    @allure.step("Получить текущий URL")    
    def get_current_url(self) -> str:
        return self.__driver.current_url
    
    
    @allure.step("Найти имя пользователя")    
    def user_name(self):
        return self.__driver.find_element(
            By.CLASS_NAME, "user-button-container__text"
            ).text
    

    @allure.step("Ввести значение для поиска")    
    def find_search_field(self, search_book):
        self.__driver.find_element(
            By.CLASS_NAME, "search-form__input search-form__input--search"
            ).send_keys(search_book)
        return self.__driver.find_element(
            By.CLASS_NAME, 
            "ui-link ui-link__color-scheme--two product-description__link base-link"
            ).text
    

    @allure.step("Получить список книг")    
    def get_books_list(self):
        return self.__driver.find_element(
            By.CLASS_NAME, "product-list app-catalog__products"
            ).is_displayed()
    

    @allure.step("Добавить книгу в корзину")    
    def add_book_to_cart(self):
        self.__driver.find_element(
            "xpath", '//button[text()="  Купить "]'
            ).click()
        return self.__driver.find_element(
            "xpath", '//button[text()="  Купить "]'
            ).text 
    

    @allure.step("Перейти в корзину")    
    def go_to_cart(self):
        self.__driver.find_elements(
            By.CLASS_NAME, "user-button-container__text"
            ).click()
