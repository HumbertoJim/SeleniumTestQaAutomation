from library import links, SeleniumWebDriverSimplifier

class LoginPage:
    def __init__(self, driver: SeleniumWebDriverSimplifier) -> None:
        self.driver = driver

    def Login(self, username: str, password: str) -> str:
        self.driver.get(links.SAUCEDEMO)
        self.driver.find_element("//input[@id='user-name']").send_keys(username)
        self.driver.find_element("//input[@id='password']").send_keys(password)
        self.driver.find_element("//input[@id='login-button']").click()
        try:
            error = self.driver.find_element_EC("//h3[@data-test='error']").text
        except:
            error = ''
        return error