# Test 13 - Challenge
# ----------------------------------------------------------------------------------------------------------------------
# Codigo para superar el primer reto del curso, el cual consiste en aplicar todo lo aprendido para llenar todos los
# campos del formulario y enviarlo sin problemas. Dado que la pagina del reto original fue dado de baja, se utilizo otra
# pagina similar, en lo que a campos y tipos de campos se refiere.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from library.commons import Dependencies, Links, Data
import time

driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service(Dependencies.CHROME_DRIVER)
)
driver.get(Links.CHALLENGE_FORM)
driver.maximize_window()

try:
    name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='edit-contact-name']")))
    name.send_keys(Data.NAME)
    name.send_keys(
        Keys.TAB + Data.EMAIL +
        Keys.TAB + Data.PHONE +
        Keys.TAB + Data.ADDRESS +
        Keys.TAB + Data.ADDRESS +
        Keys.TAB + Data.CITY
    )

    state = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='edit-contact-state-province']")))
    state_select = Select(state)
    state_select.select_by_index(9) # supose to be California

    cp = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='edit-contact-postal-code']")))
    cp.send_keys(Data.CP)

    country = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='edit-contact-country']")))
    country_select = Select(country)
    country_select.select_by_visible_text('United States')

    resume_checkbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='edit-resume-method-paste']")))
    resume_checkbox.click()

    resume = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@id='edit-resume-text']")))
    resume.send_keys(Data.MESSAGE)

    btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@id='edit-submit'])[2]")))
    driver.execute_script('arguments[0].scrollIntoView()', btn)
    btn.click()

    driver.execute_script('window.scrollBy(0, 300)')
    time.sleep(5)

    driver.close()
except TimeoutException as e:
    print('Element not found:', e.msg)
    driver.quit()

print('Finished')