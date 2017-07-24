'''
Created on Jun 19, 2017

@author: qcadmin
'''
import time
from selenium.webdriver.support.ui import Select
from Avaya_Communicator_for_Web import sso_login

pre_server = 'esnaipo.esna.com'
med_server = 'esnaipo.esna.com'
password = '3snat3ch'

username_1 = 'Reidz@esna.com'
username_2 = 'Percyt@esna.com'
ser_name_1 = 'google'
ser_name_2 = 'o365'
ser_name_3 = 'salesforce'

def select_sso_service(ser_name, user_name, driver):
#     if ser_name == 'google':
#         driver = sso_login.login_ext_with_google(driver)
#     elif ser_name == 'o365':
#         driver = sso_login.login_ext_with_office365()
#     elif ser_name == 'salesforce':
#         driver = sso_login.login_ext_with_Salesforce()
#     else:
#         print "SSO service name is wrong"

    def select_login_server():
        print "Begin to login acw account"
        driver.switch_to_window(driver.window_handles[0])
        time.sleep(5)
        connect = Select(driver.find_element_by_id('jsc0'))
        connect.select_by_visible_text('Site default')
        print "Selected default site"
        auth = Select(driver.find_element_by_id('jsc1'))
        auth.select_by_value('User')
    def input_server_domain_name():
        pre_svr = driver.find_element_by_id('jsc2')
        pre_svr.clear()
        pre_svr.send_keys(pre_server)
        med_svr = driver.find_element_by_id('jsc3')
        med_svr.clear()
        med_svr.send_keys(pre_server)
        print "Input the presence and media server %s" % pre_server
    def input_user_credential():
        user_id = driver.find_element_by_id('jsc4')
        user_id.clear()
        user_id.send_keys(user_name)
        pswd = driver.find_element_by_id('jsc5')
        pswd.clear()
        pswd.send_keys(password)
        print "Account1 credendtials is input"
        time.sleep(1)
    def login_to_ipoffice():
        xpath = "//button[contains(.,'Connect')]"
        conn_btn = driver.find_element_by_xpath(xpath)
        conn_btn.click()
        print "Login to IPOffice"
        time.sleep(2)
        try:
            xpath = "//a[contains(.,'Skip tutorial')]"
            driver.find_element_by_xpath(xpath).click()
            print "Account logged in, skipped tutorial"
        except:
            print "Account logged in, tutorial is not popped up"
    try:
        select_login_server()
        print "Site is selected."
    except:
        print "No need to select site"
        
    try:
        input_server_domain_name()
        print "Server domain is input"
    except:
        print "No need to input server domain"
    input_user_credential()
    login_to_ipoffice()
    return driver


def login_account_1_google(driver):
    select_sso_service(ser_name_1, username_1, driver)
    print "Account 1 is logged in"
    time.sleep(2)
    return driver
    
def login_account_2_google(driver):
    select_sso_service(ser_name_1, username_2, driver)
    print "Account 2 is logged in"
    time.sleep(2)
    return driver

def login_account_1_o365():
    driver = select_sso_service(ser_name_2, username_1)
    print "Account 1 is logged in"
    time.sleep(2)
    return driver
    
def login_account_2_o365():
    driver = select_sso_service(ser_name_2, username_2)
    print "Account 2 is logged in"
    time.sleep(2)
    return driver

def login_account_1_salesforce():
    driver = select_sso_service(ser_name_3, username_1)
    print "Account 1 is logged in"
    time.sleep(2)
    return driver
    
def login_account_2_salesforce():
    driver = select_sso_service(ser_name_3, username_2)
    print "Account 2 is logged in"
    time.sleep(2)
    return driver


# login_account_1_google()
# login_account_2_google()
# login_account_1_o365()
# login_account_2_o365()
# login_account_1_salesforce()
# login_account_2_salesforce()
