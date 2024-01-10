# Test 6 - Implicitly wait
# ----------------------------------------------------------------------------------------------------------------------
# Se introduce "implicitly wait", que consiste en el tiempo en que selenium estara intentando obtener los elementos.
# Esto es util cuando la pagina se carga gradualmente. Asi, en lugar de lanzar un error al inicio de la ejecucion
# del script porque no se ha encontrado un elemento, mejor se espera un momento con el fin de que el elemento
# sea cargado durante ese tiempo.

from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .library import data
import time



driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service('dependencies/webdrivers/chromedriver.exe')
)

driver.get('https://validaciones.rodrigovillanueva.com.mx/index.html')
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='nombre']").send_keys(data.get('name'))
driver.find_element(By.XPATH, "//input[@id='apellidos']").send_keys(data.get('lastname'))
driver.find_element(By.XPATH, "//input[@id='tel']").send_keys(data.get('phone'))
driver.find_element(By.XPATH, "//input[@id='email']").send_keys(data.get('email'))
driver.find_element(By.XPATH, "//input[@id='direccion']").send_keys(data.get('direction'))
driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.execute_script('window.scrollTo(0, 300)')

driver.find_element(By.ID, "error_id_not_found").click() # try to find the element until the implicitly wait time is exceeded, then throw an error

driver.close()
print('Finished')