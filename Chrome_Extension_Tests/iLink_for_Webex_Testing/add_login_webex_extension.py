'''
Created on May 18, 2017

@author: qcadmin
'''

from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options

google_id = 'reidz@esna.com'
google_pwd = 'Esnareid4'
o365_id = 'bryand@esnatech.onmicrosoft.com'
o365_pwd = '!esnatech1234$'
webex_pwd = 'Zang123!'
# os.chdir(r'D:\Chrome_Extension_Tests\iLink_for_Webex_Testing')
    #     print os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
# print dir_path
webex_file = dir_path + '\wcl_9.1.17.1626.crx'

def add_chrome_extension():
    chop = webdriver.ChromeOptions()
    chop.add_extension(webex_file)
#     disable = webdriver.ChromeOptions.add_argument("--enable-save-password-bubble=false")
    driver = webdriver.Chrome(chrome_options=chop)
    time.sleep(5)
    driver.switch_to_window(driver.window_handles[-2])
    driver.close()
    time.sleep(3)
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(3)
    return driver
driver = add_chrome_extension()

def login_ext_with_google():
    xpath = "//a[@id='preauth_ggl']"
    google_link = driver.find_element_by_xpath(xpath)
    google_link.click()
    time.sleep(5)
    driver.switch_to_window(driver.window_handles[1])
    print "Go to gmail login interface"
    email = driver.find_element_by_id("identifierId")
    email.clear()
    email.send_keys(google_id)
    print "User id is input"
    time.sleep(1)
    xpath = "//div[@id='identifierNext']/content/span"
    next_btn = driver.find_element_by_xpath(xpath)
    next_btn.click()
    print "Click next"
    time.sleep(3)
    Passwd = driver.find_element_by_name("password")
    Passwd.clear()
    Passwd.send_keys(google_pwd)
    print "User password is input"
    xpath = "//div[@id='passwordNext']/content/span"
    next_btn = driver.find_element_by_xpath(xpath)
    next_btn.click()
    print "Gmail account is logged in"
    time.sleep(5)
    print "Click ALLOW button"
    xpath = "//span[contains(.,'ALLOW')]"
    driver.find_element_by_xpath(xpath).click()
    time.sleep(3)
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(3)
    
def login_ext_with_office365():
    xpath = "//a[@id='preauth_office365']"
    o365_link = driver.find_element_by_xpath(xpath)
    o365_link.click()
    time.sleep(5)
    driver.switch_to_window(driver.window_handles[1])
    print "Go to office 365 login interface"
    email = driver.find_element_by_id("cred_userid_inputtext")
    email.clear()
    email.send_keys(o365_id)
    print "User id is input"
    time.sleep(2)
    Passwd = driver.find_element_by_id("cred_password_inputtext")
    Passwd.clear()
    Passwd.send_keys(o365_pwd)
    print "User password is input"
    signin_btn = driver.find_element_by_id('cred_sign_in_button')
    signin_btn.click()
    print "Office 365 account is logged in"
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(10)
    
def login_ext_with_Salesforce():
    xpath = "//a[@id='preauth_sf']"
    sf = driver.find_element_by_xpath(xpath)
    sf.click()
    time.sleep(3)
    driver.switch_to_window(driver.window_handles[1])
    sf_id = driver.find_element_by_id('username')
    sf_id.clear()
    sf_id.send_keys('arnoe@esna.com')
    sf_pwd = driver.find_element_by_id('password')
    sf_pwd.clear()
    sf_pwd.send_keys('EsnaAvaya03')
    login = driver.find_element_by_id('Login')
    login.click()
    time.sleep(3)
    print "Click ALLOW button"
    driver.find_element_by_id('oaapprove').click()
    time.sleep(3)
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(8)
    
def input_esna_webex_password():
    pwd = driver.find_element_by_xpath("//input[@id='txtSec']")
    pwd.send_keys(webex_pwd)
    print "Input webex passowrd"
    time.sleep(2)
    driver.find_element_by_id('chkSec').click()
    print "Check Save Password option"
    driver.find_element_by_xpath("//button[@id='buttonApply']").click()
    print "Click Save button"
    time.sleep(5)
    print "Webex credentila is saved"



# login_ext_with_google()
# login_ext_with_office365()
# login_ext_with_Salesforce()
# input_esna_webex_password()


