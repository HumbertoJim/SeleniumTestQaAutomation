"""
pytest .\pytest_examples\test_11_parameters.py -v -s -m login
"""
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
    driver = SeleniumWebDriver()
    page = SauceDemoPage(driver)
    page.Login(username, password)
    driver.close(exit_time=2)