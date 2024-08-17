import allure
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.OrderPage import OrderPage

def test_auth(test_data: dict, auth_page: AuthPage, main_page: MainPage):
    phone = test_data.get("email")
    auth_page.go()
    auth_page.login_as() #КАК ДОБАВИТЬ КОД???
    user = main_page.user_name()
 
    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть "+user):
            assert user == test_data.get("name")

def test_main(test_data: dict, main_page: MainPage):
    search_book = test_data.get("search_book")
    main_page.go_main()
    user = main_page.user_name()
    books = main_page.get_books_list()
    search = main_page.find_search_field(search_book)


    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть "+user):
            assert user == test_data.get("name")

    with allure.step("Проверить, что отображается список книг"):
        assert books #КАК ПРОВЕРИТЬ, ЧТО ЭЛЕМЕНТ ЕСТЬ НА СТРАНИЦЕ

# ПРОВЕРИТЬ,ЧТО НАЗВАНИЯ КНИГ В ИЗБРАННОМ СОДЕРЖАТ ИСКОМОЕ СЛОВО

def test_cart(test_data: dict, cart_page: CartPage):
    cart_page.go_cart()
    user = cart_page.user_name()
    books = cart_page.get_cart()
    clear = cart_page.clear_cart()
    restore = cart_page.restore_cart()


    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть "+user):
            assert user == test_data.get("name")

# ПРОВЕРИТЬ,ЧТО КОРЗИНА НЕ ПУСТАЯ
# ПРОВЕРИТЬ,ЧТО ПОСЛЕ ОЧИСТКИ КОРЗИНА ПУСТАЯ
# ПРОВЕРИТЬ,ЧТО ПОСЛЕ ВОССТАНОВЛЕНИЯ КОРЗИНА НЕ ПУСТАЯ

def test_order(test_data: dict, order_page: OrderPage):
    order_page.go_order()
    comment_to_add = test_data.get("comment")
    comment = order_page.add_comment(comment_to_add).text #ПРОВЕРИТЬ СОДЕРЖИМОЕ ПОЛЯ

    with allure.step("Проверить, что комментарий отобразился верно"):
        with allure.step("Комментарий должен быть "+comment):
            assert comment == comment_to_add
