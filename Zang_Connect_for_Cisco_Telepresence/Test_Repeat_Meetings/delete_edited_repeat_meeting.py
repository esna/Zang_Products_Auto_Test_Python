'''
Created on May 11, 2017

@author: qcadmin
'''
'''
Created on May 11, 2017

@author: qcadmin
'''
import time
import Login_Gmail_Get_Calendar
import edit_created_repeat_meetings

driver = Login_Gmail_Get_Calendar.driver
new_mt_room_1 = edit_created_repeat_meetings.new_mt_room_1
new_mt_room_2 = edit_created_repeat_meetings.new_mt_room_2

def locate_edited_meeting():
    try:
        xpath = "//div[@class='cpchip']/span[contains(., '%s')]" % new_mt_room_2
        driver.find_element_by_xpath(xpath)
        edt_meeting = driver.find_element_by_xpath(xpath)
        print "Found the edited meeting"
        edt_meeting.click()
        print "Meeting link is clicked"
        time.sleep(2)
    except:
        try:
            xpath = "//div[@class='cpchip']/span[contains(., '%s')]" % new_mt_room_1
            driver.find_element_by_xpath(xpath)
            edt_meeting = driver.find_element_by_xpath(xpath)
            print "Found the edited meeting"
            edt_meeting.click()
            print "Meeting link is clicked"
            time.sleep(2)
        except:
            print 'The edited meeting is not found'
            driver.quit()
    
def delete_edited_meeting():
    driver.switch_to_active_element()
    xpath = "//div[@class='neb-footer']/span[2]/div[1]"
    del_btn = driver.find_element_by_xpath(xpath)
    del_btn.click()
    time.sleep(2)
    try:
        xpath = "//div[@role='button']//div[contains(.,'All events in the series')]"
        confirm_btn = driver.find_element_by_xpath(xpath)
        confirm_btn.click()
        print "The edited repeat meeting is deleted from google calendar"
        print ''
    except:
        print "The edited repeat meeting is deleted from google calendar"
    
    
    
if __name__ == '__main__':
    
    Login_Gmail_Get_Calendar.login_gmail_account()
    Login_Gmail_Get_Calendar.go_to_google_calendar()
    locate_edited_meeting()
    delete_edited_meeting()
#     driver.quit()