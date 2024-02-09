from library.commons import Data
from library.simplified import SeleniumWebDriver
from library.pages import SauceDemoPage


def validate_login(username, password, message):
    driver = SeleniumWebDriver()
    page = SauceDemoPage(driver)
    msg = page.Login(username, password)
    driver.close()
    return msg == message

def test_login1():
    result = validate_login(Data.USERNAME, Data.PASSWORD, "Epic sadface: Username and password do not match any user in this service")
    if result:
        print('Prueba de username y password erroneos exitosa')
    else:
        print('Prueba de username y password erroneos no exitosa')

def test_login2():
    result = validate_login(Data.USERNAME, '', 'Epic sadface: Password is required')
    if result:
        print('Prueba de password vacio exitosa')
    else:
        print('Prueba de password vacio no exitosa')

def test_login3():
    result = validate_login('', Data.PASSWORD, 'Epic sadface: Username is required')
    if result:
        print('Prueba de username vacio exitosa')
    else:
        print('Prueba de username vacio no exitosa')


def test_login4():
    result = validate_login('problem_user', 'secret_sauce', '')
    if result:
        print('Prueba de username y password correctos exitosa')
    else:
        print('Prueba de username y password correctos no exitosa')