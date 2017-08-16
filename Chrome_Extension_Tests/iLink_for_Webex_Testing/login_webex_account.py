'''
Created on Jun 30, 2017

@author: qcadmin
'''
from selenium import webdriver
import time

url_mywebex = 'https://esna.webex.com/mw3200/mywebex/default.do?siteurl=esna&service=10'

def webex_account_login(driver):
        driver.get(url_mywebex)
        time.sleep(2)
        driver.switch_to_frame('mainFrame')
        user_id = driver.find_element_by_id('mwx-ipt-username')
        user_id.click()
        user_id.send_keys('reidz')
        print "Input user id"
        passwd = driver.find_element_by_id('mwx-ipt-password')
        passwd.click()
        passwd.send_keys('Zang123!')
        time.sleep(2)
        print "Input password"
        driver.find_element_by_id('mwx-btn-logon').click()
        print "Webex account is logged in"
        time.sleep(2)
        return driver
        
# webex_account_login()