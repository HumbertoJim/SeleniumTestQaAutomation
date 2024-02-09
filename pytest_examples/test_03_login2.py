from library.commons import Links, Data
from library.simplified import SeleniumWebDriver


def test_login1():
    global driver
    driver = SeleniumWebDriver()
    driver.get(Links.SAUCEDEMO)

    driver.find_element("//input[@id='user-name']").send_keys(Data.USERNAME)
    driver.find_element("//input[@id='password']").send_keys(Data.PASSWORD)
    driver.find_element("//input[@id='login-button']").click()
    
    msg = driver.find_element("//h3[@data-test='error']")
    if msg.text == "Epic sadface: Username and password do not match any user in this service":
        print('Prueba de username y password erroneos exitosa')
    else:
        print('Prueba de username y password erroneos no exitosa')
    driver.close()

def test_login2():
    global driver
    driver = SeleniumWebDriver()
    driver.get(Links.SAUCEDEMO)

    driver.find_element("//input[@id='user-name']").send_keys(Data.USERNAME)
    driver.find_element("//input[@id='login-button']").click()
    
    msg = driver.find_element("//h3[@data-test='error']")
    if msg.text == "Epic sadface: Password is required":
        print('Prueba de password vacio exitosa')
    else:
        print('Prueba de password vacio no exitosa')
    driver.close()