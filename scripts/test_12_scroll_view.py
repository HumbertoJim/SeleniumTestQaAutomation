# Test 12 - Scroll View
# ----------------------------------------------------------------------------------------------------------------------
# Selenium no puede interactuar con elementos que no estan visibles. Aun cuando estos elementos esten presentes en el DOM
# y se pueda obtener la referencia a ellos, cuando se trata de hacer click sobre estos, si el elemento no es visible,
# se generara un error. Una forma de solucionar esto es utilizando funciones para moverse en el documento. Estas funiones
# son scrollIntoView, que permite ir hacia un elemento; scrollBy, que realiza el movimiento a partir de la posicion actual;
# y scrollTo, que mueve hacia un punto especifico. Sin embargo, como las paginas pueden ser dinamicas y la posicion de un
# elemento podria variar, una buena practica es utilizar scrollIntoView

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from .library import links
import time

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service('dependencies/webdrivers/chromedriver.exe')
)

driver.get(links.PIXABAY)
driver.maximize_window()
time.sleep(2)

btn = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[1]/div[2]/div[2]/a/span")
driver.execute_script('arguments[0].scrollIntoView()', btn)
time.sleep(2)
driver.execute_script('window.scrollBy(0, -200)')
time.sleep(2)

btn.click()
time.sleep(2)

driver.close()
print('Finished')