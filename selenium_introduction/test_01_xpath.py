# Test 1
# ----------------------------------------------------------------------------------------------------------------------
# Selecciona los campos del formulario utilizando el xpath de cada elemento, posteriormente coloca valores en ellos.
# Al finalizar, envia el formulario haciendo click en el boton Submit.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from library.commons import Dependencies
import time


data = dict(
    name='Jim',
    email='test@gmail.com',
    subject='Learning Selenium',
    message='This is a Selenium test script'
)

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service(Dependencies.CHROME_DRIVER)
)

driver.get('https://rodrigovillanueva.com.mx/form/contact')
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='edit-name']").send_keys(data['name'])
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='edit-email']").send_keys(data['email'])
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='edit-subject']").send_keys(data['subject'])
time.sleep(1)

driver.find_element(By.XPATH, "//textarea[@id='edit-message']").send_keys(data['message'])
time.sleep(1)

driver.execute_script("window.scrollTo(0, 300)")
time.sleep(1)

driver.find_element(By.XPATH, "(//input[@type='submit'])[2]").click()
time.sleep(2)

driver.close()

print("Finished")