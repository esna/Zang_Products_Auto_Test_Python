'''
Created on May 11, 2017

@author: qcadmin
'''

import Login_Gmail_Get_Calendar
import create_a_simple_meeting
import time
from selenium.webdriver.common.keys import Keys

driver = Login_Gmail_Get_Calendar.driver
title = create_a_simple_meeting.title
new_title = 'Default meeting is changed to WebEx CMR meeting'
meeting_room = 'test1'
new_mt_room = 'WebEx CMR meeting'
userid = Login_Gmail_Get_Calendar.ConfigSectionMap("Account")['essultn_id_2']
passwd = Login_Gmail_Get_Calendar.ConfigSectionMap("Account")['essultn_pwd']
guest1 = 'esnaqc.test.01@gmail.com'
guest2 = 'esnaqc.testing@gmail.com'

def change_meeting_title():
    try:
        xpath = "//span[contains(., '%s')]" % title
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
    
def change_meeting_room():
    """remove old meeting room"""
    xpath = "(//span[@class='ep-gc-icon ep-gc-icon-response'][@title='Yes'])[2]"
    remove_symbol = driver.find_element_by_xpath(xpath)
    remove_symbol.click()
    print "Old meeting room is removed"
    xpath = "//span[@id='ui-ltsr-tab-1']"
    room_menu = driver.find_element_by_xpath(xpath)
    room_menu.click()
    time.sleep(2)
    xpath = "//input[@title='Search rooms']"
    room_filter = driver.find_element_by_xpath(xpath)
    room_filter.click()
    room_filter.clear()
    select_room = new_mt_room
    room_filter.send_keys(select_room)
    time.sleep(2)
    print "New meeting room is selected"
    try:
        select_room = 'TMSUCREID - %s' % new_mt_room
        xpath = "//span[contains(., '%s')]" % select_room
        driver.find_element_by_xpath(xpath).click()
        time.sleep(2)
        print "Meeting room is changed to %s" % select_room
    except:
        print "The meeting room is not available, meeting is not created."
        
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
    
    
    
if __name__ == '__main__':
    
    Login_Gmail_Get_Calendar.login_gmail_account()
    Login_Gmail_Get_Calendar.go_to_google_calendar()
    change_meeting_title()
    select_room = change_meeting_room()
    add_guests()
    save_edited_meeting()
    driver.quit()