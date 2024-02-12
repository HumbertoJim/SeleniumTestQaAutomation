# Test 04 - Pytest Allure Report with Error Screenshots
# ----------------------------------------------------------------------------------------------------------------------
# Ejemplo de como agregar screenshots al reporte con allure, especificamente de la parte que genero el error.
#
# Ejecutar los comandos:
# pytest .\reports\test_04_pytest_allure_screenshot_error.py --alluredir .\reports\test_04_pytest_allure_screenshot_error
# allure serve .\reports\test_04_pytest_allure_screenshot_error


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

@pytest.fixture()
def log_on_failure(request):
    global driver, page
    driver = SeleniumWebDriver(implicitly_wait=1, explicitly_wait=1)
    page = SauceDemoPage(driver)

    yield

    item = request.node
    if item.rep_call.failed:
        print('#'*30)
        # for some strange reason, the image is not atrached
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=AttachmentType.PNG)

    driver.close(exit_time=2)
    

@pytest.mark.login
@pytest.mark.usefixtures('log_on_failure')
@pytest.mark.parametrize("username, password", get_data())
def test_login(username, password):
    global driver, page
    msg = page.Login(username, password)
    allure.attach(driver.get_screenshot_as_png(), name="Login", attachment_type=AttachmentType.PNG)
    assert msg == '', 'Invalid credentials'