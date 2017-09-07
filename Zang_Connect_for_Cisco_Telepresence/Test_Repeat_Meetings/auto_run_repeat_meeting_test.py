'''
Created on May 11, 2017

@author: qcadmin
'''
import Login_Gmail_Get_Calendar
import login_tms_server
import create_repeat_meetings
import edit_created_repeat_meetings
import verify_created_edited_repeat_meetings
import delete_edited_repeat_meeting
import time

driver = Login_Gmail_Get_Calendar.driver

# Login_Gmail_Get_Calendar.login_gmail_account()
# Login_Gmail_Get_Calendar.go_to_google_calendar()
# create_repeat_meetings.input_meeting_title()
# create_repeat_meetings.set_meeting_schedule()
# create_repeat_meetings.set_repeating_cycle()
# create_repeat_meetings.select_meeting_rooms()
# create_repeat_meetings.add_guests()
# create_repeat_meetings.save_created_meeting()
# time.sleep(90)
#                 
# login_tms_server.login_tms_server()
# verify_created_edited_repeat_meetings.verify_created_repeat_meeting()
# time.sleep(2)
     
# Login_Gmail_Get_Calendar.login_gmail_account()
# Login_Gmail_Get_Calendar.go_to_google_calendar()
# edit_created_repeat_meetings.change_meeting_title()
# edit_created_repeat_meetings.change_meeting_time()
# edit_created_repeat_meetings.change_meeting_room()
# edit_created_repeat_meetings.save_edited_meeting()
# time.sleep(90)
        
login_tms_server.login_tms_server()
verify_created_edited_repeat_meetings.verify_edited_repeat_meetings()
time.sleep(2)
   
Login_Gmail_Get_Calendar.login_gmail_account()
Login_Gmail_Get_Calendar.go_to_google_calendar()
delete_edited_repeat_meeting.locate_edited_meeting()
delete_edited_repeat_meeting.delete_edited_meeting()
time.sleep(90)
      
login_tms_server.login_tms_server()
verify_created_edited_repeat_meetings.verify_deleted_meeting()
   
print "Tests ended"
# driver.quit()