import pathlib

__BASE_DIR__ = pathlib.Path(__file__).resolve().parent

class Dependencies:
    CHROME_DRIVER = __BASE_DIR__ / 'dependencies' / 'webdrivers' / 'chromedriver.exe'
    FIREFOX_DRIVER = __BASE_DIR__ / 'dependencies' / 'webdrivers' / 'geckodriver.exe'

class Links():
    BASIC_FORM = 'https://validaciones.rodrigovillanueva.com.mx/index.html'
    CHECK_FORM = 'https://validaciones.rodrigovillanueva.com.mx/Radios_Ok.html'
    COMBOBOX_FORM = 'https://validaciones.rodrigovillanueva.com.mx/ComboBox_ok.html'
    MODAL_FORM = 'https://validaciones.rodrigovillanueva.com.mx/Datatables_OK.html'
    CONTACT_FORM ='https://rodrigovillanueva.com.mx/form/contact'
    CHALLENGE_FORM = 'https://rodrigovillanueva.com.mx/form/demo-application'
    IMAGE_FORM = 'https://www.selenium.dev/selenium/web/upload.html'
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
    NOPCOMMERCE_ADMINDEMO = 'https://admin-demo.nopcommerce.com/login'

class Files:
    class Images:
        TEST = str(__BASE_DIR__ / 'files' / 'images' / 'test.png')

class Data:
    NAME = 'MyName'
    LAST_NAME = 'Lastname'
    PHONE = '0123456789'
    EMAIL = 'test@gmail.com'
    ADDRESS = 'ipsum lorem'
    CITY = 'CDMX'
    CP = '5000'
    MESSAGE = 'test'
    USERNAME = 'san'
    PASSWORD = 'tiago'
    LOREM_IPSUM = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'