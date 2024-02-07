from selenium.webdriver.common.by import By


class MainLocators:
    create_order_button = By.XPATH, ".//button[text()='Оформить заказ']"
    krator_bun = By.XPATH, ".//img[@alt='Краторная булка N-200i']"
    popup_ingredient_ditail = By.XPATH, ".//h2[text()='Детали ингредиента']"
    close_popup = By.XPATH, ".//button[@type='button']"
    burger_cart = By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]"
    count_buns = By.XPATH, "//ul[1]/a[2]//p[contains(@class, 'num')]"
    popup_order_identifier = By.XPATH, ".//p[text()='идентификатор заказа']"
    order_number_in_popup = By.XPATH, (".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m "
                                       "text text_type_digits-large mb-8']")
    lk_button = By.XPATH, ".//p[text()='Личный Кабинет']"
    constructor_button = By.XPATH, ".//p[text()='Конструктор']"
    order_feed_button = By.XPATH, ".//p[text()='Лента Заказов']"
