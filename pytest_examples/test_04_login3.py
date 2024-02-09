from library.commons import Links, Data
from library.simplified import SeleniumWebDriver

from pytest_examples.test_03_login2 import test_login1, test_login2

def test_login3():
    global driver
    driver = SeleniumWebDriver()
    driver.get(Links.SAUCEDEMO)

    driver.find_element("//input[@id='password']").send_keys(Data.PASSWORD)
    driver.find_element("//input[@id='login-button']").click()
    
    msg = driver.find_element("//h3[@data-test='error']")
    if msg.text == "Epic sadface: Username is required":
        print('Prueba de username vacio exitosa')
    else:
        print('Prueba de username vacio no exitosa')
    driver.close()

def test_login4():
    global driver
    driver = SeleniumWebDriver()
    driver.get(Links.SAUCEDEMO)

    driver.find_element("//input[@id='user-name']").send_keys('problem_user')
    driver.find_element("//input[@id='password']").send_keys('secret_sauce')
    driver.find_element("//input[@id='login-button']").click()
    
    msg = driver.find_element_with_EC("//div[@class='product_label']")
    if msg.text == "Products":
        print('Prueba de username y password correctos exitosa')
    else:
        print('Prueba de username y password correctos no exitosa')
    driver.close()