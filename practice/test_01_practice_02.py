from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from library.commons import Dependencies, Links, Data
import unittest
import time

class LoginPage:
    def __init__(self, driver : webdriver.Chrome) -> None:
        self.driver = driver

    def Login(self, username, password):
        self.driver.get(Links.SAUCEDEMO)
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        time.sleep(2)
        try:
            error = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
            )
            return error.text
        except TimeoutException:
            return ''


class PracticeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(
            options=webdriver.ChromeOptions(),
            service=webdriver.ChromeService(Dependencies.CHROME_DRIVER)
        )
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_login_bad(self):
        msg = LoginPage(self.driver).Login(Data.USERNAME, Data.PASSWORD)
        return 'Test Bad Login: ' + 'OK' if msg != '' else 'BAD'
    
    def test_login_ok(self):
        msg = LoginPage(self.driver).Login('standard_user', 'secret_sauce')
        return 'Test Ok Login: ' + 'OK' if msg == '' else 'BAD'
    
if __name__ == '__main__':
    unittest.main()