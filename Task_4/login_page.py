from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def autorization(self, user_name, login_password):
        # Authorization on site
        username_field = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
        username_field.send_keys(user_name)
        password_field = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        password_field.send_keys(login_password)
        time.sleep(1)
        login_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="login-button"]')))
        login_button.click()
        time.sleep(1)
        print("Login into site\n")