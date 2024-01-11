# Test 8 - Checkbox
# ----------------------------------------------------------------------------------------------------------------------
# Ejemplo de como interactuar con checkbox. En resumen, funciona de la misma forma que un boton.
# Selecciona el elemento de interes y haz click en el.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from library import links, data
import time

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service('dependencies/webdrivers/chromedriver.exe')
)

driver.get(links.CHECK_FORM)
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='campo1']").send_keys(data.get('name'))
driver.find_element(By.XPATH, "//input[@id='campo2']").send_keys(data.get('phone'))
driver.find_element(By.XPATH, "//input[@id='opcion2']").click()
driver.find_element(By.XPATH, "//input[@id='opcionA']").click() # checkbox
driver.find_element(By.XPATH, "//input[@id='opcionB']").click() # checbbox
driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.execute_script('window.scrollTo(0, 300)')
time.sleep(5)

driver.close()
print('Finished')