import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Final_project.config.ConfigProvider import ConfigProvider

class CartPage:
    
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.__url = ConfigProvider().get("ui", "base_url")+"personal/cart"
    
    @allure.step("Перейти на страницу корзины")
    def go_cart(self):
        self.__driver.get(self.__url)

    @allure.step("Найти имя пользователя")    
    def user_name(self):
        return self.__driver.find_element(By.CSS_SELECTOR, ".user-button-container__text").text

    @allure.step("Получить содержимое корзины")    
    def get_cart(self):
        return self.__driver.find_element(By.CSS_SELECTOR, ".basket-page__list")
       
    @allure.step("Очистить корзину")
    def clear_cart(self):
        self.__driver.find_elements("xpath", '//button[text()=" Очистить "]').click()

    @allure.step("Восстановить корзину")
    def restore_cart(self):
        self.__driver.find_elements("xpath", '//button[text()=" Восстановить корзину "]').click()

    @allure.step("Перейти к оформлению")
    def make_order(self):
        self.__driver.find_elements("xpath", '//button[text()=" Перейти к оформлению "]').click()
     