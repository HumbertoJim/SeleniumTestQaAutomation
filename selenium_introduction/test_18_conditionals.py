# Test 18 - Conditionals
# ----------------------------------------------------------------------------------------------------------------------
# En este apartado se muestra como validar si un elemento esta presente o habilitado en la pagina. Esto podria ser
# util para verificar si la pagina que estamos visitando es realmente la pagina que queremos, o bien para esperar
# hasta que un elemento se habilite.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from library.commons import Dependencies, Links
import time

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service(Dependencies.CHROME_DRIVER)
)

driver.get(Links.UNICARIBE)
driver.maximize_window()

logo = driver.find_element(By.XPATH, "//*[@id='logo-ucaribe']")
if logo.is_displayed():
    print('Imagen existe')
    time.sleep(2)
    btn = driver.find_element(By.XPATH, "//a[@href='http://blog.unicaribe.mx/']")
    if btn.is_enabled():
        print('Boton activo')
        time.sleep(2)
        btn.click()
    else:
        print('Boton no activo')
else:
    print('Elemento no existe')
    

time.sleep(5)
driver.close()
print('Finished')
