'''
Created on Jun 30, 2017

@author: qcadmin
'''
import time
import create_repeat_meetings, edit_repeat_meetings
import verify_meeting_data_from_webex
import delete_repeat_meetings

url_mywebex = 'https://esna.webex.com/mw3200/mywebex/default.do?siteurl=esna&service=10'
driver = create_repeat_meetings.driver

create_repeat_meetings.go_to_google_mail_calendar()
create_repeat_meetings.create_repeat_meeging()
create_repeat_meetings.input_meeting_title()
create_repeat_meetings.set_meeting_schedule()
create_repeat_meetings.set_repeating_cycle()
create_repeat_meetings.save_meeting()
time.sleep(60)
    
verify_meeting_data_from_webex.webex_account_login()
verify_meeting_data_from_webex.verify_created_meeting_data()
    
edit_repeat_meetings.go_to_goolge_calendar()
edit_repeat_meetings.change_meeting_title()
edit_repeat_meetings.change_meeting_date_time()
edit_repeat_meetings.set_repeating_cycle()
edit_repeat_meetings.change_meeting_type_audio_with_webex_icon()
edit_repeat_meetings.save_edited_repeat_meetings()
time.sleep(30)
try:
    verify_meeting_data_from_webex.webex_account_login()
except:
    print "Webex account has already logged in"
verify_meeting_data_from_webex.verify_edited_meeting_data()
try:
    delete_repeat_meetings.webex_account_login()
except:
    print "Webex account has alreday logged in"
delete_repeat_meetings.delete_edited_repeat_meetings_from_webex_server()
delete_repeat_meetings.delete_repeat_meetings_from_google_calendar()
print "Tests ends"
driver.quit()