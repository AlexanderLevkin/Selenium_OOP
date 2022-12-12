import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome

from login_page import LoginPage


class Test1:
    def test_select_product(self):
        driver = Chrome(executable_path=ChromeDriverManager().install())
        base_url = 'https://www.saucedemo.com'
        driver.get(base_url)
        driver.maximize_window()
        login_problem_user = 'problem_user'
        password = 'secret_sauce'

        print('Start Test')
        login = LoginPage(driver)
        login.autorization(user_name=login_problem_user, login_password=password)

        select_product = WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH,'//button[@id="add-to-cart-sauce-labs-backpack"]')))
        select_product.click()
        print('Select product')

        select_shoping_cart = WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH,'//div[@id="shopping_cart_container"]')))
        select_shoping_cart.click()
        print('Click enter shopping cart')
        time.sleep(2)

        success_test = WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH,'//span[@class="title"]')))
        success_test = success_test.text
        print(success_test)
        assert success_test == "YOUR CART"
        print('Test success')


test_2 =Test1()
test_2.test_select_product()