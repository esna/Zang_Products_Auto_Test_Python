'''
Created on May 9, 2017

@author: qcadmin
'''
import time
import csv
import Login_Gmail_Get_Calendar
import create_meeting_with_mapping_resource
import signal
from read_csv_files import google_res_dict

map_file = "C:/TMS_Resources/resources_map_google.csv"
tms_res = "C:/TMS_Resources/resources_tms.csv"
google_res = "C:/TMS_Resources/resources_google.csv"
"""read first line from mapping file, get google id"""
with open (map_file, 'r') as f:
    lines = f.readlines()
    line = lines[1]
    gid = line.split(",")[1]
    tid = line.split(",")[0]
"""get google resource name from csv file"""
reader = csv.reader(open(google_res, 'r'))
for row in reader:
    k = row[0]
    v = row[2]
    google_res_dict[k] = v
for v in google_res_dict:
    google_res_room2 = google_res_dict[v]
    if v == gid:
        break
    else:
        continue
        
title = create_meeting_with_mapping_resource.title
new_title = 'Add meeting room with mapped resources'
new_mt_room = 'WebEx CMR meeting'
userid = Login_Gmail_Get_Calendar.ConfigSectionMap("Account")['essultn_id_2']
passwd = Login_Gmail_Get_Calendar.ConfigSectionMap("Account")['essultn_pwd']
guest1 = 'reidz@esna.com'
guest2 = 'esnaqc.testing@gmail.com'
driver = Login_Gmail_Get_Calendar.driver

def change_meeting_title():
    """Get the created meeting"""
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
        driver.service.process.send_signal(signal.SIGTERM)
         
    """Change meeting title"""
    xpath = "//input[@title='Event title']"
    meeting_title = driver.find_element_by_xpath(xpath)
    meeting_title.clear()
    meeting_title.send_keys(new_title)
    print "Meeting title is changed to a new one"
    
def change_meeting_room():
    xpath = "(//span[@class='ep-gc-icon ep-gc-icon-response'][@title='Yes'])[2]"
    remove_symbol = driver.find_element_by_xpath(xpath)
    remove_symbol.click()
    print "Old meeting room is removed"
    
    print "Select meeting room to be changed"
    xpath = "//span[@id='ui-ltsr-tab-1']"
    room_menu = driver.find_element_by_xpath(xpath)
    room_menu.click()
    time.sleep(2)
    xpath = "//input[@title='Search rooms']"
    room_filter = driver.find_element_by_xpath(xpath)
    room_filter.click()
    room_filter.clear()
#     select_room = 'TMSUCREID - %s' % google_name
    room_filter.send_keys(google_res_room2)
    time.sleep(1)
    try:
        driver.find_element_by_xpath("//span[contains(.,'%s')]"% google_res_room2).click()
        time.sleep(2)
        print "%s is added" % google_res_room2
    except:
        "The meeting room is not available, meeting is not created."
        driver.close()
        driver.quit
        
def save_created_meeting():
    print "Save the created meeting"
    xpath = "//div[@class='goog-imageless-button-content'][contains(., 'Save')]"
    save_btn = driver.find_element_by_xpath(xpath)
    save_btn.click()
    time.sleep(5)
    print "Created meeting is saved"
    print ''
        
    
    
        
# if __name__ == '__main__':
#     
#     Login_Gmail_Get_Calendar.login_gmail_account()
#     Login_Gmail_Get_Calendar.go_to_google_calendar()
#     change_meeting_title()
#     select_room = change_meeting_room()
#     save_created_meeting()
#     driver.quit()
    

