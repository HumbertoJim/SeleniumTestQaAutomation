# Test 7 - Explicitly wait
# ----------------------------------------------------------------------------------------------------------------------
# Se introduce "explicitly wait", que consiste en el tiempo en que selenium estara intentando obtener un elemento.
# Funciona de forma similar que el implicitly wait, solo que explicitly time se aplica unicamente a un elemento de interes.
# De acuerdo a Rodrigo Villanueva, es mejor utilizar explicitly wait.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .library import links, data
import time

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service('dependencies/webdrivers/chromedriver.exe')
)

driver.get(links.SELENIUM_DYNAMIC)
driver.maximize_window()
# driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//input[@id='adder']").click()

# Example - Get elements that does not exist in the DOM
# field = driver.find_element(By.XPATH, "//div[@id='box0']") # throw an error without implicitly time
box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[@id='box0']")
    )
)
print('Founded:', box)

# Example - Get elements that does exist in the DOM but there are no visible
driver.find_element(By.ID, 'reveal').click()
field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, 'revealed')
    )
)
field.send_keys(data.get('message'))

time.sleep(5)

driver.close()
print('Finished')