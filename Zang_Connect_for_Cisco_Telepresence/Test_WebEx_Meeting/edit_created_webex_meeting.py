'''
Created on May 11, 2017

@author: qcadmin
'''

import Login_Gmail_Get_Calendar
import create_webex_meeting
import time
from selenium.webdriver.common.keys import Keys

driver = Login_Gmail_Get_Calendar.driver
ori_title = create_webex_meeting.ori_title
new_title = 'Edit WebEx meeting date to the day after tomorrow'
userid = Login_Gmail_Get_Calendar.ConfigSectionMap("Account")['essultn_id_2']
passwd = Login_Gmail_Get_Calendar.ConfigSectionMap("Account")['essultn_pwd']
guest1 = 'esnaqc.test.01@gmail.com'
guest2 = 'esnaqc.testing@gmail.com'
tom_plus_one = create_webex_meeting.tom_plus_one
new_fromtime = '11:00 AM'
new_untltime = '12:00 PM'
mt_descp = "Reid Zhang invites you to this meeting."


def change_meeting_title():
    try:
        xpath = "//span[contains(., '%s')]" % ori_title
        driver.find_element_by_xpath(xpath)
        crt_meeting = driver.find_element_by_xpath(xpath)
        crt_meeting.click()
        print "Found the edited meeting"
        time.sleep(2)
    except:
        print 'The created meeting is not found'
        driver.close()
        driver.quit()
    xpath = "//input[@title='Event title']"
    meeting_title = driver.find_element_by_xpath(xpath)
    meeting_title.clear()
    meeting_title.send_keys(new_title)
    print "Meeting title is changed to a new one"
    
    xpath = "//textarea[contains(.,'%s')]" % mt_descp
    text_area = driver.find_element_by_xpath(xpath)
    if text_area.is_displayed():
        print "Meeting description is displayed"
    
def change_meeting_schedule():
    from_date = driver.find_element_by_xpath("//input[@title = 'From date']")
    until_date = driver.find_element_by_xpath("//input[@title = 'Until date']")
    from_time = driver.find_element_by_xpath("//input[@title = 'From time']")
    until_time = driver.find_element_by_xpath("//input[@title = 'Until time']")
    from_date.clear()
    from_date.send_keys(tom_plus_one)
    until_date.clear()
    until_date.send_keys(tom_plus_one)
    from_time.clear()
    from_time.send_keys(new_fromtime)
    until_time.clear()
    until_time.send_keys(new_untltime)
    print "Meeting schedule is set"
        
def add_guests():
    guests = driver.find_element_by_id("ui-ltsr-tab-0")
    guests.click()
    time.sleep(1)
    add_box = driver.find_element_by_xpath("//input[@title='Add guests']")
    for guests in (guest1, guest2):
        add_box.clear()
        add_box.send_keys(guests)
        add_box.send_keys(Keys.RETURN)
        time.sleep(2)
    print "Two new guests are added"
    
def save_edited_meeting():
    xpath = "//div[@class='goog-imageless-button-content'][contains(., 'Save')]"
    save_btn = driver.find_element_by_xpath(xpath)
    save_btn.click()
    time.sleep(2)
    try:
        driver.switch_to_active_element()
        send_btn = driver.find_element_by_name('no')
        send_btn.click()
        print "Edited meeting is saved"
        print ''
    except:
        print "Edited meeting is saved"
        print ''
    
    
    
# if __name__ == '__main__':
#     
#     Login_Gmail_Get_Calendar.login_gmail_account()
#     Login_Gmail_Get_Calendar.go_to_google_calendar()
#     change_meeting_title()
#     select_room = change_meeting_schedule()
#     add_guests()
#     save_edited_meeting()
#     driver.quit()