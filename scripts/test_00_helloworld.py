# Test 0 - Hello world
# ----------------------------------------------------------------------------------------------------------------------
# Script introductorio a Selenium. Abre una pagina en chrome, imprime su titulo y la cierra.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(
    service=Service('dependencies/webdrivers/chromedriver.exe'),
    options=webdriver.ChromeOptions()
)

driver.get('https://docs.unity3d.com/Manual/index.html')

print('Bienvenido Selenium')
print(driver.title)

driver.close()

