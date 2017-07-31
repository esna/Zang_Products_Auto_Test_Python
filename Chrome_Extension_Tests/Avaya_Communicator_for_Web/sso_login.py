'''
Created on Jun 19, 2017

@author: qcadmin
'''
import time

google_id = 'reidz@esna.com'
google_pwd = 'Esnareid4'
o365_id = 'bryand@esnatech.onmicrosoft.com'
o365_pwd = '!esnatech1234$'
sf_id = 'arnoe@esna.com'
sf_pwd = 'EsnaAvaya06'

def login_ext_with_google(driver):
    xpath = "//a[@href='ws://'][@class='social google']/div"
    driver.find_element_by_xpath(xpath).click()
    time.sleep(2)
#     driver.switch_to_window(driver.window_handles[1])
#     driver.close()
    driver.switch_to_window(driver.window_handles[-1])
    time.sleep(2)
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
    time.sleep(2)
    return driver
    
def login_ext_with_office365(driver):
    driver.find_element_by_xpath("//a[@class='social office365']/div").click()
    time.sleep(1)
#     driver.switch_to_window(driver.window_handles[1])
#     driver.close()
    driver.switch_to_window(driver.window_handles[-1])
    time.sleep(5)
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
    return driver
    
def login_ext_with_Salesforce(driver):
    driver.find_element_by_xpath("//a[@class='social salesforce']/div").click()
    time.sleep(1)
#     driver.switch_to_window(driver.window_handles[1])
#     driver.close()
    driver.switch_to_window(driver.window_handles[-1])
    time.sleep(2)
    print "Go to Salesforce login interface"
    sf_username = driver.find_element_by_id('username')
    sf_username.clear()
    print 'userid is input'
    sf_username.send_keys(sf_id)
    sf_password = driver.find_element_by_id('password')
    sf_password.clear()
    print 'password is input'
    sf_password.send_keys(sf_pwd)
    login = driver.find_element_by_id('Login')
    login.click()
    time.sleep(3)
    print "Click ALLOW button"
    driver.find_element_by_id('oaapprove').click()
    time.sleep(3)
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(8)
    return driver
    
    
# login_ext_with_google()