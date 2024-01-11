import enum
from typing import Any


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
    message='test'
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