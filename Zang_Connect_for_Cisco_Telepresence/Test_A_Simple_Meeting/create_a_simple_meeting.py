'''
Created on May 11, 2017

@author: qcadmin
'''
import Login_Gmail_Get_Calendar
import time
import datetime
from selenium.webdriver.common.keys import Keys

tmr = datetime.date.today() + datetime.timedelta(days=1)
tmr_plus_one = datetime.date.today() + datetime.timedelta(days=2)
d1 = datetime.datetime.strptime("%s" % tmr, '%Y-%m-%d')
d2 = datetime.datetime.strptime("%s" % tmr_plus_one, '%Y-%m-%d')
tomorrow = datetime.date.strftime(d1, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
tom_plus_one = datetime.date.strftime(d2, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
fromtime = "12:00 PM"
untiltime = "1:00 PM"
title = 'Default meeting with single meeting room'
new_title = 'Default meeting is changed to WebEx CMR meeting'
meeting_room = 'new intern testing room'
new_mt_room = 'WebEx CMR meeting'
guest_1 = 'dev02@esnaqc.com'
guest_2 = 'dev01@esnaqc.com'
guestlist_1 = (guest_1, guest_2)
userid = Login_Gmail_Get_Calendar.ConfigSectionMap("Account")['essultn_id_2']
passwd = Login_Gmail_Get_Calendar.ConfigSectionMap("Account")['essultn_pwd']

driver = Login_Gmail_Get_Calendar.driver

def input_meeting_title():
    xpath = "//div[@id='createEventButtonContainer']//div[@class='goog-imageless-button-content']"
    create_btn = driver.find_element_by_xpath(xpath)
    create_btn.click()
    print "Input meeting title"
    xpath = "//input[@title='Event title']"
    meeting_title = driver.find_element_by_xpath(xpath)
    meeting_title.clear()
    meeting_title.send_keys(title)
    print "Meeting title is input"

def set_meeting_schedule():
    from_date = driver.find_element_by_xpath("//input[@title = 'From date']")
    until_date = driver.find_element_by_xpath("//input[@title = 'Until date']")
    from_time = driver.find_element_by_xpath("//input[@title = 'From time']")
    until_time = driver.find_element_by_xpath("//input[@title = 'Until time']")
    from_date.clear()
    from_date.send_keys(tomorrow)
    until_date.clear()
    until_date.send_keys(tomorrow)
    from_time.clear()
    from_time.send_keys(fromtime)
    until_time.clear()
    until_time.send_keys(untiltime)
    print "Meeting schedule is set"
    
def select_meeting_room():
    print "Select meeting room"
    xpath = "//span[@id='ui-ltsr-tab-1']"
    room_menu = driver.find_element_by_xpath(xpath)
    room_menu.click()
    time.sleep(2)
    xpath = "//input[@title='Search rooms']"
    room_filter = driver.find_element_by_xpath(xpath)
    room_filter.click()
    room_filter.clear()
    select_room = 'TMSUCREID - %s' % meeting_room
    room_filter.send_keys(select_room)
    time.sleep(1)
    driver.find_element_by_xpath("//span[contains(.,'%s')]"% select_room).click()
    time.sleep(1)
    return select_room
    time.sleep(2)
    print "Meeting room is selected"
    try:
        driver.find_element_by_xpath("//span[contains(.,'%s')]"% select_room).click()
        time.sleep(2)
        print "Selected meeting room is added"
    except:
        print "Selected meeting room is not available, meeting cannot be created"
        driver.quit()
        
def add_guests():
    guests = driver.find_element_by_id("ui-ltsr-tab-0")
    guests.click()
    time.sleep(1)
    add_box = driver.find_element_by_xpath("//input[@title='Add guests']")
    for guests in (guestlist_1):
        add_box.clear()
        add_box.send_keys(guests)
        add_box.send_keys(Keys.RETURN)
        time.sleep(2)
        print "Invited guest %s is added" % guests
        
def save_created_meeting():
    print "Save the created meeting"
    xpath = "//div[@class='goog-imageless-button-content'][contains(., 'Save')]"
    save_btn = driver.find_element_by_xpath(xpath)
    print "Click Save button"
    save_btn.click()
    driver.switch_to_active_element()
    time.sleep(2)
    print "Click Send button for sending email"
    try:
        driver.switch_to_active_element()
        send_btn = driver.find_element_by_name('yes')
        send_btn.click()
        print "Created meeting is saved"
        print ''
    except:
        print "Created meeting is saved"
        print ''
    time.sleep(2)
    print ''

        
# if __name__ == '__main__':
#       
#     Login_Gmail_Get_Calendar.login_gmail_account()
#     Login_Gmail_Get_Calendar.go_to_google_calendar()
#     input_meeting_title()
#     set_meeting_schedule()
#     select_room = select_meeting_room()
#     add_guests()
#     save_created_meeting()
    
