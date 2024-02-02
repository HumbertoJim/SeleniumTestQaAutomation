# Test 17 - Alert
# ----------------------------------------------------------------------------------------------------------------------
# Se muestra como abordar los alert: aceptarlos, cancelarlos e ingresar texto. Hay dos formas de obtener una referencia
# a estos, la primera es utilizando el expected_condition de alert_is_present, el segundo es utilizando el atributo switch_to.
# En el caso de chromedriver, este presenta un bug en el que el texto enviado no se muestra en el campo de texto del prompt.
# Sin embargo, este es un bug completamente visual, por lo que el texto, aunque no se vea, esta presente alli y puedes
# trabajar sin problemas.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from library.commons import Dependencies, Links, Data
import time

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service(Dependencies.CHROME_DRIVER)
)

driver.get(Links.ALERT_VALIDATION)
driver.maximize_window()

driver.find_element(By.XPATH, "//button[contains(.,'Click for JS Prompt')]").click()
alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
alert.send_keys(Data.MESSAGE)
time.sleep(2)
alert.accept()
time.sleep(2)

driver.find_element(By.XPATH, "//button[contains(.,'Click for JS Confirm')]").click()
alert = driver.switch_to.alert
time.sleep(2)
alert.dismiss()
time.sleep(2)

time.sleep(3)
driver.close()
print('Finished')