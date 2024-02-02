# Test 10 - Exceptions
# ----------------------------------------------------------------------------------------------------------------------
# Se combina el uso de WebDriverWait para explicitly waits, junto con manejo de excepciones. Esta practica es
# recomendada, con el fin de determinar que hacer cuando un elemento no es encontrado.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from library.commons import Dependencies, Data, Links
import time

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service(Dependencies.CHROME_DRIVER)
)

driver.get(Links.COMBOBOX_FORM)
driver.maximize_window()

try:
    elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(  (By.XPATH, "//select[@id='comboBox1']") ))
    select = Select(elem)
    select.select_by_index(1)
except TimeoutException as e:
    print("Error, element not found: ", e)

try:
    elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'comboBox2')))
    select = Select(elem)
    select.select_by_index(1)
    select.select_by_index(2)
    select.select_by_index(4)
except TimeoutException as e:
    print("Error, element not found: ", e)

try:
    elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'os')))
    select = Select(elem)
    select.select_by_index(1)
except TimeoutException as e:
    print("Error, element not found: ", e)

try:
    elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'version')))
    select = Select(elem)
    select.select_by_index(3)
except TimeoutException as e:
    print("Error, element not found: ", e)

try:
    elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][contains(.,'Enviar')]")))
    elem.click()
except TimeoutException as e:
    print("Error, element not found: ", e)

driver.execute_script('window.scrollTo(0, 300)')
time.sleep(5)

driver.close()
print('Finished')