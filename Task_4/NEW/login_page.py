import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome


class USER:
    def __init__(self, user_name, login_password):
        self.user_name = user_name
        self.login_password = login_password

    def getintosite(self):
        # driver
        driver = Chrome(service=Service(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com'
        driver.get(base_url)
        driver.maximize_window()
        print('Start Test User_3')
        # Authorization on site
        username_field = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
        username_field.send_keys(self.user_name)
        password_field = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        password_field.send_keys(self.login_password)
        time.sleep(1)
        login_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="login-button"]')))
        login_button.click()
        time.sleep(1)
        print("Login into site\n")
        # Parsing element "PRODUCT"
        check_pars = driver.find_element(By.XPATH, "//span[@class='title']")
        check_pars = check_pars.text
        print(f"{check_pars}")
        assert check_pars == "PRODUCTS"
        # Logout from site
        select_burger_menu = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='react-burger-menu-btn']")))
        select_burger_menu.click()
        time.sleep(2)
        click_to_the_logout_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='logout_sidebar_link']")))
        click_to_the_logout_button.click()
        print('Logout')
