'''
Created on Jun 22, 2017

@author: qcadmin
'''
from Avaya_Communicator_for_Web.acw_functionalities import user_presence
from Avaya_Communicator_for_Web.acw_functionalities import add_edit_delete_group
from Avaya_Communicator_for_Web.acw_functionalities import acw_account_login
from Avaya_Communicator_for_Web.acw_functionalities import settings

driver = acw_account_login.login_account_1_salesforce()

driver = user_presence.presence_test(driver)
add_edit_delete_group.group_test(driver)
settings.settings_test(driver)

