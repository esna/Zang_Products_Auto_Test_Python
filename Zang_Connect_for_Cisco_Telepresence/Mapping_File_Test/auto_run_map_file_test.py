'''
Created on May 11, 2017

@author: qcadmin
'''
import Login_Gmail_Get_Calendar
import login_tms_server
import create_meeting_with_mapping_resource
import edit_meeting_with_mapping_resource
import verify_meeting_with_mapping_resource
import delete_edited_meeting_with_mapping
import time
 
driver = Login_Gmail_Get_Calendar.driver
Login_Gmail_Get_Calendar.login_gmail_account()
Login_Gmail_Get_Calendar.go_to_google_calendar()
  
create_meeting_with_mapping_resource.input_meeting_title()
create_meeting_with_mapping_resource.set_meeting_schedule()
create_meeting_with_mapping_resource.select_meeting_room()
create_meeting_with_mapping_resource.save_created_meeting()
time.sleep(90)

login_tms_server.login_tms_server()
verify_meeting_with_mapping_resource.verify_created_meeting_details()
time.sleep(2)
 
Login_Gmail_Get_Calendar.go_to_google_calendar()
edit_meeting_with_mapping_resource.change_meeting_title()
edit_meeting_with_mapping_resource.change_meeting_room()
edit_meeting_with_mapping_resource.save_created_meeting()
time.sleep(90)
 
login_tms_server.login_tms_server()
verify_meeting_with_mapping_resource.verify_edited_meeting_details()
time.sleep(2)
 
Login_Gmail_Get_Calendar.go_to_google_calendar()
delete_edited_meeting_with_mapping.locate_edited_meeting()
delete_edited_meeting_with_mapping.delete_edited_meeting()
time.sleep(90)

login_tms_server.login_tms_server()
verify_meeting_with_mapping_resource.verify_deleted_meeting()

print "Tests ended"
# driver.quit()








