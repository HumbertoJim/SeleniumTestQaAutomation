from selenium.webdriver.common.by import By
from library.commons import Data
from library.simplified import SeleniumWebDriver
from library.pages import AdminDemoNopCommercePage

def setup_function(function):
    global driver
    print(':: INI ::')
    driver = SeleniumWebDriver(implicitly_wait=2, explicitly_wait=2)
    page = AdminDemoNopCommercePage(driver)
    page.Login('admin@yourstore.com', 'admin')

def teardown_function(function):
    global driver
    driver.close()
    print(':: END ::')

def test_search_product():
    global driver
    driver.find_element("(//p[contains(.,'Catalog')])[1]").click()
    driver.find_element("(//p[contains(.,'Products')])[1]").click()
    driver.find_element("//input[@id='SearchProductName']").send_keys("Computer")
    driver.find_element("//button[@id='search-products']").click()

def test_create_product():
    global driver
    driver.find_element("(//p[contains(.,'Catalog')])[1]").click()
    driver.find_element("(//p[contains(.,'Products')])[1]").click()
    driver.find_element("//a[@href='/Admin/Product/Create']").click()
    driver.find_element("//input[@id='Name']").send_keys('Laptop Dell')
    driver.find_element("//textarea[@id='ShortDescription']").send_keys(Data.MESSAGE)
    driver.find_element("//span[contains(.,'File')]").click()
    driver.find_element("//div[@class='tox-collection__item-label'][contains(.,'New document')]").click()
    driver.switch_to_frame()
    driver.find_element('tinymce', by=By.ID).send_keys(Data.LOREM_IPSUM)
    driver.switch_to_default()
    driver.find_element("//input[@id='Sku']").send_keys('#29038445')
    driver.find_element("//button[@name='save']", offset_y=-100).click()
    msg = driver.find_element("//div[@class='alert alert-success alert-dismissable']").text
    assert 'The new product has been added successfully.' in msg

