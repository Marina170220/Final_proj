import allure
from selenium.webdriver.common.by import By
from selenium import webdriver


from Final_proj.config.ConfigProvider import ConfigProvider

class CartPage:
    
    def __init__(self, driver: webdriver, provider: ConfigProvider) -> None:
        self.__driver = driver
        self.__url = provider.get_ui_url()+"personal/cart"
    
    @allure.step("Перейти на страницу корзины")
    def go_cart(self):
        self.__driver.get(self.__url)

    @allure.step("Найти имя пользователя")    
    def user_name(self):
        return self.__driver.find_element(By.CLASS_NAME, "user-button-container__text").text

    @allure.step("Получить содержимое корзины")    
    def get_cart(self):
        return self.__driver.find_element(By.CLASS_NAME, "basket-page__list").is_displayed()
       
    @allure.step("Очистить корзину")
    def clear_cart(self):
        self.__driver.find_element("xpath", '//button[text()=" Очистить "]').click()
        return self.__driver.find_element(By.CLASS_NAME, "basket-cleared__title").is_displayed()

    @allure.step("Восстановить корзину")
    def restore_cart(self):
        self.__driver.find_elements("xpath", '//button[text()=" Восстановить корзину "]').click()
        return self.__driver.find_element(By.CLASS_NAME, "basket-page__list").is_displayed()

    @allure.step("Перейти к оформлению")
    def make_order(self):
        self.__driver.find_elements("xpath", '//button[text()=" Перейти к оформлению "]').click()
     