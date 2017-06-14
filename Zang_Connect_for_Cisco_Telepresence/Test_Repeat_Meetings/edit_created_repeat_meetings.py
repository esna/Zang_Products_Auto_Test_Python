'''
Created on May 11, 2017

@author: qcadmin
'''
import Login_Gmail_Get_Calendar
import create_repeat_meetings
import time

driver = Login_Gmail_Get_Calendar.driver
ori_title = create_repeat_meetings.ori_title
new_title = create_repeat_meetings.new_title

new_title = "Repeat meeting edited, two meeting rooms, start time 1:00pm"
meeting_room = 'test1'
userid = Login_Gmail_Get_Calendar.ConfigSectionMap("Account")['essultn_id_2']
passwd = Login_Gmail_Get_Calendar.ConfigSectionMap("Account")['essultn_pwd']
new_from_time = "1:00 PM"
new_untl_time = "2:00 PM"
meeting_room_1 = create_repeat_meetings.meeting_room_1
meeting_room_2 = create_repeat_meetings.meeting_room_2
new_mt_room_1 = 'test1'
new_mt_room_2 = 'No Name (192.168.1.38)'
room_list_2 = (new_mt_room_1, new_mt_room_2)

def change_meeting_title():
    try:
        xpath = "//span[@class='chip-caption']"
        fl_menu = driver.find_element_by_xpath(xpath)
        fl_menu.click()
        print "Found the edited meeting"
    except:
        print 'The created meeting is not found'
    time.sleep(1)
    """Get created meeting and edit"""
    driver.switch_to_active_element()
    xpath = "//div[@class='neb-footer']/span[2]/div[2]"
    edit_btn = driver.find_element_by_xpath(xpath)
    edit_btn.click()
    time.sleep(2)
    xpath = "//input[@title='Event title']"
    mt_title = driver.find_element_by_xpath(xpath)
    mt_title.clear()
    mt_title.send_keys(new_title)
    print "Meeting title is changed to a new one"
    
def change_meeting_time():
    from_time = driver.find_element_by_xpath("//input[@title = 'From time']")
    until_time = driver.find_element_by_xpath("//input[@title = 'Until time']")
    from_time.clear()
    from_time.send_keys(new_from_time)
    until_time.clear()
    until_time.send_keys(new_untl_time)
    print "Meeting schedule is changed"
    
def change_meeting_room():
    """remove webex meeting"""
    for mt_room in (meeting_room_1, meeting_room_2):
        try:
            xpath = "//div[@aria-label='TMSUCREID - %s, accepted']/div/div/span[2]" % mt_room
            remove_icon = driver.find_element_by_xpath(xpath)
            remove_icon.click()
            print "%s is removed" % mt_room
        except:
            print "%s is not in the participant list"
    
    for new_mt_room in room_list_2:
        xpath = "//span[@id='ui-ltsr-tab-1']"
        room_menu = driver.find_element_by_xpath(xpath)
        room_menu.click()
        time.sleep(2)
        xpath = "//input[@title='Search rooms']"
        room_filter = driver.find_element_by_xpath(xpath)
        room_filter.click()
        room_filter.clear()
        room_filter.send_keys(new_mt_room)
        time.sleep(1)
        print "%s is selected" % new_mt_room 
        try:
            select_room = 'TMSUCREID - %s' % new_mt_room
            xpath = "//span[contains(., '%s')]" % select_room
            driver.find_element_by_xpath(xpath).click()
            time.sleep(1)
            print "Meeting room is changed to %s" % select_room
        except:
            print "The meeting room is not available, meeting is not created."
    
def save_edited_meeting():
    xpath = "//div[@class='goog-imageless-button-content'][contains(., 'Save')]"
    save_btn = driver.find_element_by_xpath(xpath)
    save_btn.click()
    driver.switch_to_active_element()
    driver.find_element_by_xpath("(//td[@class='ep-es-button-cell']/div)[3]").click()
    print "Edited meeting is saved"
    print ''
    
    
    
# if __name__ == '__main__':
#     
#     Login_Gmail_Get_Calendar.login_gmail_account()
#     Login_Gmail_Get_Calendar.go_to_google_calendar()
#     change_meeting_title()
#     change_meeting_time()
#     change_meeting_room()
#     save_edited_meeting()