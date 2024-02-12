# Test 01 - Unittest
# ----------------------------------------------------------------------------------------------------------------------
# Se introduce al módulo unittest, esensial para la realizacion de pruebas. En este caso, se define una clase base que
# tiene dos funciones fundamentales para el inicio y cierre de la prueba, y se agrega un testcase que en este caso
# solo consiste en abrir una pagina y ya.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from library.commons import Dependencies, Links
import unittest
import time

class base_test(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(
            options=webdriver.ChromeOptions(),
            service=Service(Dependencies.CHROME_DRIVER)
        )
        self.driver.maximize_window()
        return super().setUp()
    
    def tearDown(self) -> None:
        time.sleep(4)
        self.driver.close()
        print('Finished')
        return super().tearDown()
    
    def test1(self):
        self.driver.get(Links.UNITY)

if __name__ == '__main__':
    unittest.main()