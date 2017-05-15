'''
Created on May 9, 2017

@author: qcadmin
'''
import time
import signal
import Login_Gmail_Get_Calendar
import create_webex_meeting
import edit_meeting_with_mapping_resource

driver = Login_Gmail_Get_Calendar.driver
new_title = edit_meeting_with_mapping_resource.new_title
google_res_room = edit_meeting_with_mapping_resource.google_res_room2
meeting_room_1 = create_webex_meeting.meeting_room_1

def locate_edited_webex_meeting():
    try:
        xpath = "//div[@class='cpchip']/span[contains(., '%s')]" % meeting_room_1
        driver.find_element_by_xpath(xpath)
        edt_meeting = driver.find_element_by_xpath(xpath)
        print "Found the edited meeting"
        edt_meeting.click()
        print "Meeting link is clicked"
        time.sleep(2)
    except:
        print 'The edited meeting is not found'
        driver.close()
        driver.service.process.send_signal(signal.SIGTERM)
    
def delete_edited_webex_meeting():
    driver.switch_to_active_element()
    xpath = "//div[@class='neb-footer']/span[2]/div[1]"
    del_btn = driver.find_element_by_xpath(xpath)
    del_btn.click()
    driver.switch_to_active_element()
    try:
        confirm_btn = driver.find_element_by_name("no")
        confirm_btn.click()
        print "The simple meeting is deleted from google calendar"
    except:
        print "The simple meeting is deleted from google calendar"
        
    

if __name__ == '__main__':
    
    Login_Gmail_Get_Calendar.login_gmail_account()
    Login_Gmail_Get_Calendar.go_to_google_calendar()
    locate_edited_webex_meeting()
    delete_edited_webex_meeting()
    driver.quit()
