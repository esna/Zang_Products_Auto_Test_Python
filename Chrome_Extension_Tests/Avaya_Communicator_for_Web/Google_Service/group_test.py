'''
Created on Jun 22, 2017

@author: qcadmin
'''
from Avaya_Communicator_for_Web.acw_functionalities import add_edit_delete_group
from Avaya_Communicator_for_Web.acw_functionalities import acw_account_login

driver = acw_account_login.login_account_1_google()
add_edit_delete_group.group_test(driver)
