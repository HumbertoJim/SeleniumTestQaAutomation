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

    def __init__(self, driver=WebDriver.CHROME, implicitly_wait=2, explicitly_wait=5) -> None:
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

    def scroll_to(self, x : int, y : int):
        self.driver.execute_script(f'window.scrollTo({x}, {y})')

    def scroll_by(self, x : int, y: int):
        self.driver.execute_script(f'window.scrollBy({x}, {y})')

    def scroll_into_view(self, elem : WebElement, offset_x = 0, offset_y = 0):
        self.driver.execute_script(f'arguments[0].scrollIntoView()', elem)
        self.scroll_by(offset_x, offset_y)

    def find_element(self, value: str, by = By.XPATH, offset_x = 0, offset_y = 0) -> WebElement:
        elem = self.driver.find_element(by=by, value=value)
        self.scroll_into_view(elem, offset_x, offset_y)
        return elem
    
    def find_element_with_EC(self, value: str, by = By.XPATH, offset_x = 0, offset_y = 0, expected_condition = EC.visibility_of_element_located) -> WebElement:
        elem = WebDriverWait(self.driver, self.explicitly_wait).until(
            expected_condition([by, value])
        )
        self.scroll_into_view(elem, offset_x, offset_y)
        return elem
    
    def find_select(self, value: str, by = By.XPATH, offset_x = 0, offset_y = 0) -> Select:
        elem = self.find_element(value, by, offset_x, offset_y)
        select = Select(elem)
        return select
    
    def find_select_with_EC(self, value: str, by = By.XPATH, offset_x = 0, offset_y = 0, expected_condition = EC.visibility_of_element_located) -> Select:
        elem = self.find_element(value, by, offset_x, offset_y, expected_condition)
        select = Select(elem)
        return select
    
    def switch_to_frame(self, frame_reference : str | int | WebElement = 0 ):
        self.driver.switch_to.frame(frame_reference)

    def switch_to_alert(self):
        self.driver.switch_to.alert()

    def switch_to_default(self):
        self.driver.switch_to.default_content()
    
    def close(self, exit_time: int = 4):
        self.sleep(exit_time)
        self.driver.close()

    def get_screenshot_as_png(self):
        return self.driver.get_screenshot_as_png()