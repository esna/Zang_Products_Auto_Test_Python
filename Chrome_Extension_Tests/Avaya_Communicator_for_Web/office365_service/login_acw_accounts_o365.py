'''
Created on Jun 19, 2017

@author: qcadmin
'''
from Avaya_Communicator_for_Web import add_acw_extension
from Avaya_Communicator_for_Web import acw_account_login
from Avaya_Communicator_for_Web import sso_login
import time

username_1 = 'Reidz@esna.com'
username_2 = 'Percyt@esna.com'


def login_acw_account_1():
    driver = add_acw_extension.add_chrome_extension()
    time.sleep(2)
    sso_login.login_ext_with_office365(driver)
    acw_account_login.ipoffice_login(driver, username_1)

def login_acw_account_2():
    driver = add_acw_extension.add_chrome_extension()
    time.sleep(2)
    sso_login.login_ext_with_office365(driver)
    acw_account_login.ipoffice_login(driver, username_2)


login_acw_account_1()
login_acw_account_2()

