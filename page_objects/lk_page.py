import allure

from page_objects.base_page import BasePage
from locators.lk_locators import LKLocators


class LKPage(BasePage):

    @allure.step('Ожидание видимости кнопки "История заказов"')
    def waiting_visibility_orders_history_button(self):
        self.waiting_visibility_by_xpath(LKLocators.order_history_button)

    @allure.step('Клик по кнопке "История заказов"')
    def click_orders_history_button(self):
        self.waiting_visibility_by_xpath(LKLocators.order_history_button)
        self.click_by_xpath(LKLocators.order_history_button)

    @allure.step('Клик по кнопке "Выход"')
    def click_exit_button(self):
        self.waiting_visibility_by_xpath(LKLocators.exit_button)
        self.click_by_xpath(LKLocators.exit_button)