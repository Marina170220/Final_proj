import allure
from Final_proj.api.BookApi import BookApi

def test_get_books_list(api_client: BookApi):
    books_list = api_client.get_books_list()
    
    with allure.step("Проверить, что список книг не пустой"):
        assert len(books_list) > 0


def test_add_book_to_wishlist(api_client: BookApi, wish_book_id):
    api_client.add_book_to_wishlist(wish_book_id)
    wishlist = api_client.get_wishlist()

    with allure.step("Проверить, что в избранном 1 книга"):
        assert len(wishlist) == 1


def test_delete_book_from_wishlist(api_client: BookApi, wish_book_id):
    wishlist_before = api_client.get_wishlist()
    api_client.delete_book_from_wishlist(wish_book_id)
    wishlist_after = api_client.get_wishlist()

    with allure.step(
        "Проверить, что количество книг в избранном уменьшилось на 1"
        ):
        assert len(wishlist_after) == len(wishlist_before) - 1

    with allure.step("Проверить, что список избранного пуст"):
        assert len(wishlist_after) == 0


def test_add_book_with_invalid_id(api_client: BookApi, wish_book_id):
    wishlist_before = api_client.get_wishlist()
    resp = api_client.add_book_to_wishlist("")
    wishlist_after = api_client.get_wishlist()

    with allure.step(
        "Проверить, что книга не добавлена'"
        ):
        assert resp["success"] == False

    with allure.step(
        "Проверить, что количество книг в избранном не изменилось"
        ):
        assert len(wishlist_after) == len(wishlist_before)
        

def test_delete_book_with_invalid_id(api_client: BookApi, wish_book_id):
    api_client.add_book_to_wishlist(wish_book_id)             
    wishlist_before = api_client.get_wishlist()
    code = api_client.delete_book_from_wishlist("")
    wishlist_after = api_client.get_wishlist()

    with allure.step(
        "Проверить, что статус-код ответа 400 'Bad request'"
        ):
        assert code == 400

    with allure.step(
        "Проверить, что в избранном осталась одна книга"
        ):
        assert len(wishlist_after) == 1

    with allure.step(
        "Проверить, что количество книг в избранном не изменилось"
        ):
        assert len(wishlist_after) == len(wishlist_before)
