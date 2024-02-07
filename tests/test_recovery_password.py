import allure

from helpers.helpers import *
from page_objects.login_page import LoginPage
from page_objects.recovery_password_page import RecoveryPasswordPage
from page_objects.reset_password_page import ResetPasswordPage


class TestRestorePassword:
    @allure.title('Проверка кнопки восстановления пароля')
    @allure.description('Проверка перехода на страницу восстановления пароля со страницы авторизации')
    def test_restore_password_button(self, driver):
        driver.get(base_url + Endpoint.login_endpoint)

        login_page = LoginPage(driver)
        login_page.click_forgot_password_button()

        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.waiting_visibility_restore_button()

        assert recovery_password_page.get_current_url() == f'{base_url}{Endpoint.recovery_password_endpoint}'

    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    @allure.description('Проверка перехода на страницу для ввода кода, высланного на email')
    def test_entering_email_address_and_click_reset_button(self, driver):
        driver.get(base_url + Endpoint.recovery_password_endpoint)
        random_email = f'{generate_random_string(10)}@mail.ru'

        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.fill_email_field(random_email)
        recovery_password_page.click_restore_button()

        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.waiting_visibility_input_code_from_email()

        assert reset_password_page.get_current_url() == f'{base_url}{Endpoint.reset_password_endpoint}'

    @allure.title('Проверка кнопки показать/скрыть пароль')
    @allure.description('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_show_password_button(self, driver):
        driver.get(base_url + Endpoint.recovery_password_endpoint)

        random_email = f'{generate_random_string(10)}@mail.ru'
        random_password = generate_random_string(10)

        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.fill_email_field(random_email)
        recovery_password_page.click_restore_button()

        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.fill_password_field(random_password)
        reset_password_page.click_display_password_button()

        assert reset_password_page.display_password_is_active() == True