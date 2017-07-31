'''
Created on May 11, 2017

@author: qcadmin
'''
import Login_Gmail_Get_Calendar
import login_tms_server
import create_webex_meeting
import edit_created_webex_meeting
import verify_webex_meeting_details
import delete_edited_webex_meeting
import time

driver = Login_Gmail_Get_Calendar.driver
Login_Gmail_Get_Calendar.login_gmail_account()
Login_Gmail_Get_Calendar.go_to_google_calendar()
    
create_webex_meeting.input_meeting_title()
create_webex_meeting.set_meeting_schedule()
create_webex_meeting.select_meeting_rooms()
create_webex_meeting.save_created_meeting()
time.sleep(90)
  
login_tms_server.login_tms_server()
verify_webex_meeting_details.verify_created_webex_meeting()
time.sleep(2)
   
Login_Gmail_Get_Calendar.go_to_google_calendar()
edit_created_webex_meeting.change_meeting_title()
edit_created_webex_meeting.change_meeting_schedule()
edit_created_webex_meeting.add_guests()
edit_created_webex_meeting.save_edited_meeting()
time.sleep(90)

login_tms_server.login_tms_server()

verify_webex_meeting_details.verify_edited_webex_meeting()
time.sleep(2)
   
Login_Gmail_Get_Calendar.go_to_google_calendar()
delete_edited_webex_meeting.locate_edited_webex_meeting()
delete_edited_webex_meeting.delete_edited_webex_meeting()
time.sleep(90)
  
login_tms_server.login_tms_server()
verify_webex_meeting_details.verify_deleted_webex_meeting()
 
print "Tests ended"
# driver.quit()








