from library.commons import Links, Data
from library.simplified import SeleniumWebDriver

def test_login1():
    global driver
    driver = SeleniumWebDriver()
    driver.get(Links.SAUCEDEMO)

    driver.find_element("//input[@id='user-name']").send_keys(Data.USERNAME)
    driver.find_element("//input[@id='password']").send_keys(Data.PASSWORD)
    driver.find_element("//input[@id='login-button']").click()
    
    driver.close()
