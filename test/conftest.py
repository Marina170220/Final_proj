import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Final_proj.api.BookApi import BookApi
from Final_proj.config.ConfigProvider import ConfigProvider
from Final_proj.data.DataProvider import DataProvider
from Final_proj.pages.AuthPage import AuthPage
from Final_proj.pages.MainPage import MainPage
from Final_proj.pages.CartPage import CartPage
from Final_proj.pages.OrderPage import OrderPage



@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.implicitly_wait(5)
        browser.maximize_window()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture(scope="session")
def api_client() -> BookApi:
    return BookApi()

@pytest.fixture
def wish_book_id() -> str:
    api = BookApi()
    with allure.step("Получить id книги для добавления в избранное"):
        resp = api.get_book_id()
    return resp

@pytest.fixture
def test_data():
    return DataProvider()

@pytest.fixture
def auth_page():
    return AuthPage(webdriver)

@pytest.fixture
def main_page():
    return MainPage(webdriver)

@pytest.fixture
def cart_page():
    return CartPage(webdriver)

@pytest.fixture
def order_page():
    return OrderPage(webdriver)
