from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

import time
import enum


class str_dict(dict):
    def get(self, key):
        value = super().get(key)
        value = value if value else ''
        return value

data = str_dict(
    name='MyName',
    lastname='Lastname',
    phone='0123456789',
    email='test@gmail.com',
    address='ipsum lorem',
    city='CDMX',
    cp='5000',
    message='test',
    username='san',
    password='tiago'
)

class links():
    BASIC_FORM = 'https://validaciones.rodrigovillanueva.com.mx/index.html'
    CHECK_FORM = 'https://validaciones.rodrigovillanueva.com.mx/Radios_Ok.html'
    COMBOBOX_FORM = 'https://validaciones.rodrigovillanueva.com.mx/ComboBox_ok.html'
    MODAL_FORM = 'https://validaciones.rodrigovillanueva.com.mx/Datatables_OK.html'
    CONTACT_FORM ='https://rodrigovillanueva.com.mx/form/contact'
    CHALLENGE_FORM = 'https://rodrigovillanueva.com.mx/form/demo-application'
    IMAGE_FORM = 'https://pinetools.com/es/brillo-contraste-imagen'
    MEDIUM = 'https://devjaime.medium.com/que-es-celery-en-django-con-python-19050ac30c41'
    UNITY = 'https://docs.unity3d.com/Manual/index.html'
    UNICARIBE = 'https://unicaribe.mx/'
    DATACAMP = 'https://www.datacamp.com/'
    SELENIUM = 'https://www.selenium.dev/'
    SELENIUM_DYNAMIC = 'https://www.selenium.dev/selenium/web/dynamic.html'
    SELENIUM_ALERT = 'https://www.selenium.dev/selenium/web/alerts.html'
    PIXABAY = 'https://pixabay.com/es/'
    ALERT_VALIDATION = 'https://the-internet.herokuapp.com/javascript_alerts'
    SAUCEDEMO = 'https://www.saucedemo.com/v1/'

class SeleniumWebDriverSimplifier:
    class WebDriver(enum.Enum):
        CHROME = enum.auto()
        FIREFOX = enum.auto()

    def __init__(self, driver=WebDriver.CHROME, implicitly_wait=5, explicitly_wait=10) -> None:
        if driver == SeleniumWebDriverSimplifier.WebDriver.CHROME:
            self.driver = webdriver.Chrome(webdriver.ChromeOptions(), webdriver.ChromeService('dependencies/webdrivers/chromedriver.exe'))
        else:
            self.driver = webdriver.Firefox(webdriver.FirefoxOptions(), webdriver.FirefoxService('dependencies/webdrivers/geckodriver.exe'))
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
