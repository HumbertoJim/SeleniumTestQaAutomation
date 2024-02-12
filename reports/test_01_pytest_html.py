# Test 01 - Pytest HTML Report
# ----------------------------------------------------------------------------------------------------------------------
# Se utiliza el plugin HTML para generar un reporte sencillo, el cual muestra información de los casos exitosos y los
# errores.
# 
# Ejecutar con el comando:
# pytest .\reports\test_01_pytest_html.py --html .\reports\test_01_pytest_html\report.html

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