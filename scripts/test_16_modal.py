# Test 16 - Modal
# ----------------------------------------------------------------------------------------------------------------------
# Se muestra como trabajar con modales, generalmente se utiliza lo que ya se ha aprendido. Nada nuevo.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .library import links, data
import time


driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service('dependencies/webdrivers/chromedriver.exe')
)

driver.get(links.MODAL_FORM)
driver.maximize_window()

driver.find_element(By.XPATH, "//button[contains(.,'Agregar Registro')]").click()

WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='nombre']")))
driver.find_element(By.XPATH, "//input[@id='nombre']").send_keys(data.get('name'))
driver.find_element(By.XPATH, "//input[@id='apellidos']").send_keys(data.get('lastname'))
driver.find_element(By.XPATH, "//input[@id='telefono']").send_keys(data.get('phone'))

time.sleep(1)

driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Enviar')]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//button[contains(@data-dismiss,'modal')]").click()
time.sleep(5)

driver.close()
print('Finished')