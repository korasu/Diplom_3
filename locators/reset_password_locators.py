from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    input_email_code = By.XPATH, ".//label[text()='Введите код из письма']"
    input_password = By.XPATH, ".//input[@type='password']"
    visible_password_button = By.XPATH, "//div[contains(@class, 'input__icon')]"
    password_input_form = By.XPATH, "//div[contains(@class, 'input_status_active')]"
