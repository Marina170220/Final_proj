import requests
import allure

from Final_proj.data.DataProvider import DataProvider
from Final_proj.test_config import *

class BookApi:
    
    def __init__(self, test_data: DataProvider) -> None:
        self.__url = api_url
        self.__token = test_data.get_token()
        self.__cookie = {
            "name":"BK_ACCESS_TOKEN",
            "value": self.__token
        }

    
    @allure.step("Получить каталог всех книг")
    def get_books_list(self) -> list:
        url = self.__url + \
            "products/?page=1&per-page=60&include=category,"\
                "publishingHouse,customerProductAttraction,"\
                "ratingStats,author,orsProduct&filterPreset="\
                    "catalog-index&sortPreset=-popular"
        resp = requests.get(url, cookie=self.__cookie)
        return resp.json()['data']['data']
    
    
    @allure.step("Получить ID первой книги")
    def get_book_id(self):
        url = self.__url + \
            "products/?page=1&per-page=60&include=category,"\
                "publishingHouse,customerProductAttraction,"\
                "ratingStats,author,orsProduct&filterPreset="\
                    "catalog-index&sortPreset=-popular"
        resp = requests.get(url, cookie=self.__cookie)
        return resp.json()['data']['data'][0]['id']
    
    
    @allure.step("Добавить книгу в избранное")
    def add_book_to_wishlist(self, book_id):
        url = "{url}wishlist/?productId={id}".format(url=self.__url, id=book_id)
        resp = requests.post(url, cookie=self.__cookie)
        return resp.json()
    
    
    @allure.step("Получить список избранного")
    def get_wishlist(self):
        url = self.__url + \
            "wishlist/?page=1&per-page=60&include=product,product.author,"\
                "product.publishingHouse,product.category,product.orsProduct"
        resp = requests.get(url, cookie=self.__cookie)
        return resp.json()["data"]["included"]
    

    @allure.step("Удалить книгу из избранного")
    def delete_book_from_wishlist(self, book_id):
        url = "{url}wishlist/{id}/".format(url=self.__url, id=book_id)
        resp = requests.delete(url, cookie=self.__cookie)
        return resp.status_code
