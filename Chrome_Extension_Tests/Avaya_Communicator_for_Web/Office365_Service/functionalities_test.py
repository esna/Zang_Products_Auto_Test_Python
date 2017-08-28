'''
Created on Jun 22, 2017

@author: qcadmin
'''

import time
from Avaya_Communicator_for_Web import add_acw_extension
from Avaya_Communicator_for_Web import sso_login
from Avaya_Communicator_for_Web import acw_account_login
from Avaya_Communicator_for_Web.acw_functionalities import user_presence
from Avaya_Communicator_for_Web.acw_functionalities import add_edit_delete_group
from Avaya_Communicator_for_Web.acw_functionalities import settings
from Avaya_Communicator_for_Web.acw_functionalities import interact_activities

# def login_acw_account_1():
#     driver = add_acw_extension.add_chrome_extension()
#     driver = sso_login.login_ext_with_office365(driver)
#     driver1 = acw_account_login.login_account_1(driver)
#     time.sleep(2)
#     return driver1

def login_acw_account_2():
    driver = add_acw_extension.add_chrome_extension()
    driver = sso_login.login_ext_with_office365(driver)
    driver2 = acw_account_login.login_account_2(driver)
    time.sleep(2)
    return driver2

# driver1 = login_acw_account_1()
# time.sleep(2)

driver2 = login_acw_account_2()
time.sleep(2)

# settings.settings_test(driver1)
# user_presence.presence_test(driver1)
add_edit_delete_group.group_test(driver2)
# interact_activities.messages_call_actions(driver1, driver2)