from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

url = 'http://www.google.com'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)


