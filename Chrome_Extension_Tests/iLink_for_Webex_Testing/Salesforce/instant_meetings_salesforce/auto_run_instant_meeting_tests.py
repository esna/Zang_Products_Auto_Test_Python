'''
Created on Jul 25, 2017

@author: qcadmin
'''
import create_inst_mt_from_webex_icon
create_inst_mt_from_webex_icon.create_inst_meeting_from_webex_icon()
           
import create_inst_mt_from_sf_contacts
create_inst_mt_from_sf_contacts.create_inst_mt_from_contact_classic()
create_inst_mt_from_sf_contacts.create_inst_mt_from_contact_lightning()
         
import verify_instant_meeting_data
try:
    verify_instant_meeting_data.webex_account_login()
except:
    print "Webex account has logged in"
verify_instant_meeting_data.verify_meeting_data()

import delete_instant_meeting_from_webex
delete_instant_meeting_from_webex.delete_created_instant_meeting()