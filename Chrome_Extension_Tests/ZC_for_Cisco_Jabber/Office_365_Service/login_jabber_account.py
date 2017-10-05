'''
Created on Aug 28, 2017

@author: qcadmin
'''
import time
from ZC_for_Cisco_Jabber import add_jabber_extension
from ZC_for_Cisco_Jabber import sso_login
from ZC_for_Cisco_Jabber import jabber_account_login

def login_jabber_account_1():
    driver = add_jabber_extension.add_chrome_extension()
    driver = sso_login.login_ext_with_office365(driver)
    driver1 = jabber_account_login.login_account_1(driver)
    time.sleep(2)
    return driver1

def login_jabber_account_2():
    driver = add_jabber_extension.add_chrome_extension()
    driver = sso_login.login_ext_with_office365(driver)
    driver2 = jabber_account_login.login_account_2(driver)
    return driver2
 
# driver1 = login_jabber_account_1()
# time.sleep(2)

# driver1 = login_jabber_account_2()
# time.sleep(2)