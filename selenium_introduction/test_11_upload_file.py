# Test 11 - Upload File
# ----------------------------------------------------------------------------------------------------------------------
# En este script se carga una imagen a una pagina para cambiar la intensidad de su brillo. Para cargar el archivo,
# basta con indicar la ruta en el campo del formulario. En ocasiones, pasa un error debido a que la pagina nunca deja de
# cargar sus componentes. Una causa podria ser el internet y otra los anuncios que tiene.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from library.commons import Dependencies, Files, Links
import time

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service(Dependencies.CHROME_DRIVER)
)

driver.get(Links.IMAGE_FORM)
driver.maximize_window()
time.sleep(1)

try:
    file = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='upload']")))
    print(Files.Images.TEST)
    file.send_keys(Files.Images.TEST)
    print('Pass Image File')
    time.sleep(2)
    btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='go']")))
    print('Found Button')
    btn.click()
    print('Pass Button') 
except TimeoutException as e:
    print("Error, element not found: ")

driver.execute_script('window.scrollTo(0, 300)')
time.sleep(4)

driver.close()
print('Finished')