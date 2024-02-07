import allure
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    @allure.step('Получить текст из шапки страницы')
    def get_text_from_order_feed_header(self):
        self.waiting_visibility_by_xpath(OrderFeedLocators.order_feed_header)
        return self.get_element_text_by_xpath(OrderFeedLocators.order_feed_header)

    @allure.step('Ожидание видимости шапки страницы')
    def waiting_visibility_order_feed_page_header(self):
        self.waiting_visibility_by_xpath(OrderFeedLocators.order_feed_header)

    @allure.step('Клик по первому заказу')
    def click_first_order(self):
        self.waiting_visibility_by_xpath(OrderFeedLocators.first_order)
        self.click_by_xpath(OrderFeedLocators.first_order)

    @allure.step('Ожидание видимости попапа с информацией о заказе')
    def waiting_visibility_order_info(self):
        self.waiting_visibility_by_xpath(OrderFeedLocators.popup_with_order_info)

    @allure.step('Получить текст из попапа с информацией о заказе')
    def get_text_from_popup_with_order_info(self):
        self.waiting_visibility_by_xpath(OrderFeedLocators.popup_with_order_info)
        return self.get_element_text_by_xpath(OrderFeedLocators.popup_with_order_info)

    @allure.step('Получить номер верхнего заказа')
    def get_text_from_first_order(self):
        self.waiting_visibility_by_xpath(OrderFeedLocators.number_first_order)
        return self.get_element_text_by_xpath(OrderFeedLocators.number_first_order)

    @allure.step('Получить количество заказов за все время')
    def get_orders_count_for_all_time(self):
        self.waiting_visibility_by_xpath(OrderFeedLocators.count_orders_for_all_time)
        return self.get_element_text_by_xpath(OrderFeedLocators.count_orders_for_all_time)

    @allure.step('Получить количество заказов за день')
    def get_orders_count_in_a_day(self):
        self.waiting_visibility_by_xpath(OrderFeedLocators.count_orders_in_day)
        return self.get_element_text_by_xpath(OrderFeedLocators.count_orders_in_day)

    @allure.step('Получаем номер заявки')
    def get_text_from_orders_in_work(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*OrderFeedLocators.order_in_work).text not in ("", "Все текущие заказы готовы!")
        )
        return self.driver.find_element(*OrderFeedLocators.order_in_work).text
