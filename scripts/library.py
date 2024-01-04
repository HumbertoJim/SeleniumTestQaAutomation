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
    direction='ipsum lorem'
)


class links():
    BASIC_FORM = 'https://validaciones.rodrigovillanueva.com.mx/index.html'
    CONTACT_FORM ='https://rodrigovillanueva.com.mx/form/contact'
    MEDIUM = 'https://devjaime.medium.com/que-es-celery-en-django-con-python-19050ac30c41'
    UNITY = 'https://docs.unity3d.com/Manual/index.html'
    UNICARIBE = 'https://unicaribe.mx/'
    DATACAMP = 'https://www.datacamp.com/'