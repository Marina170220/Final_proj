import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from Final_proj.api.BookApi import BookApi
from Final_proj.test_config import driver_path
from Final_proj.data.DataProvider import DataProvider
from Final_proj.pages.AuthPage import AuthPage
from Final_proj.pages.MainPage import MainPage
from Final_proj.pages.CartPage import CartPage
from Final_proj.pages.OrderPage import OrderPage


@pytest.fixture(scope="session")
def browser():
    with allure.step("Открыть и настроить браузер"):
        chrome_options = Options()
        chrome_service=Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(executable_path=driver_path, service=chrome_service, options=chrome_options)
        browser.implicitly_wait(5)
        browser.maximize_window()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def test_data():
    return DataProvider()


@pytest.fixture
def add_cookie(test_data: DataProvider, browser: webdriver):
    cookie = {
            "name":"BK_ACCESS_TOKEN",
            "value": test_data.get_token()
        }
    browser.add_cookie(cookie)


@pytest.fixture
def add_invalid_cookie(browser: webdriver):
    cookie = {
            "name":"BK_ACCESS_TOKEN",
            "value": ""
        }
    browser.add_cookie(cookie)


@pytest.fixture
def api_client() -> BookApi:
    return BookApi(test_data)


@pytest.fixture
def wish_book_id() -> str:
    api = api_client
    with allure.step("Получить id книги для добавления в избранное"):
        resp = api.get_book_id()
    return resp


@pytest.fixture
def auth_page():
    return AuthPage(browser)


@pytest.fixture
def main_page():
    return MainPage(browser, test_data, add_cookie)


@pytest.fixture
def main_page_no_auth():
    return MainPage(browser, test_data, add_invalid_cookie)


@pytest.fixture
def cart_page():
    return CartPage(browser, add_cookie)


@pytest.fixture
def order_page():
    return OrderPage(browser, add_cookie)
