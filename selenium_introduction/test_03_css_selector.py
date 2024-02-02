# Test 3
# ----------------------------------------------------------------------------------------------------------------------
# Selecciona los campos del formulario utilizando el selector css de cada elemento, posteriormente coloca valores en ellos.
# Al finalizar, envia el formulario haciendo click en el boton Enviar.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from library.commons import Dependencies
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
    service=Service(Dependencies.CHROME_DRIVER)
)

driver.get('https://validaciones.rodrigovillanueva.com.mx/index.html')
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input[name='nombre']").send_keys(data.get('name'))
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[name='apellidos']").send_keys(data.get('lastname'))
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[name='tel']").send_keys('0123456789')
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(data.get('email'))
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[name='direccion']").send_keys(data.get('address'))
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(1)

driver.execute_script('window.scrollTo(0, 300)')
time.sleep(2)

driver.close()

print('Finished')