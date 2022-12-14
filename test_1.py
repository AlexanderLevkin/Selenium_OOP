import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
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

        print('Start Test')
        login = LoginPage(driver)
        login.autorization(user_name="standard_user", login_password="secret_sauce")

        select_product = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH,'//button[@id="add-to-cart-sauce-labs-backpack"]')))
        select_product.click()
        print('Select product')

        select_shoping_cart = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH,'//div[@id="shopping_cart_container"]')))
        select_shoping_cart.click()
        print('Click enter shopping cart')
        time.sleep(2)

        success_test = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH,'//span[@class="title"]')))
        success_test = success_test.text
        print(success_test)
        assert success_test == "YOUR CART"
        print('Test success')


test = Test1() #Экземпляр класса
test.test_select_product()