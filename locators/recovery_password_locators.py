from selenium.webdriver.common.by import By


class RecoveryPasswordLocators:
    recovery_button = By.XPATH, ".//button[text()='Восстановить']"
    input_button = By.XPATH, ".//input[@name='name']"
