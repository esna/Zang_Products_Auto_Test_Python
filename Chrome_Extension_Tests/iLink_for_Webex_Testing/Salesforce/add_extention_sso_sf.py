'''
Created on Jul 24, 2017

@author: qcadmin
'''
import add_login_webex_extension
import time

def extenstion_and_sso():
    driver = add_login_webex_extension.driver
    try:
        add_login_webex_extension.login_ext_with_Salesforce()
        add_login_webex_extension.input_esna_webex_password()
    except:
        print "sso has executed"
    time.sleep(5)
    return driver