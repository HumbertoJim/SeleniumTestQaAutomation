# Test 9 - Combobox
# ----------------------------------------------------------------------------------------------------------------------
# Ejemplo de como interactuar con selects y multi selects. Para esto, se utiliza un componente especial llamado Select.
# En el caso de Multiselect, parece ser que el indice de los elementos van de 0 a n-1. En los otros casos va de 1 hasta n.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from library.commons import Dependencies, Data, Links
import time

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service(Dependencies.CHROME_DRIVER)
)

driver.get(Links.COMBOBOX_FORM)
driver.maximize_window()

# Select
select1 = Select(driver.find_element(By.XPATH, "//select[@id='comboBox1']"))
select1.select_by_index(2)
time.sleep(1)
select1.select_by_value('4')
time.sleep(1)
select1.select_by_visible_text('Valor 5')
time.sleep(1)

# Multi Select
select2 = Select(driver.find_element(By.ID, 'comboBox2'))
select2.select_by_index(1)
select2.select_by_index(3)
select2.select_by_index(4)
time.sleep(2)

# Select SO
select3 = Select(driver.find_element(By.ID, 'os'))
select3.select_by_index(2)
time.sleep(2)

# Select Version
select4 = Select(driver.find_element(By.ID, 'version'))
select4.select_by_index(3)
time.sleep(2)

# Send
driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Enviar')]").click()
driver.execute_script('window.scrollTo(0, 300)')
time.sleep(5)

driver.close()
print('Finished')