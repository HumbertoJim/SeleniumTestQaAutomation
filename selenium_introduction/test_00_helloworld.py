# Test 0 - Hello world
# ----------------------------------------------------------------------------------------------------------------------
# Script introductorio a Selenium. Abre una pagina en chrome, imprime su titulo y la cierra.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from library.commons import Dependencies
import time

driver = webdriver.Chrome(
    service=Service(Dependencies.CHROME_DRIVER),
    options=webdriver.ChromeOptions()
)

driver.get('https://docs.unity3d.com/Manual/index.html')

print('Bienvenido Selenium')
print(driver.title)

time.sleep(2)
driver.close()
print('Finished')
