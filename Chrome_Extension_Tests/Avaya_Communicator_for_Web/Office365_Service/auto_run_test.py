'''
Created on Jun 22, 2017

@author: qcadmin
'''

import login_acw_account
import settings
import user_presence
import group_test
import get_available_contact
import contact_actions_test
import message_and_call

driver1 = login_acw_account.login_acw_account_1()
# driver2 = login_acw_account.login_acw_account_2()

# settings.settings_test(driver1)
# user_presence.presence_test(driver1)
group_test.group_test(driver1)
# get_available_contact.add_get_available_contact(driver1)
# contact_actions_test.contact_actions(driver1)
# message_and_call.messages_and_calls(driver1)