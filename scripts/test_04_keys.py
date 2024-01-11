# Test 4
# ----------------------------------------------------------------------------------------------------------------------
# Se introduce una nueva herramienta llamada Keys, la cual permite movernos en el navegador tal cual
# como podemos hacerlo con las teclas. Por ejemplo, Keys.TAB implementa la acción de la tecla tab que
# permite movernos entre campo y campo de un formulario. Esto es util porque ya no tenemos que obtener
# la referencia de un elemento utilizando su xpath, por ejemplo, sino que basta con obtener el primer
# campo y el resto se llena utilizando las teclas.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


data = dict(
    name='Humberto',
    lastname='Jim',
    phone='0123456789',
    email='test@gmail.com',
    address='ipsum lorem'
)

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service('dependencies/webdrivers/chromedriver.exe')
)

driver.get('https://validaciones.rodrigovillanueva.com.mx/index.html')
driver.maximize_window()

name = driver.find_element(By.XPATH, "//input[@id='nombre']")
name.send_keys(
    data.get('name') +
    Keys.TAB +
    data.get('lastname') +
    Keys.TAB +
    data.get('phone') +
    Keys.TAB +
    data.get('email') +
    Keys.TAB +
    data.get('address') +
    Keys.TAB +
    Keys.ENTER
)
time.sleep(2)

driver.execute_script('window.scrollTo(0, 300)')

time.sleep(3)

driver.close()
print('Finished')