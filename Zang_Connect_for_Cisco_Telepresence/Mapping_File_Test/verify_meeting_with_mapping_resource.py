'''
Created on May 9, 2017

@author: qcadmin
'''
import Login_Gmail_Get_Calendar
import login_tms_server
import create_meeting_with_mapping_resource
import edit_meeting_with_mapping_resource
import csv
import time

map_file = "C:/TMS_Resources/resources_map_google.csv"
tms_res = "C:/TMS_Resources/resources_tms.csv"
tms_res_dict = {}
driver = Login_Gmail_Get_Calendar.driver
title = create_meeting_with_mapping_resource.title
new_title = edit_meeting_with_mapping_resource.new_title
tomorrow = create_meeting_with_mapping_resource.tomorrow
fromtime = create_meeting_with_mapping_resource.fromtime
untiltime = create_meeting_with_mapping_resource.untiltime
tms_res_room1 = ''
tms_res_room2 = ''

"""read first line from mapping file, get google id"""
with open (map_file, 'r') as f:
    lines = f.readlines()
    line = lines[0]
    tid1 = line.split(",")[0]
    line = lines[1]
    tid2 = line.split(",")[0]

"""get tms resource name from csv file"""
reader = csv.reader(open(tms_res, 'r'))
for row in reader:
    k = row[0]
    v = row[1]
    tms_res_dict[k] = v
    
for v in tms_res_dict:
    if v == tid1:
        tms_res_room1 = tms_res_dict[v]
        break
    else:
        continue
    
for v in tms_res_dict:
    if v == tid2:
        tms_res_room2 = tms_res_dict[v]
        break
    else:
        continue

def verify_created_meeting_details():
    def get_meeting_title():
        values_list = []
        xpath = "//a[contains(., '%s')]" % title
        try:
            meeting_title = driver.find_element_by_xpath(xpath)
            print "Created meeting is found"
            meeting_title.click()
            time.sleep(2)
            xpath = "//td[@class='PropertyValue']"
    #             xpath = "%s/following-sibling::td[@class='PropertyValue']/span" % title_xpath
            title_item = driver.find_elements_by_xpath(xpath)
            for elem in title_item:
                values_list.append(elem.text)
            title_content = values_list[0]
            return title_content
        except:
            print "Created meeting is not found"
            driver.quit()
            driver.quit()

    title_content = get_meeting_title()
    
    def get_meeting_scheduel():
        xpath = "//input[@id='ctl00_uxContent_ctl01_conferenceTime_dpStartDate_dateInput']"
        start_date = driver.find_element_by_xpath(xpath)
        st_date = start_date.get_attribute('value')
        
        xpath = "//input[@id='ctl00_uxContent_ctl01_conferenceTime_dpEndDate_dateInput']"
        end_date = driver.find_element_by_xpath(xpath)
        ed_date = end_date.get_attribute('value')

        xpath = "//input[@id='ctl00_uxContent_ctl01_conferenceTime_tbStartTime']"
        start_time = driver.find_element_by_xpath(xpath)
        st_time = start_time.get_attribute('value')

        xpath = "//input[@id='ctl00_uxContent_ctl01_conferenceTime_tbEndTime']"
        end_time = driver.find_element_by_xpath(xpath)
        ed_time = end_time.get_attribute('value')
        print "Got meeting schedule date time"
        return (st_date, ed_date, st_time, ed_time)
    (st_date, ed_date, st_time, ed_time) = get_meeting_scheduel()
    
    def get_meeting_romm():
        xpath = "//table[@id='ctl00_uxContent_ctl01_uxConferenceParticipants_participantGrid']/tbody/tr[2]/td[2]/nobr"
        particpt = driver.find_element_by_xpath(xpath)
        mt_room = particpt.text
        print "Got meeting room info"
        return mt_room
    mt_room = get_meeting_romm()
    
    """Verify meeting details"""
    assert title == title_content
    print "Meeting title is verified"
    assert tomorrow == st_date
    assert tomorrow == ed_date
    assert fromtime == st_time
    assert untiltime == ed_time
    print "Meeting date, start and end time are verified"
    assert tms_res_room1 == mt_room
    print "Meeting room is verified"
    print "The meeting details are exactly same with those in created meeting"
    print ''
        
        
def verify_edited_meeting_details():
    def get_meeting_title():
        values_list = []
        xpath = "//a[contains(., '%s')]" % new_title
        try:
            meeting_title = driver.find_element_by_xpath(xpath)
            print "Edited meeting is found"
            meeting_title.click()
            time.sleep(3)
            xpath = "//td[@class='PropertyValue']"
    #             xpath = "%s/following-sibling::td[@class='PropertyValue']/span" % title_xpath
            title_item = driver.find_elements_by_xpath(xpath)
            for elem in title_item:
                values_list.append(elem.text)
            title_content = values_list[0]
            return title_content
        except:
            print "Edited meeting is not found"
            driver.quit()
            driver.quit()

    title_content = get_meeting_title()
    
    def get_meeting_romm():
        xpath = "//table[@id='ctl00_uxContent_ctl01_uxConferenceParticipants_participantGrid']/tbody/tr[2]/td[2]/nobr"
        particpt = driver.find_element_by_xpath(xpath)
        mt_room = particpt.text
        print "Got meeting room info"
        return mt_room
    mt_room = get_meeting_romm()
    
    """Verify meeting details"""
    assert new_title == title_content
    print "Meeting title is verified"
    print tms_res_room2
    print mt_room
    assert tms_res_room2 == mt_room
    print "Meeting room is verified"
    print "The meeting details are exactly same with those in created meeting"
    print ''
        
def verify_deleted_meeting():
    try:
        xpath = "//td[contains(., 'No results found. Try widening your search by using fewer criteria.')]"
        no_result = driver.find_element_by_xpath(xpath)
        if no_result.is_displayed():
            print "No meeting list is diaplyed, the edited meeting is deleted"
        else:
            print "A meeting list is displayed"
    except:
        try:
            xpath = "//a[contains(., '%s')]" % new_title
            meeting_title = driver.find_element_by_xpath(xpath)
            xpath = "//span[@id='ctl00_uxContent_ctl01_conferenceGrid_ctl02_StartDate']"
            start_date = driver.find_element_by_xpath(xpath)
            st_date = start_date.text
            if meeting_title.is_displayed() and tomorrow == st_date:
                print "The meeting is still there, not deleted"
            else:
                print "Edited repeat meeting is not found in meeting list, it was deleted"
        except:
            print "Edited repeat meeting is not found, it is deleted"
        
        
# if __name__ == '__main__':
#     
#     login_tms_server.login_tms_server()
#     verify_created_meeting_details()
#     verify_edited_meeting_details()
#     verify_deleted_meeting()
#     driver.quit()