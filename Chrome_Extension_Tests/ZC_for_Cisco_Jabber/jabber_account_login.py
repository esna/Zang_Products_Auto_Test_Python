'''
Created on Jun 19, 2017

@author: qcadmin
'''
import time
from selenium.webdriver.support.ui import Select
from Avaya_Communicator_for_Web import sso_login

pre_server = 'esna-imp11.esna.com'
med_server = 'esna-cucm11.esna.com'
password = '3snat3ch'

username_1 = 'dev1@esna.com'
username_2 = 'dev2@esna.com'

def select_sso_service(user_name, driver):
    def select_login_server():
        print "Begin to login jabber account"
        driver.switch_to_window(driver.window_handles[0])
        time.sleep(5)
        connect = Select(driver.find_element_by_id('jsc0'))
        connect.select_by_visible_text('Site default')
        print "Selected default site"
    def input_server_domain_name():
        pre_svr = driver.find_element_by_id('jsc1')
        pre_svr.clear()
        pre_svr.send_keys(pre_server)
        med_svr = driver.find_element_by_id('jsc2')
        med_svr.clear()
        med_svr.send_keys(pre_server)
        print "Input the presence and media server %s" % pre_server
    def input_user_credential():
        user_id = driver.find_element_by_id('jsc7')
        user_id.clear()
        user_id.send_keys(user_name)
        pswd = driver.find_element_by_id('jsc8')
        pswd.clear()
        pswd.send_keys(password)
        print "Account1 credendtials is input"
        time.sleep(1)
    def login_to_cisco_server():
        xpath = "//button[contains(.,'Connect')]"
        conn_btn = driver.find_element_by_xpath(xpath)
        conn_btn.click()
        print "Logged in to Cisco Server"
        time.sleep(5)
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
    login_to_cisco_server()
    return driver


def login_account_1(driver):
    select_sso_service(username_1, driver)
    print "Account 1 is logged in"
    time.sleep(2)
    return driver
    
def login_account_2(driver):
    select_sso_service(username_2, driver)
    print "Account 2 is logged in"
    time.sleep(2)
    return driver

# def login_account_1_o365(driver):
#     driver = select_sso_service(username_1, driver)
#     print "Account 1 is logged in"
#     time.sleep(2)
#     return driver
#     
# def login_account_2_o365(driver):
#     driver = select_sso_service(username_2, driver)
#     print "Account 2 is logged in"
#     time.sleep(2)
#     return driver
# 
# def login_account_1_salesforce(driver):
#     driver = select_sso_service(username_1, driver)
#     print "Account 1 is logged in"
#     time.sleep(2)
#     return driver
#     
# def login_account_2_salesforce(driver):
#     driver = select_sso_service(username_2, driver)
#     print "Account 2 is logged in"
#     time.sleep(2)
#     return driver


# login_account_1_google()
# login_account_2_google()
# login_account_1_o365()
# login_account_2_o365()
# login_account_1_salesforce()
# login_account_2_salesforce()
