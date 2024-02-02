from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from library.commons import Dependencies
import time
import enum


class SeleniumWebDriver:
    class WebDriver(enum.Enum):
        CHROME = enum.auto()
        FIREFOX = enum.auto()

    def __init__(self, driver=WebDriver.CHROME, implicitly_wait=5, explicitly_wait=10) -> None:
        if driver == SeleniumWebDriver.WebDriver.CHROME:
            self.driver = webdriver.Chrome(webdriver.ChromeOptions(), webdriver.ChromeService(Dependencies.CHROME_DRIVER))
        else:
            self.driver = webdriver.Firefox(webdriver.FirefoxOptions(), webdriver.FirefoxService(Dependencies.FIREFOX_DRIVER))
        self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        self.explicitly_wait = explicitly_wait

    def sleep(self, seconds: int = 2) -> None:
        time.sleep(seconds)

    def get(self, url: str) -> None:
        self.driver.get(url)

    def find_element(self, value: str, by = By.XPATH) -> WebElement:
        elem = self.driver.find_element(by=by, value=value)
        self.driver.execute_script('arguments[0].scrollIntoView()', elem)
        return elem
    
    def find_element_with_EC(self, value: str, by = By.XPATH, expected_condition = EC.visibility_of_element_located) -> WebElement:
        elem = WebDriverWait(self.driver, self.explicitly_wait).until(
            expected_condition([by, value])
        )
        self.driver.execute_script('arguments[0].scrollIntoView()', elem)
        return elem
    
    def find_select(self, value: str, by = By.XPATH) -> Select:
        elem = self.find_element(value, by)
        select = Select(elem)
        return select
    
    def find_select_with_EC(self, value: str, by = By.XPATH, expected_condition = EC.visibility_of_element_located) -> Select:
        elem = self.find_element(value, by, expected_condition)
        select = Select(elem)
        return select
    
    def close(self, exit_time: int = 4):
        self.sleep(exit_time)
        self.driver.close()
        print('Finished')
