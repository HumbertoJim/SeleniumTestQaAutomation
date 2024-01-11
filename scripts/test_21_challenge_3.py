# Test 21 - Challenge 3
# ----------------------------------------------------------------------------------------------------------------------
# Codigo para superar el tercer reto del curso, el cual consiste en verificar todas las posibles entradas para loguearse
# en una pagina. Estas pruebas incluyen desde dejar los campos vacios, ingresar datos erroneos y datos correctos. Para
# esto, se emplea tanto unittest como selenium, pero todavia no se hace uso de los asserts.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from library import links
import unittest
import time


class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(
            options=webdriver.ChromeOptions(),
            service=Service('dependencies/webdrivers/chromedriver.exe')
        )
        self.driver.maximize_window()
        return super().setUp()
    
    def tearDown(self) -> None:
        time.sleep(4)
        self.driver.close()
        print('Finished')
        return super().tearDown()
    
    def test_login_empty(self):
        self.driver.get(links.SAUCEDEMO)
        
        self.driver.find_element(value='user-name').send_keys('')
        self.driver.find_element(value='password').send_keys('')
        self.driver.find_element(value='login-button').click()

        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        if error.text == 'Epic sadface: Username is required':
            print('Empty Login Test: OK')
        else:
            print('Empty Login Test: BAD')
    
    def test_login_empty_username(self):
        self.driver.get(links.SAUCEDEMO)
        
        self.driver.find_element(value='user-name').send_keys('')
        self.driver.find_element(value='password').send_keys('tiago')
        self.driver.find_element(value='login-button').click()

        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        if error.text == 'Epic sadface: Username is required':
            print('Empty Username Login Test: OK')
        else:
            print('Empty Username Login Test: BAD')

    def test_login_empty_password(self):
        self.driver.get(links.SAUCEDEMO)
        
        self.driver.find_element(value='user-name').send_keys('san')
        self.driver.find_element(value='password').send_keys('')
        self.driver.find_element(value='login-button').click()

        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        if error.text == 'Epic sadface: Password is required':
            print('Empty Password Login Test: OK')
        else:
            print('Empty Password Login Test: BAD')

    def test_login_wrong(self):
        self.driver.get(links.SAUCEDEMO)
        
        self.driver.find_element(value='user-name').send_keys('san')
        self.driver.find_element(value='password').send_keys('tiago')
        self.driver.find_element(value='login-button').click()

        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        if error.text == 'Epic sadface: Username and password do not match any user in this service':
            print('Wrong Login Test: OK')
        else:
            print('Wrong Login Test: BAD')

    def test_login_wrong_username(self):
        self.driver.get(links.SAUCEDEMO)
        
        self.driver.find_element(value='user-name').send_keys('san')
        self.driver.find_element(value='password').send_keys('secret_sauce')
        self.driver.find_element(value='login-button').click()

        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        if error.text == 'Epic sadface: Username and password do not match any user in this service':
            print('Wrong Username Login Test: OK')
        else:
            print('Wrong Username Login Test: BAD')

    def test_login_wrong_password(self):
        self.driver.get(links.SAUCEDEMO)
        
        self.driver.find_element(value='user-name').send_keys('standard_user')
        self.driver.find_element(value='password').send_keys('tiago')
        self.driver.find_element(value='login-button').click()

        error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        if error.text == 'Epic sadface: Username and password do not match any user in this service':
            print('Wrong Password Login Test: OK')
        else:
            print('Wrong Password Login Test: BAD')

    def test_login_ok(self):
        self.driver.get(links.SAUCEDEMO)
        
        self.driver.find_element(value='user-name').send_keys('standard_user')
        self.driver.find_element(value='password').send_keys('secret_sauce')
        self.driver.find_element(value='login-button').click()

        if self.driver.find_element(By.XPATH, "//div[@class='peek']").is_displayed():
            print('Ok Login Test: OK')
        else:
            print('Ok Login Test: BAD')

if __name__ == '__main__':
    unittest.main()