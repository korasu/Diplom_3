import allure

from page_objects.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание видимости кнопки "Восстановить пароль"')
    def waiting_visibility_forgot_password_button(self):
        self.waiting_visibility_by_xpath(LoginLocators.recovery_password_button)

    @allure.step('Клик кнопке "Восстановить пароль"')
    def click_forgot_password_button(self):
        self.waiting_visibility_by_xpath(LoginLocators.recovery_password_button)
        self.click_by_xpath(LoginLocators.recovery_password_button)

    @allure.step('Ожидание видимости поля ввода маила')
    def waiting_visibility_email_input(self):
        self.waiting_visibility_by_xpath(LoginLocators.email_input)

    @allure.step('Заполнить поле "Email"')
    def fill_email_field(self, email):
        self.waiting_visibility_by_xpath(LoginLocators.email_input)
        self.fill_field_by_xpath(LoginLocators.email_input, email)

    @allure.step('Заполнить поле "Пароль"')
    def fill_password_field(self, password):
        self.waiting_visibility_by_xpath(LoginLocators.password_input)
        self.fill_field_by_xpath(LoginLocators.password_input, password)

    @allure.step('Клик кнопке "Войти"')
    def click_login_button(self):
        self.waiting_visibility_by_xpath(LoginLocators.login_button)
        self.click_by_xpath(LoginLocators.login_button)