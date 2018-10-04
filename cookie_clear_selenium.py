import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

def ClearCookies(): 
options = Options()
driver = webdriver.Chrome('chromedriver.exe')
driver.get('chrome://settings/clearBrowserData')
time.sleep(2)
elem = Select(driver.find_element_by_css_selector('* /deep/ #dropdownMenu'))
elem.select_by_index(2)   
time.sleep(2)           
result = driver.find_element_by_css_selector('* /deep/ #checkbox')
result.click()
time.sleep(2)
clear = driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')
clear.click()
time.sleep(2)
driver.close()

ClearCookies()
   
