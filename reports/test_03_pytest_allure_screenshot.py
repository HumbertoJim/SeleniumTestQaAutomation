# Test 03 - Pytest Allure Report with Screenshots
# ----------------------------------------------------------------------------------------------------------------------
# Ejemplo de como agregar screenshots al reporte con allure.
#
# Ejecutar los comandos:
# pytest .\reports\test_03_pytest_allure_screenshot.py --alluredir .\reports\test_03_pytest_allure_screenshot
# allure serve .\reports\test_03_pytest_allure_screenshot


from library.simplified import SeleniumWebDriver
from library.pages import SauceDemoPage
import pytest
import allure
from allure_commons.types import AttachmentType

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
    allure.attach(driver.get_screenshot_as_png(), name='users', attachment_type=AttachmentType.PNG)
    driver.close(exit_time=2)
    assert msg == '', 'Invalid credentials'