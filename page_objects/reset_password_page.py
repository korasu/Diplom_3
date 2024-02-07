import allure

from page_objects.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators


class ResetPasswordPage(BasePage):

    @allure.step('Ожидание видимости инпута "Введите код из письма"')
    def waiting_visibility_input_code_from_email(self):
        self.waiting_visibility_by_xpath(ResetPasswordLocators.input_email_code)

    @allure.step('Ввести пароль')
    def fill_password_field(self, password):
        self.waiting_visibility_by_xpath(ResetPasswordLocators.input_password)
        self.fill_field_by_xpath(ResetPasswordLocators.input_password, password)

    @allure.step('Клик по переключателю видимости пароля')
    def click_display_password_button(self):
        self.waiting_visibility_by_xpath(ResetPasswordLocators.visible_password_button)
        self.click_by_xpath(ResetPasswordLocators.visible_password_button)

    @allure.step('Проверка видимости пароля')
    def display_password_is_active(self):
        self.waiting_visibility_by_xpath(ResetPasswordLocators.password_input_form)
        return self.is_active(ResetPasswordLocators.password_input_form)