# Test 2
# ----------------------------------------------------------------------------------------------------------------------
# Selecciona los campos del formulario utilizando el id de cada elemento, posteriormente coloca valores en ellos.
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

driver =  webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service(Dependencies.CHROME_DRIVER)
)

driver.get('https://validaciones.rodrigovillanueva.com.mx/index.html')
driver.maximize_window()

driver.find_element(By.ID, 'nombre').send_keys(data['name'])
time.sleep(1)

driver.find_element(By.ID, 'apellidos').send_keys(data['lastname'])
time.sleep(1)

driver.find_element(By.ID, 'tel').send_keys(data['phone'])
time.sleep(1)

driver.find_element(By.ID, 'email').send_keys(data['email'])
time.sleep(1)

driver.find_element(By.ID, 'direccion').send_keys(data['address'])
time.sleep(1)

driver.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Enviar')]").click()
time.sleep(1)

driver.execute_script('window.scrollTo(0, 300)')
time.sleep(2)

driver.close()

print("Finished")