from selenium.webdriver.common.by import By


class LoginLocators:
    recovery_password_button = By.XPATH, ".//a[text()='Восстановить пароль']"
    email_input = By.XPATH, ".//input[@name='name']"
    password_input = By.XPATH, ".//input[@name='Пароль']"
    login_button = By.XPATH, ".//button[text()='Войти']"
