'''
Created on May 18, 2017

@author: qcadmin
'''

from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options

# os.chdir(r'D:\Chrome_Extension_Tests\iLink_for_Webex_Testing')
    #     print os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
# print dir_path
acw_file = dir_path + '\/avaya_1.0.17.1612.crx'
# acw_file = "D:\\Chrome_Extension_Tests\\Avaya_Communicator_for_Web\\avaya_1.0.17.1612.crx"
def add_chrome_extension():
    chop = webdriver.ChromeOptions()
    chop.add_extension(acw_file)
#     disable = webdriver.ChromeOptions.add_argument("--enable-save-password-bubble=false")
    driver = webdriver.Chrome(chrome_options=chop)
    time.sleep(5)
    driver.switch_to_window(driver.window_handles[-2])
    time.sleep(2)
    return driver
# driver = add_chrome_extension()


# def login_ext_with_Salesforce():
#     xpath = "//a[@id='preauth_sf']"
#     sf = driver.find_element_by_xpath(xpath)
#     sf.click()
#     time.sleep(3)
#     driver.switch_to_window(driver.window_handles[1])
#     sf_id = driver.find_element_by_id('username')
#     sf_id.clear()
#     sf_id.send_keys('arnoe@esna.com')
#     sf_pwd = driver.find_element_by_id('password')
#     sf_pwd.clear()
#     sf_pwd.send_keys('EsnaAvaya03')
#     login = driver.find_element_by_id('Login')
#     login.click()
#     time.sleep(3)
#     print "Click ALLOW button"
#     driver.find_element_by_id('oaapprove').click()
#     time.sleep(3)
#     driver.switch_to_window(driver.window_handles[0])
#     time.sleep(8)
    




