from Avaya_Communicator_for_Web import add_login_acw_extension
from selenium.webdriver.support.ui import Select
import time

driver = add_login_acw_extension.driver
pre_server = 'esnaipo.esna.com'
med_server = 'esnaipo.esna.com'
username_1 = 'Reidz@esna.com'
passwd_1 = '3snat3ch'

def login_acw_account_1():
    add_login_acw_extension.login_ext_with_google()
    time.sleep(2)
    print "Begin to login acw account"
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(2)
    
    print driver.title
    
    connect = Select(driver.find_element_by_id('jsc0'))
    connect.select_by_value('Site default')
    
#     auth = Select(driver.find_element_by_id('jsc1'))
#     auth.select_by_value('Use explicit credentials')
#     pre_svr = driver.find_element_by_id('jsc2')
#     pre_svr.clear()
#     pre_svr.send_keys(pre_server)
#     med_svr = driver.find_element_by_id('jsc3')
#     med_svr.clear()
#     med_svr.send_keys(pre_server)
#     user_id = driver.find_element_by_id('jsc4')
#     user_id.clear()
#     user_id.send_keys(username_1)
#     pswd = driver.find_element_by_id('jsc5')
#     pswd.clear()
#     pswd.send_keys(passwd_1)
#     xpath = "//button[contains(.,'Connect')]"
#     conn_btn = driver.find_element_by_xpath(xpath)
#     conn_btn.click()
    
    
login_acw_account_1()
    