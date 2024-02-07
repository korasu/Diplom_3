from selenium.webdriver.common.by import By


class LKLocators:
    order_history_button = By.XPATH, ".//a[text()='История заказов']"
    exit_button = By.XPATH, ".//button[text()='Выход']"
