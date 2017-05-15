'''
Created on May 9, 2017

@author: qcadmin
'''
import datetime
import time
import csv
import Login_Gmail_Get_Calendar
from read_csv_files import google_res_dict

map_file = "C:/TMS_Resources/resources_map_google.csv"
tms_res = "C:/TMS_Resources/resources_tms.csv"
google_res = "C:/TMS_Resources/resources_google.csv"

"""read first line from mapping file, get google id"""
with open (map_file, 'r') as f:
    lines = f.readlines()
    line = lines[0]
    gid = line.split(",")[1]
    tid = line.split(",")[0]
    
"""get google resource name from csv file"""
reader = csv.reader(open(google_res, 'r'))
for row in reader:
    k = row[0]
    v = row[1]
    google_res_dict[k] = v
for v in google_res_dict:
    google_res_room = google_res_dict[v]
    if v == gid:
        break
    else:
        continue
    
tmr = datetime.date.today() + datetime.timedelta(days=1)
tmr_plus_one = datetime.date.today() + datetime.timedelta(days=2)
d1 = datetime.datetime.strptime("%s" % tmr, '%Y-%m-%d')
d2 = datetime.datetime.strptime("%s" % tmr_plus_one, '%Y-%m-%d')
tomorrow = datetime.date.strftime(d1, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
tom_plus_one = datetime.date.strftime(d2, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
fromtime = "12:00 PM"
untiltime = "1:00 PM"
title = 'Create a meeting with mapped resources'
userid = Login_Gmail_Get_Calendar.ConfigSectionMap("Account")['essultn_id_2']
passwd = Login_Gmail_Get_Calendar.ConfigSectionMap("Account")['essultn_pwd']
guest1 = 'reidz@esna.com'
guest2 = 'esnaqc.testing@gmail.com'
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
#     select_room = 'TMSUCREID - %s' % google_name
    room_filter.send_keys(google_res_room)
    print "Meeting room is selected"
    time.sleep(1)
    try:
        driver.find_element_by_xpath("//span[contains(.,'%s')]"% google_res_room).click()
        time.sleep(2)
        print "Selected meeting room is added"
    except:
        print "Selected meeting room is not available, meeting cannot be created"
        driver.quit()
        
def save_created_meeting():
    print "Save the created meeting"
    xpath = "//div[@class='goog-imageless-button-content'][contains(., 'Save')]"
    save_btn = driver.find_element_by_xpath(xpath)
    save_btn.click()
    time.sleep(5)
    print "Created meeting is saved"
    print ''
    
    
        
if __name__ == '__main__':
    
    Login_Gmail_Get_Calendar.login_gmail_account()
    Login_Gmail_Get_Calendar.go_to_google_calendar()
    input_meeting_title()
    set_meeting_schedule()
    select_room = select_meeting_room()
    save_created_meeting()
    
