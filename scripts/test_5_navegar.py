# Test 5 - Navegar
# ----------------------------------------------------------------------------------------------------------------------
# Se muestra como utilizar la funcion de back, para regresar a una pagina anterior.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


t = 4

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service('dependencies/webdrivers/chromedriver.exe')
)
driver.maximize_window()

driver.get('https://rodrigovillanueva.com.mx/form/contact')
time.sleep(t)

driver.get('https://docs.unity3d.com/Manual/index.html')
time.sleep(t)

driver.get('https://validaciones.rodrigovillanueva.com.mx/index.html')
time.sleep(t)

driver.get('https://pythonguides.com/login-system-in-python-django/')
time.sleep(t)

driver.back()
time.sleep(t)

driver.back()
time.sleep(t)

driver.back()
time.sleep(t)

driver.back()
time.sleep(t)

driver.forward()
time.sleep(t)

driver.forward()
time.sleep(t)

driver.forward()
time.sleep(t)

driver.forward()
time.sleep(t)

driver.close()
print('Finished')