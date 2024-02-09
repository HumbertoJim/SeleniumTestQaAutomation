"""
Fixture scopes
Fixtures are created when first requested by a test, and are destroyed based on their scope:

function: the default scope, the fixture is destroyed at the end of the test.

class: the fixture is destroyed during teardown of the last test in the class.

module: the fixture is destroyed during teardown of the last test in the module.

package: the fixture is destroyed during teardown of the last test in the package.

session: the fixture is destroyed at the end of the test session.
"""

from library.simplified import SeleniumWebDriver
from library.pages import SauceDemoPage, AdminDemoNopCommercePage
import pytest

@pytest.fixture(scope='module')
def setup_admindemonopcommerce():
    global driver
    print(':: INI ::')
    driver =  SeleniumWebDriver(implicitly_wait=2)
    page = AdminDemoNopCommercePage(driver)
    page.Login('admin@yourstore.com', 'admin')
    yield
    driver.close()
    print(':: FIN ::')

@pytest.fixture(scope='module')
def setup_saucedemopage():
    global driver2
    print(':: INI 2 ::')
    driver2 = SeleniumWebDriver(implicitly_wait=2)
    page = SauceDemoPage(driver2)
    page.Login('standard_user', 'secret_sauce')
    yield
    driver2.close()
    print(':: FIN 2 ::')

@pytest.mark.usefixtures('setup_admindemonopcommerce')
def test_one():
    driver.sleep(3)

@pytest.mark.usefixtures('setup_admindemonopcommerce')
def test_one_two():
    driver.sleep(3)

@pytest.mark.usefixtures('setup_saucedemopage')
def test_two():
    driver2.sleep(3)