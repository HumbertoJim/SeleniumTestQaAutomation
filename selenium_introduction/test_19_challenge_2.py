# Test 19 - Challenge 2
# ----------------------------------------------------------------------------------------------------------------------
# Codigo para superar el segundo reto del curso, el cual consiste en verificar vi existen errores en los campos del
# formulario, errores como datos vacios. Si hay presente este tipo de mensajes, entonces llenar los campos para
# que el formulario pueda ser enviado sin problemas. Dado que la pagina del reto original fue dado de baja, se utilizo
# otra pagina similar.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from library.commons import Dependencies, Links, Data
import time

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service(Dependencies.CHROME_DRIVER)
)

driver.get(Links.BASIC_FORM)
driver.maximize_window()

if driver.find_element(value='errorNombre').is_displayed():
    print("Error name visible")
else:
    print('Error not visible')
time.sleep(2)

name = driver.find_element(value='nombre')
lastname = driver.find_element(value='apellidos')
phone = driver.find_element(value='tel')
email = driver.find_element(value='email')
address = driver.find_element(value='direccion')

lastname.send_keys(Data.LAST_NAME)
email.send_keys(Data.EMAIL)

btn = driver.find_element(By.XPATH, "//button[@type='submit']")
time.sleep(2)

btn.click()
time.sleep(2)

if driver.find_element(value='errorNombre').is_displayed():
    print('Name required')
    name.send_keys(Data.NAME)
if driver.find_element(value='errorApellidos').is_displayed():
    print('Lastname required')
    lastname.send_keys(Data.LAST_NAME)
if driver.find_element(value='errorTel').is_displayed():
    print('Phone required')
    phone.send_keys(Data.PHONE)
if driver.find_element(value='errorEmail').is_displayed():
    print('Email required')
    email.send_keys(Data.EMAIL)
if driver.find_element(value='errorDireccion').is_displayed():
    print('Address required')
    address.send_keys(Data.ADDRESS)
time.sleep(2)

btn.click()
driver.execute_script('window.scrollTo(0, 300)')

time.sleep(5)
driver.close()
print("Finished")