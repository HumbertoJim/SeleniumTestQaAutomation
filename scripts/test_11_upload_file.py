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

from .library import links
import time

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service('dependencies/webdrivers/chromedriver.exe')
)

driver.get(links.IMAGE_FORM)
driver.maximize_window()
time.sleep(1)

try:
    file = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='659b84125da18-ii-input-file']")))
    file.send_keys('C:/Users/HUMBERTO/Documents/Github/SeleniumTestQaAutomation/files/image.png')
    print('Pass Image File')
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='659b84125da2c-brightness']").send_keys(100)
    print('Pass Brightness')
    time.sleep(2)
    btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Ajustar!')]")))
    print('Found Ajust Button')
    btn.click()
    print('Pass Ajust Button') 
except TimeoutException as e:
    print("Error, element not found: ", e.msg)

driver.execute_script('window.scrollTo(0, 300)')
time.sleep(4)

driver.close()
print('Finished')