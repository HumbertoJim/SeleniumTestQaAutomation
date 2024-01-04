# Test 6 - Implicitly wait
# ----------------------------------------------------------------------------------------------------------------------
# Se introduce "implicit wait", que consiste en el tiempo en que selenium estara intentando obtener un elemento.
# Esto es util cuando la pagina se carga gradualmente. Asi, en lugar de lanzar un error al inicio de la ejecucion
# del script porque no se ha encontrado un elemento, mejor se espera un momento con el fin de que el elemento
# sea cargado durante ese tiempo.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .library import data, links
import time


driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service('dependencies/webdrivers/chromedriver.exe')
)

driver.get(links.DATACAMP)
driver.maximize_window()
driver.implicitly_wait(20)
#time.sleep(2)

btn = driver.find_element(By.XPATH, "//span[contains(.,'Iniciar chat')]")
print(btn.id)
btn.click()

driver.execute_script('window.scrollTo(0, 300)')
time.sleep(2)

driver.close()
print('Finished')