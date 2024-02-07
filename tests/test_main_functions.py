import allure

from data.urls import *
from page_objects.main_page import MainPage
from page_objects.order_feed_page import OrderFeedPage


class TestMainFunctionality:
    @allure.title('Проверка кнопки "Конструктор"')
    @allure.description('Проверка перехода в конструктор')
    def test_constructor_button(self, register_new_user_and_authorization_return_driver):
        main_page = MainPage(register_new_user_and_authorization_return_driver)
        main_page.click_personal_area_button()
        main_page.click_constructor_button()

        assert main_page.get_text_from_create_order_button() == "Оформить заказ"
        assert main_page.get_current_url() == f'{base_url}/'

    @allure.title('Проверка перехода в ленту заказов')
    @allure.description('Проверка перехода на страницу ленты заказов')
    def test_go_to_order_feed_page(self, register_new_user_and_authorization_return_driver):
        main_page = MainPage(register_new_user_and_authorization_return_driver)
        main_page.waiting_visibility_personal_area_button()
        main_page.click_personal_area_button()
        main_page.waiting_visibility_order_feed_button()
        main_page.click_order_feed_button()

        order_feed_page = OrderFeedPage(register_new_user_and_authorization_return_driver)
        order_feed_page.waiting_visibility_order_feed_page_header()
        assert order_feed_page.get_text_from_order_feed_header() == "Лента заказов"
        assert order_feed_page.get_current_url() == f'{base_url}{Endpoint.order_feed_endpoint}'

    @allure.title('Проверка появления всплывающего окна')
    @allure.description('Всплывающее окно появляется при клике на ингредиент')
    def test_popup_will_appear_if_click_to_ingredient(self, register_new_user_and_authorization_return_driver):
        main_page = MainPage(register_new_user_and_authorization_return_driver)
        main_page.click_krator_bun()
        main_page.waiting_visibility_ingredient_info_popup()

        assert main_page.get_text_from_header_ingredient_info_popup() == "Детали ингредиента"

    @allure.title('Проверка кликабельности крестика всплывающего окна')
    @allure.description('Всплывающее окно можно закрыть нажатием на крестик')
    def test_popup_with_ingredient_info_can_be_closed(self, register_new_user_and_authorization_return_driver):
        main_page = MainPage(register_new_user_and_authorization_return_driver)
        main_page.click_krator_bun()
        main_page.click_to_close_popup_button()
        main_page.waiting_invisibility_popup_with_ingredient_info()

        assert main_page.get_text_from_header_ingredient_info_popup() == ""

    @allure.title('Проверка изменения счетчика ингредиента')
    @allure.description('Изменения счетчика ингредиента при переносе в корзину')
    def test_ingredient_count_in_basket(self, register_new_user_and_authorization_return_driver):
        main_page = MainPage(register_new_user_and_authorization_return_driver)
        main_page.move_bun_in_basket()

        assert int(main_page.get_count_buns_in_basket()) == 2

    @allure.title('Создание заказа')
    @allure.description('Проверка успешного создания заказа авторизованным пользователем')
    def test_create_order_by_authorized_user(self, register_new_user_and_authorization_return_driver):
        main_page = MainPage(register_new_user_and_authorization_return_driver)
        main_page.move_bun_in_basket()
        main_page.click_create_order_button()
        main_page.waiting_visibility_popup_with_order_identifier()

        assert main_page.get_text_from_popup_with_order_identifier() == 'идентификатор заказа'
        