# Test 02 - Pytest Allure Report
# ----------------------------------------------------------------------------------------------------------------------
# En este caso, se utiliza el plugin de allure-pytest para generar ciertos los archivos necesarios, los cuales serviran
# para generar el reporte. Estos archivos son empleados por el servidor de Allure, a fin de desplegar la información de
# los errores encontrados. 
#
# Ejecutar los comandos:
# pytest .\reports\test_02_pytest_allure.py --alluredir .\reports\test_02_pytest_allure
# allure serve .\reports\test_02_pytest_allure


from library.simplified import SeleniumWebDriver
from library.pages import SauceDemoPage
import pytest

def get_data():
    return [
        ('Padro', 'asdf'),
        ('Karina', '2452'),
        ('standard_user', '2452'),
        ('Gilberto', 'secret_sauce'),
        ('standard_user', 'secret_sauce'),
    ]

@pytest.mark.login
@pytest.mark.parametrize("username, password", get_data())
def test_login(username, password):
    driver = SeleniumWebDriver(implicitly_wait=1, explicitly_wait=1)
    page = SauceDemoPage(driver)
    msg = page.Login(username, password)
    driver.close(exit_time=2)
    assert msg == '', 'Invalid credentials'