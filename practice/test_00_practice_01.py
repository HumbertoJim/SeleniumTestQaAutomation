from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from library.commons import Dependencies, Links
import time

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=webdriver.ChromeService(Dependencies.CHROME_DRIVER)
)

driver.get(Links.UNITY)
driver.maximize_window()
driver.implicitly_wait(5)

search = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='q']"))
)
search.send_keys('Networking')
search.send_keys(Keys.ENTER)

time.sleep(2)

element = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[1]/div[4]/div[1]/a"))
)
element.click()

time.sleep(20)
driver.close()
print('Finished')