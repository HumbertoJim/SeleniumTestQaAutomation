# Test 15 - Link Tag MouseHover
# ----------------------------------------------------------------------------------------------------------------------
# Hay ocasiones en las que interactuar con los elementos del menu de navegacion puede resultar mas complejo, en el
# sentido de que el cursor del mouse debe estar posicionado sobre el elemento para desglosar un submenu, o de lo,
# el submenu se cierra. Cuando este es el caso, hacer un click sobre el boton no es suficiente. Es necesario emplear
# ActionsChains, que provee funciones especificas para estos casos donde se require automatizar que el mouse se
# mueva sobre un elemento y, asi, desglose el submenu sin que este desaparezca.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from .library import links
import time


driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service('dependencies/webdrivers/chromedriver.exe')
)

driver.get(links.CHALLENGE_FORM)
driver.maximize_window()

elems = driver.find_elements(By.TAG_NAME, 'a')
for elem in elems:
    print(elem.text)

btn = driver.find_element(By.LINK_TEXT, "Prácticas")
a = ActionChains(driver)

a.move_to_element(btn).perform()
btn2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Calculo de Edad")))
a.move_to_element(btn2).click().perform()

driver.execute_script('window.scrollTo(0, 300)')
time.sleep(5)

driver.close()
print('Finished')