from library.commons import Links
from library.simplified import SeleniumWebDriver

class SauceDemoPage:
    def __init__(self, driver: SeleniumWebDriver) -> None:
        self.driver = driver

    def Login(self, username: str, password: str) -> str:
        self.driver.get(Links.SAUCEDEMO)
        self.driver.find_element("//input[@id='user-name']").send_keys(username)
        self.driver.find_element("//input[@id='password']").send_keys(password)
        self.driver.find_element("//input[@id='login-button']").click()
        try:
            error = self.driver.find_element_with_EC("//h3[@data-test='error']").text
        except:
            error = ''
        return error
    
class AdminDemoNopCommercePage:
    def __init__(self, driver: SeleniumWebDriver) -> None:
        self.driver = driver

    def Login(self, email: str, password: str) -> str:
        self.driver.get(Links.NOPCOMMERCE_ADMINDEMO)

        email_element = self.driver.find_element("//input[@id='Email']")
        email_element.clear()
        email_element.send_keys(email)

        password_element = self.driver.find_element("//input[@id='Password']")
        password_element.clear()
        password_element.send_keys(password)

        self.driver.find_element("//button[@type='submit']").click()
        try:
            error = self.driver.find_element_with_EC("//div[@class='message-error validation-summary-errors']").text
        except:
            error = ''
        return error