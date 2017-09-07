'''
Created on Jun 30, 2017

@author: qcadmin
'''
import time
import create_repeat_meetings, edit_repeat_meetings
import verify_created_meeting_data
import verify_edited_meeting_data
import delete_edited_repeat_meetings

url_mywebex = 'https://esna.webex.com/mw3200/mywebex/default.do?siteurl=esna&service=10'
driver = create_repeat_meetings.driver

create_repeat_meetings.go_to_O365_calendar()
create_repeat_meetings.input_meeging_data_from_calendar()
create_repeat_meetings.create_meeting_from_webex_icon()
create_repeat_meetings.save_meeting_on_o365_calendar()
time.sleep(60)
    
verify_created_meeting_data.webex_account_login()
verify_created_meeting_data.verify_meeting_title()
verify_created_meeting_data.verify_meeting_time()
verify_created_meeting_data.verify_meeting_data_from_webex_icon()
       
edit_repeat_meetings.go_to_O365_calendar()
try:
    edit_repeat_meetings.locate_created_meeting()
except:
    xpath = "//button[@aria-label='NextWeek go to ']/span"
    driver.find_element_by_xpath(xpath).click()
    time.sleep(2)
    edit_repeat_meetings.locate_created_meeting()
edit_repeat_meetings.change_meeting_title()
edit_repeat_meetings.edit_meeting_date_time()
edit_repeat_meetings.change_repeat_cycle()
edit_repeat_meetings.edit_meeting_items_with_webex_icon()
edit_repeat_meetings.save_meeting_on_o365_calendar()
time.sleep(60)
  
try:
    verify_created_meeting_data.webex_account_login()
except:
    print "Webex account has already login"
verify_edited_meeting_data.verify_meeting_title()
verify_edited_meeting_data.verify_meeting_time()
verify_edited_meeting_data.verify_meeting_data_from_webex_icon()
 
delete_edited_repeat_meetings.delete_edited_repeat_meetings_from_webex_server()
delete_edited_repeat_meetings.delete_repeat_meetings_from_o365_calendar()
print "Tests ends"
# driver.quit()