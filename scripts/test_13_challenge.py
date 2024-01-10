# Test 13 - Challenge
# ----------------------------------------------------------------------------------------------------------------------
# Codigo para superar el primer reto del curso. Dado que la pagina del reto original fue dado de baja, se utilizo otra
# pagina similar, en lo que a campos y tipos de campos se refiere.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from .library import links, data
import time


driver = webdriver.Chrome(
    options=webdriver.ChromeOptions(),
    service=Service('dependencies/webdrivers/chromedriver.exe')
)

driver.get(links.CHALLENGE_FORM)
driver.maximize_window()

try:
    name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='edit-contact-name']")))
    name.send_keys(data.get('name'))
    name.send_keys(
        Keys.TAB + data.get('email') +
        Keys.TAB + data.get('phone') +
        Keys.TAB + data.get('direction') +
        Keys.TAB + data.get('direction') +
        Keys.TAB + data.get('city')
    )

    state = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='edit-contact-state-province']")))
    state_select = Select(state)
    state_select.select_by_index(9) # supose to be California

    cp = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='edit-contact-postal-code']")))
    cp.send_keys(data.get('cp'))

    country = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='edit-contact-country']")))
    country_select = Select(country)
    country_select.select_by_visible_text('United States')

    resume_checkbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='edit-resume-method-paste']")))
    resume_checkbox.click()

    resume = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@id='edit-resume-text']")))
    resume.send_keys(data.get('message'))

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