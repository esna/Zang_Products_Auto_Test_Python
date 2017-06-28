'''
Created on May 11, 2017

@author: qcadmin
'''
import Login_Gmail_Get_Calendar
import login_tms_server
import create_a_simple_meeting
import edit_created_simple_meeting
import time

title = create_a_simple_meeting.title
new_title = edit_created_simple_meeting.new_title
tomorrow = create_a_simple_meeting.tomorrow
fromtime = create_a_simple_meeting.fromtime
untiltime = create_a_simple_meeting.untiltime
meeting_room = create_a_simple_meeting.meeting_room
guest1 = edit_created_simple_meeting.guest1
guest2 = edit_created_simple_meeting.guest2
WebEx_CMR = 'Externally Hosted Conference'
values_list = []
driver = Login_Gmail_Get_Calendar.driver

def verify_created_simple_meeting():
    def get_meeting_title():
        values_list = []
        xpath = "//a[contains(., '%s')]" % title
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
    assert meeting_room == mt_room
    print "Meeting room is verified"
    print "The meeting details are exactly same with those in created meeting"
    print ''
    
def verify_edited_simple_meeting():
    def locate_edited_meeting():
        try:
            xpath = "//a[contains(., '%s')]" % new_title
            meeting_title = driver.find_element_by_xpath(xpath)
            meeting_title.click()
            print "Edited meeting is found"
        except:
            print "Edited meeting is not found"
        time.sleep(1)
    locate_edited_meeting()
        
    def verify_meeting_title():
        xpath = "//td[@class='PropertyValue']"
        title_item = driver.find_elements_by_xpath(xpath)
        for elem in title_item:
            values_list.append(elem.text)
        title_content = values_list[0]
        assert new_title == title_content
        print "Changed meeting title is verified"
    verify_meeting_title()
    
    def verify_invited_guests():
        for num in (2, 3, 4):
            xpath = "//table[@id='ctl00_uxContent_ctl01_uxConferenceParticipants_participantGrid']/tbody/tr[%d]/td[2]/nobr" % num
            particpt = driver.find_element_by_xpath(xpath)
            if num == 2:
                assert particpt.text == WebEx_CMR
            elif num == 3:
                assert particpt.text == "EsnaQC Testing [%s]" % guest2
            elif num == 4:
                assert particpt.text == "EsnaQCForTestingOnEsnaAgainAndAgain TestAccount [%s]" % guest1
            else:
                print "Meeting room or participant are not found"
        print "Changed meeting room and 2 intvited guests are verified"
        print "The meeting details are exactly same with those in created meeting"
        print ''
    verify_invited_guests()
    
def verify_deleted_meeting():
    try:
        xpath = "//td[contains(., 'No results found. Try widening your search by using fewer criteria.')]"
        no_result = driver.find_element_by_xpath(xpath)
        if no_result.is_displayed():
            print "No meeting list is diaplyed, the edited simple meeting is deleted"
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
                print "Edited meeting is not found in meeting list, it was deleted"
        except:
            print "Edited simple meeting is not found, it is deleted"

# if __name__ == '__main__':
#      
#     login_tms_server.login_tms_server()
#     verify_created_simple_meeting()
#     verify_edited_simple_meeting()
#     verify_deleted_meeting()
#     driver.quit()