import time

from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome

from login_page import LoginPage
from Credentials import credentials


class User1:
    def test_select_product(self):
        driver = Chrome(service=Service(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com'
        driver.get(base_url)
        driver.maximize_window()

        print('Start Test User_1')
        login = LoginPage(driver)
        login.autorization(user_name=credentials()[1], login_password=credentials()[0])

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


test_1 = User1()
test_1.test_select_product()


class User2:
    def test_select_product(self):
        driver = Chrome(service=Service(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com'
        driver.get(base_url)
        driver.maximize_window()

        print('Start Test User_2')

        login = LoginPage(driver)
        login.autorization(user_name=credentials()[2], login_password=credentials()[0])
        error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        error_message = error_message.text
        print(error_message)
        assert error_message == "Epic sadface: Sorry, this user has been locked out."
        print("Skip this USER")
        driver.refresh()


test_2 = User2()
test_2.test_select_product()


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


class User4:
    def test_select_product(self):
        driver = Chrome(service=Service(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com'
        driver.get(base_url)
        driver.maximize_window()

        print('Start Test User_4')
        login = LoginPage(driver)
        login.autorization(user_name=credentials()[4], login_password=credentials()[0])

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


test_4 = User4()
test_4.test_select_product()

#
# select_shoping_cart = WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH,'//div[@id="shopping_cart_container"]')))
# select_shoping_cart.click()
# print('Click enter shopping cart')
# time.sleep(2)
#
# success_test = WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH,'//span[@class="title"]')))
# success_test = success_test.text
# print(success_test)
# assert success_test == "YOUR CART"
# print('Test success')
