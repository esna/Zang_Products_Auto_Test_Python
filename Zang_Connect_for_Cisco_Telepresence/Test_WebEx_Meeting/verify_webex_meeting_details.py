'''
Created on May 11, 2017

@author: qcadmin
'''
import create_webex_meeting
import Login_Gmail_Get_Calendar
import login_tms_server
import edit_created_webex_meeting
import time
from create_a_simple_meeting import tomorrow

driver = Login_Gmail_Get_Calendar.driver
ori_title = create_webex_meeting.ori_title
new_title = edit_created_webex_meeting.new_title
tom_plus_one = edit_created_webex_meeting.tom_plus_one
fromtime = create_webex_meeting.fromtime
untiltime = create_webex_meeting.untiltime
new_from_time = edit_created_webex_meeting.new_fromtime
new_untl_time = edit_created_webex_meeting.new_untltime
meeting_room_1 = create_webex_meeting.meeting_room_1
meeting_room_2 = create_webex_meeting.meeting_room_2
guest1 = edit_created_webex_meeting.guest1
guest2 = edit_created_webex_meeting.guest2
# new_mt_room_1 = edit_created_webex_meeting.new_mt_room_1
# new_mt_room_2 = edit_created_webex_meeting.new_mt_room_2


def verify_created_webex_meeting():
    def get_meeting_title():
        values_list = []
        xpath = "//a[contains(., '%s')]" % ori_title
        meeting_title = driver.find_element_by_xpath(xpath)
        print "Created meeting is found"
        xpath = "//td[@class='PropertyValue']"
        print "View meeting detials"
        meeting_title.click()
        time.sleep(2)
        title_item = driver.find_elements_by_xpath(xpath)
        for elem in title_item:
            values_list.append(elem.text)
        title_content = values_list[0]
        assert ori_title == title_content
        print "Meeting title is verified"
    get_meeting_title()
        
    def get_edited_webex_meeting_scheduel():
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
        assert tomorrow == st_date
        assert tomorrow == ed_date
        assert fromtime == st_time
        assert untiltime == ed_time
        print "Meeting date, start and end time are verified"
    get_edited_webex_meeting_scheduel()
    
    def verify_meeting_rooms():
        webex_meeting = "Cisco WebEx Meeting" 
        for mt_room in (webex_meeting, meeting_room_2):
            try:
                xpath = "//nobr[contains(., '%s')]" % mt_room
                particpt = driver.find_element_by_xpath(xpath)
                if particpt.is_displayed():
                    print "%s is verified in participant list" % mt_room
            except:
                print "%s is not in participant list for unknown reason (check ZC log)" % mt_room
                continue
    verify_meeting_rooms()
    print ''
    
    
    
    
def verify_edited_webex_meeting():
    def get_edited_webex_meeting_title():
        values_list = []
        xpath = "//a[contains(., '%s')]" % new_title
        meeting_title = driver.find_element_by_xpath(xpath)
        print "Created meeting is found"
        xpath = "//td[@class='PropertyValue']"
        print "View meeting detials"
        meeting_title.click()
        time.sleep(2)
        title_item = driver.find_elements_by_xpath(xpath)
        for elem in title_item:
            values_list.append(elem.text)
        title_content = values_list[0]
        assert new_title == title_content
        print "Meeting title is verified"
    get_edited_webex_meeting_title()
            
    def verify_mtrooms_new_guests():
        print "View the meeting details"
        webex_meeting = "Cisco WebEx Meeting"
        tms_guest1 = "EsnaQCForTestingOnEsnaAgainAndAgain TestAccount [%s]" % guest1
        tms_guest2 = "EsnaQC Testing [%s]" % guest2
        particpt_list = (webex_meeting, meeting_room_2, tms_guest1, tms_guest2)
        for particpts in particpt_list:
            try:
                xpath = "//nobr[contains(., '%s')]" % particpts
                particpt = driver.find_element_by_xpath(xpath)
                if particpt.is_displayed():
                    print "%s is verified in participant list" % particpts
            except:
                print "%s is not in the participant list for unknown reason (check CZ log)" % particpts
        print ''
    verify_mtrooms_new_guests()
    
    
def verify_deleted_webex_meeting():
    try:
        xpath = "//td[contains(., 'No results found. Try widening your search by using fewer criteria.')]"
        no_result = driver.find_element_by_xpath(xpath)
        if no_result.is_displayed():
            print "No meeting list is diaplyed, the edited repeat meeting is deleted"
        else:
            print "A meeting list is displayed"
    except:
        try:
            xpath = "//a[contains(., '%s')]" % new_title
            meeting_title = driver.find_element_by_xpath(xpath)
            xpath = "//span[@id='ctl00_uxContent_ctl01_conferenceGrid_ctl02_StartDate']"
            start_date = driver.find_element_by_xpath(xpath)
            st_date = start_date.text
            if meeting_title.is_displayed() and tom_plus_one == st_date:
                print "The meeting is still there, not deleted"
        except:
            print "Edited webex meeting is not found, it is deleted"

# if __name__ == '__main__':
#     
#     login_tms_server.login_tms_server()
#     verify_created_webex_meeting()
#     verify_edited_webex_meeting()
#     verify_deleted_webex_meeting()
#     driver.quit()