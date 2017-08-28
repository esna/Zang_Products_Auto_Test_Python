'''
Created on Jun 22, 2017

@author: qcadmin
'''

import login_acw_account
import settings
import user_presence
import group_test
import interact_activities

driver1 = login_acw_account.login_acw_account_1()
driver2 = login_acw_account.login_acw_account_2()

# settings.settings_test(driver1)
# user_presence.presence_test(driver1)
# group_test.group_test(driver1)
interact_activities.messages_call_actions(driver1, driver2)