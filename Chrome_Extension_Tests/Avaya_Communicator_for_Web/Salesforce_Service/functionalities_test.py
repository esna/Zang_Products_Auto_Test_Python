'''
Created on Jun 22, 2017

@author: qcadmin
'''

from Avaya_Communicator_for_Web import add_acw_extension
from Avaya_Communicator_for_Web import sso_login
from Avaya_Communicator_for_Web.acw_functionalities import user_presence
from Avaya_Communicator_for_Web.acw_functionalities import add_edit_delete_group
from Avaya_Communicator_for_Web import acw_account_login
from Avaya_Communicator_for_Web.acw_functionalities import settings

def login_acw_account_1():
    driver = add_acw_extension.add_chrome_extension()
    driver = sso_login.login_ext_with_google(driver)
    driver1 = acw_account_login.login_account_1_salesforce(driver)
    return driver1
driver = login_acw_account_1()

settings.settings_test(driver)
user_presence.presence_test(driver)
driver = add_edit_delete_group.group_test(driver)