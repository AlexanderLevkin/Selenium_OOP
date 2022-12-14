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

class User3:
    def test_select_product(self):
        driver = Chrome(service=Service(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com'
        driver.get(base_url)
        driver.maximize_window()

        print('Start Test User_3')
        login = LoginPage(driver)
        login.autorization(user_name=credentials()[3], login_password=credentials()[0])

        check_pars = driver.find_element(By.XPATH, "//span[@class='title']")
        check_pars = check_pars.text
        print(f"{check_pars}")
        assert check_pars == "PRODUCTS"

        select_burger_menu = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='react-burger-menu-btn']")))
        select_burger_menu.click()
        time.sleep(2)
        click_to_the_logout_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='logout_sidebar_link']")))
        click_to_the_logout_button.click()
        print('Logout')


test_3 = User3()
test_3.test_select_product()