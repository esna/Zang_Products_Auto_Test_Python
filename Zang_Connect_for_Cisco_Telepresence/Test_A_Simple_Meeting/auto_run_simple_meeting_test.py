'''
Created on May 11, 2017

@author: qcadmin
'''
'''
Created on May 11, 2017

@author: qcadmin
'''
import Login_Gmail_Get_Calendar
import login_tms_server
import create_a_simple_meeting
import edit_created_simple_meeting
import verify_created_edited_simple_meeting
import delete_edited_simple_meeting
import time

driver = Login_Gmail_Get_Calendar.driver
Login_Gmail_Get_Calendar.login_gmail_account()
Login_Gmail_Get_Calendar.go_to_google_calendar()
  
create_a_simple_meeting.input_meeting_title()
create_a_simple_meeting.set_meeting_schedule()
create_a_simple_meeting.select_meeting_room()
create_a_simple_meeting.save_created_meeting()
time.sleep(90)
  
login_tms_server.login_tms_server()
verify_created_edited_simple_meeting.verify_created_simple_meeting()
time.sleep(2)
 
Login_Gmail_Get_Calendar.go_to_google_calendar()
edit_created_simple_meeting.change_meeting_title()
edit_created_simple_meeting.change_meeting_room()
edit_created_simple_meeting.add_guests()
edit_created_simple_meeting.save_edited_meeting()
time.sleep(90)
 
login_tms_server.login_tms_server()
verify_created_edited_simple_meeting.verify_edited_simple_meeting()
time.sleep(2)

Login_Gmail_Get_Calendar.go_to_google_calendar()
delete_edited_simple_meeting.locate_edited_meeting()
delete_edited_simple_meeting.delete_edited_meeting()
time.sleep(90)
 
login_tms_server.login_tms_server()
verify_created_edited_simple_meeting.verify_deleted_meeting()

print "Tests ended"
driver.quit()








