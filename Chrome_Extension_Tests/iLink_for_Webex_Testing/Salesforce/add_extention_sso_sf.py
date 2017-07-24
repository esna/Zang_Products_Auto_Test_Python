'''
Created on Jul 24, 2017

@author: qcadmin
'''
import add_login_webex_extension
import time

driver = add_login_webex_extension.driver
add_login_webex_extension.login_ext_with_Salesforce()
add_login_webex_extension.input_esna_webex_password()
time.sleep(5)