'''
Created on Jun 22, 2017

@author: qcadmin
'''
from Avaya_Communicator_for_Web.acw_functionalities import user_presence
from Avaya_Communicator_for_Web.acw_functionalities import acw_account_login

driver = acw_account_login.login_account_1_google()
user_presence.presence_test(driver)

