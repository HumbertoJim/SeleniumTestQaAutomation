# Test 14 - Link tag
# ----------------------------------------------------------------------------------------------------------------------
# Se muestra como obtener la referencia de todos los elementos de un tag en especifico. Se muestra tambien como seleccionar
# un elemento por el texto que contenga un link. Particularmente, se ejemplifica la seleccion de un boton del menu de
# navegacion que desglosa un submenu.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from library.commons import Dependencies, Links
import time

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service(Dependencies.CHROME_DRIVER)
)

driver.get(Links.SELENIUM)
driver.maximize_window()

elems = driver.find_elements(By.TAG_NAME, 'a')
for elem in elems:
    print(elem.text)

driver.find_element(By.LINK_TEXT, 'About').click()

time.sleep(1)

driver.find_element(By.LINK_TEXT, 'About Selenium').click()
time.sleep(5)

driver.close()
print('Finished')