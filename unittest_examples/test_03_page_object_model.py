# Test 22 - Page Object Model
# ----------------------------------------------------------------------------------------------------------------------
# Demostracion del Page Object Model. En este codigo se muestra como se ha reducido en gran medida el numero de lineas
# empleadas para 


from library.commons import Data
from library.pages import LoginPage
from library.simplified import SeleniumWebDriver
import unittest


class POMTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = SeleniumWebDriver()
        return super().setUp()

    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

    def test_login_empty(self):
        page = LoginPage(self.driver)
        error = page.Login('', '')
        return 'Empty Login Test: ' + 'OK' if error == 'Epic sadface: Username is required' else 'BAD'
    
    def test_login_empty_username(self):
        page = LoginPage(self.driver)
        error = page.Login('', Data.PASSWORD)
        return 'Empty Login Test: ' + 'OK' if error == 'Epic sadface: Username is required' else 'BAD'

    def test_login_empty_password(self):
        page = LoginPage(self.driver)
        error = page.Login(Data.USERNAME, '')
        return 'Empty Login Test: ' + 'OK' if error == 'Epic sadface: Password is required' else 'BAD'

    def test_login_wrong(self):
        page = LoginPage(self.driver)
        error = page.Login(Data.USERNAME, Data.PASSWORD)
        return 'Empty Login Test: ' + 'OK' if error == 'Epic sadface: Username and password do not match any user in this service' else 'BAD'

    def test_login_wrong_username(self):
        page = LoginPage(self.driver)
        error = page.Login(Data.USERNAME, 'secret_sauce')
        return 'Empty Login Test: ' + 'OK' if error == 'Epic sadface: Username and password do not match any user in this service' else 'BAD'

    def test_login_wrong_password(self):
        page = LoginPage(self.driver)
        error = page.Login('standard_user', Data.PASSWORD)
        return 'Empty Login Test: ' + 'OK' if error == 'Epic sadface: Username and password do not match any user in this service' else 'BAD'

    def test_login_ok(self):
        page = LoginPage(self.driver)
        error = page.Login('standard_user', 'secret_sauce')
        return 'Empty Login Test: ' + 'OK' if error == '' else 'BAD'

if __name__ == '__main__':
    unittest.main()