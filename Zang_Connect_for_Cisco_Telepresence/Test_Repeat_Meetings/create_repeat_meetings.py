'''
Created on May 11, 2017

@author: qcadmin
'''
import Login_Gmail_Get_Calendar
import time
import datetime

tmr = datetime.date.today() + datetime.timedelta(days=1)
tmr_plus_one = datetime.date.today() + datetime.timedelta(days=2)
d1 = datetime.datetime.strptime("%s" % tmr, '%Y-%m-%d')
d2 = datetime.datetime.strptime("%s" % tmr_plus_one, '%Y-%m-%d')
tomorrow = datetime.date.strftime(d1, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
tom_plus_one = datetime.date.strftime(d2, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
fromtime = "12:00 PM"
untiltime = "1:00 PM"
ori_title = 'Repeat meeting, two meeting rooms, repeat daily for 5 times'
new_title = "Repeat meeting edited, three meeting rooms, start time 1:00pm"
meeting_room_1 = 'No Name (192.168.0.138)'
meeting_room_2 = 'New Room A'
room_list_1 = (meeting_room_1, meeting_room_2)
userid = Login_Gmail_Get_Calendar.ConfigSectionMap("Account")['essultn_id_2']
passwd = Login_Gmail_Get_Calendar.ConfigSectionMap("Account")['essultn_pwd']

driver = Login_Gmail_Get_Calendar.driver


def input_meeting_title():
    xpath = "//div[@id='createEventButtonContainer']//div[@class='goog-imageless-button-content']"
    create_btn = driver.find_element_by_xpath(xpath)
    create_btn.click()
    xpath = "//input[@title='Event title']"
    meeting_title = driver.find_element_by_xpath(xpath)
    meeting_title.clear()
    meeting_title.send_keys(ori_title)
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

def set_repeating_cycle():
    repeat_check = driver.find_element_by_id(":20.repeatcheckbox")
    repeat_check.click()
    time.sleep(2)
    driver.switch_to_active_element()
    xpath = "//table[@class='ep-rec']/tbody/tr/td/select/option[@value='0']"
    driver.find_element_by_xpath(xpath).click()
    xpath = "//input[@aria-label='Ends after a number of occurrences']"
    option_after = driver.find_element_by_xpath(xpath)
    option_after.click()
    xpath = "//td[@class='ep-rec-buttons-padding']/div/div"
    time.sleep(2)
    done_btn = driver.find_element_by_xpath(xpath)
    done_btn.click()
    print "Repeating cycle is set"

def select_meeting_rooms():
    for select_room in room_list_1:
        xpath = "//span[@id='ui-ltsr-tab-1']"
        room_menu = driver.find_element_by_xpath(xpath)
        room_menu.click()
        time.sleep(2)
        xpath = "//input[@title='Search rooms']"
        room_filter = driver.find_element_by_xpath(xpath)
        room_filter.click()
        select_room = 'TMSUCREID - %s' % select_room
        room_filter.clear()
        room_filter.send_keys(select_room)
        time.sleep(2)
        try:
            xpath = "//span[contains(., '%s')]" % select_room
            driver.find_element_by_xpath(xpath).click()
            print "%s is selected" % select_room
            time.sleep(2)
        except:
            print "The meeting room is not available."
    print "Meeting rooms are selected"
    time.sleep(5)
        
def save_created_meeting():
    xpath = "//div[@class='goog-imageless-button-content'][contains(., 'Save')]"
    save_btn = driver.find_element_by_xpath(xpath)
    save_btn.click()
    print "Scheduled repeat meeting is saved"
    print ''


# if __name__ == '__main__':
#     
#     Login_Gmail_Get_Calendar.login_gmail_account()
#     Login_Gmail_Get_Calendar.go_to_google_calendar()
#     input_meeting_title()
#     set_meeting_schedule()
#     set_repeating_cycle()
#     select_meeting_rooms()
#     save_created_meeting()