import allure
from Final_proj.pages.AuthPage import AuthPage
from Final_proj.pages.MainPage import MainPage
from Final_proj.pages.CartPage import CartPage
from Final_proj.pages.OrderPage import OrderPage

def test_auth(test_data: dict, auth_page: AuthPage, main_page: MainPage):
    phone = test_data["email"]
    auth_page.go()
    auth_page.login_as() #КАК ДОБАВИТЬ КОД???
    user = main_page.user_name()
 
    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть "+user):
            assert user == test_data["name"]

def test_main(test_data: dict, main_page: MainPage):
    search_book = test_data["search_book"]
    main_page.go_main()
    user = main_page.user_name()
    books = main_page.get_books_list()
    search = main_page.find_search_field(search_book)
    add_book_button = main_page.add_book_to_cart()


    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть "+user):
            assert user == test_data["name"]

    with allure.step("Проверить, что отображается список книг"):
        assert books is True

    with allure.step("Проверить, что отображаются книги, соответствующие поиску"):
        with allure.step("В названии книг должно быть слово "+test_data["search_book"]):
            assert test_data["search_book"] in search

    with allure.step("Проверить, что при нажаьтт снопки Купить меняется текст кнопки"):
        with allure.step("Текст кнопки должен поменяться на 'Оформить'"):
            assert add_book_button == 'Оформить'


def test_cart(test_data: dict, cart_page: CartPage):
    cart_page.go_cart()
    user = cart_page.user_name()
    books = cart_page.get_cart()
    clear = cart_page.clear_cart()
    restore = cart_page.restore_cart()


    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть "+user):
            assert user == test_data["name"]

    with allure.step("Проверить, что в корзине есть товары"):
        assert books is True

    with allure.step("Проверить, что корзина пустая после нажатия конпки Очистить"):
        assert clear is True

    with allure.step("Проверить, что корзина восстановлена после нажатия конпки Восстановить"):
        assert restore is True
   

def test_order(test_data: dict, order_page: OrderPage):
    order_page.go_order()
    comment_to_add = test_data["comment"]
    comment = order_page.add_comment(comment_to_add)

    with allure.step("Проверить, что комментарий отобразился верно"):
        with allure.step("Комментарий должен быть "+comment):
            assert comment == comment_to_add
