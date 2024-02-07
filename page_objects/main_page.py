import allure
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage
from locators.main_locators import MainLocators


class MainPage(BasePage):

    @allure.step('Клик по кнопки "Оформить заказ"')
    def click_create_order_button(self):
        self.waiting_visibility_by_xpath(MainLocators.create_order_button)
        self.click_by_xpath(MainLocators.create_order_button)

    @allure.step('Ожидание видимости кнопки "Оформить заказ"')
    def waiting_visibility_create_order_button(self):
        self.waiting_visibility_by_xpath(MainLocators.create_order_button)

    @allure.step('Получить текст кнопки "Оформить заказ"')
    def get_text_from_create_order_button(self):
        self.waiting_visibility_by_xpath(MainLocators.create_order_button)
        return self.get_element_text_by_xpath(MainLocators.create_order_button)

    @allure.step('Клик по краторная булке в списке конструктора"')
    def click_krator_bun(self):
        self.waiting_visibility_by_xpath(MainLocators.krator_bun)
        self.click_by_xpath(MainLocators.krator_bun)

    @allure.step('Ожидание видимости всплывающего окна с информацией о ингредиенте"')
    def waiting_visibility_ingredient_info_popup(self):
        self.waiting_visibility_by_xpath(MainLocators.popup_ingredient_ditail)

    @allure.step('Получить текст из шапки в попапе с информацией о ингредиенте')
    def get_text_from_header_ingredient_info_popup(self):
        return self.get_element_text_by_xpath(MainLocators.popup_ingredient_ditail)

    @allure.step('Ожидание исчезновения попапа  синформацией о ингредиенте')
    def waiting_invisibility_popup_with_ingredient_info(self):
        self.waiting_invisibility_by_xpath(MainLocators.popup_ingredient_ditail)

    @allure.step('Клик на кнопку закрытия попапа')
    def click_to_close_popup_button(self):
        self.waiting_visibility_by_xpath(MainLocators.close_popup)
        self.click_by_xpath(MainLocators.close_popup)

    @allure.step('Перенести булку в корзину')
    def move_bun_in_basket(self):
        self.waiting_visibility_by_xpath(MainLocators.krator_bun)
        self.waiting_visibility_by_xpath(MainLocators.burger_cart)
        self.move_from_to(MainLocators.krator_bun, MainLocators.burger_cart)

    @allure.step('Получить количество добавленных булок')
    def get_count_buns_in_basket(self):
        self.waiting_visibility_by_xpath(MainLocators.count_buns)
        return self.get_element_text_by_xpath(MainLocators.count_buns)

    @allure.step('Ожидание видимости попапа с идентификатором заказа')
    def waiting_visibility_popup_with_order_identifier(self):
        self.waiting_visibility_by_xpath(MainLocators.popup_order_identifier)

    @allure.step('Получить текст из попапа с информацией о созданном заказе')
    def get_text_from_popup_with_order_identifier(self):
        return self.get_element_text_by_xpath(MainLocators.popup_order_identifier)

    @allure.step('Получаем номер заявки')
    def get_order_number_from_home_page(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*MainLocators.order_number_in_popup).text not in ("", "9999")
        )
        return self.driver.find_element(*MainLocators.order_number_in_popup).text

    @allure.step('Клик на "Личный кабинет"')
    def click_personal_area_button(self):
        self.click_by_xpath(MainLocators.lk_button)

    @allure.step('Клик на "Конструктор')
    def click_constructor_button(self):
        self.click_by_xpath(MainLocators.constructor_button)

    @allure.step('Ожидание видимости кнопки "Личный кабинет"')
    def waiting_visibility_personal_area_button(self):
        self.waiting_visibility_by_xpath(MainLocators.lk_button)

    @allure.step('Ожидание видимости кнопки "Лента заказов"')
    def waiting_visibility_order_feed_button(self):
        self.waiting_visibility_by_xpath(MainLocators.order_feed_button)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_order_feed_button(self):
        self.click_by_xpath(MainLocators.order_feed_button)
