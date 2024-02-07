import allure

from page_objects.base_page import BasePage
from locators.recovery_password_locators import RecoveryPasswordLocators


class RecoveryPasswordPage(BasePage):
    @allure.step('Ожидание видимости кнопки "Восстановить"')
    def waiting_visibility_restore_button(self):
        self.waiting_visibility_by_xpath(RecoveryPasswordLocators.recovery_button)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_restore_button(self):
        self.waiting_visibility_by_xpath(RecoveryPasswordLocators.recovery_button)
        self.click_by_xpath(RecoveryPasswordLocators.recovery_button)

    @allure.step('Заполнить поле "Email"')
    def fill_email_field(self, email):
        self.waiting_visibility_by_xpath(RecoveryPasswordLocators.input_button)
        self.fill_field_by_xpath(RecoveryPasswordLocators.input_button, email)
