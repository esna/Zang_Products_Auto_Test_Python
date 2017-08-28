'''
Created on Aug 28, 2017

@author: qcadmin
'''
import time
from Avaya_Communicator_for_Web import add_acw_extension
from Avaya_Communicator_for_Web import sso_login
from Avaya_Communicator_for_Web import acw_account_login

def login_acw_account_1():
    driver = add_acw_extension.add_chrome_extension()
    driver = sso_login.login_ext_with_google(driver)
    driver1 = acw_account_login.login_account_1(driver)
    time.sleep(2)
    return driver1

def login_acw_account_2():
    driver = add_acw_extension.add_chrome_extension()
    driver = sso_login.login_ext_with_google(driver)
    driver2 = acw_account_login.login_account_2(driver)
    return driver2
 
# driver1 = login_acw_account_1()
# time.sleep(2)
#  
# driver2 = login_acw_account_2()
# time.sleep(2)