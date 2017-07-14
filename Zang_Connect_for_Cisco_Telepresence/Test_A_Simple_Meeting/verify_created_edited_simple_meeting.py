'''
Created on May 11, 2017

@author: qcadmin
'''
import Login_Gmail_Get_Calendar
import login_tms_server
import create_a_simple_meeting
import edit_created_simple_meeting
import time
from Gmail_and_Google_Calendar import login_meeting_attendee_email
from email import email

title = create_a_simple_meeting.title
new_title = edit_created_simple_meeting.new_title
tomorrow = create_a_simple_meeting.tomorrow
fromtime = create_a_simple_meeting.fromtime
untiltime = create_a_simple_meeting.untiltime
meeting_room = create_a_simple_meeting.meeting_room
guest1 = create_a_simple_meeting.guest_1
guest2 = create_a_simple_meeting.guest_2
guest3 = edit_created_simple_meeting.guest_3
guest4 = edit_created_simple_meeting.guest_4
tms_default = "Conductor01"
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
#         xpath = "//table[@id='ctl00_uxContent_ctl01_uxConferenceParticipants_participantGrid']/tbody/tr[2]/td[2]/nobr"
        xpath = "//tr[contains(@title,'%s')]/td[2]/nobr" % meeting_room
        particpt = driver.find_element_by_xpath(xpath)
        print particpt.text
        mt_room = particpt.text
        print "Got meeting room info"
        return mt_room
    mt_room = get_meeting_romm()
    
    def verify_invited_guests():
        for num in range(2, 5):
            xpath = "//table[@id='ctl00_uxContent_ctl01_uxConferenceParticipants_participantGrid']/tbody/tr[%d]/td[2]/nobr" % num
            particpt = driver.find_element_by_xpath(xpath)
            if particpt.text == 'Dev 02 [%s]' % guest1:
                print "Participant %s is in the list" % guest1
            elif particpt.text == "Dev Test01 [%s]" % guest2:
                print "Participant %s is in the list" % guest2
            elif particpt.text == tms_default:
                print "Participant %s is in the list" % tms_default
            else:
                print "Meeting room or participant are not found"
        print "Selected meeting room and 2 invited guests are verified"
        print "The meeting details are exactly same with those in created meeting"
        print ''
    verify_invited_guests()
    
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
    
    def verify_emails_guest_received():
        print "Verify Guest received meeting invitation"
        login_meeting_attendee_email.guest_email_login(driver)
        email_1 = "Updated Invitation: %s" % title
        email_2 = "Invitation: %s" % title
        for emails in (email_1, email_2):
            xpath = "//a[contains(@title,'Inbox')]"
            Inbox_link = driver.find_element_by_xpath(xpath)
            Inbox_link.click()
            time.sleep(2)
            xpath_unread = "//span[@class='bog']/b[contains(.,'%s')]" % emails
            xpath_read = "//span[contains(.,'%s')]" % emails
            try:
                email_sjct = driver.find_element_by_xpath(xpath_unread)
                email_sjct.click()
                print "Email '%s' is verified received" % emails
    #             xpath = "//div[@aria-label='Delete']/div/div"
                xpath = "//*[@id=':5']/div[2]/div[1]/div/div[2]/div[3]/div/div"
                del_trash = driver.find_element_by_xpath(xpath)
                del_trash.click()
                print "Email'%s' is deleted" % emails
                time.sleep(1)
            except:
                email_sjct = driver.find_element_by_xpath(xpath_read)
                email_sjct.click()
                print "Email '%s' is verified received" % emails
                xpath = "//*[@id=':5']/div[2]/div[1]/div/div[2]/div[3]/div/div"
                del_trash = driver.find_element_by_xpath(xpath)
                del_trash.click()
                print "Email '%s' is deleted" % emails
                time.sleep(1)
    verify_emails_guest_received()
    
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
        for num in range(2, 7):
            xpath = "//table[@id='ctl00_uxContent_ctl01_uxConferenceParticipants_participantGrid']/tbody/tr[%d]/td[2]/nobr" % num
            particpt = driver.find_element_by_xpath(xpath)
            if particpt.text == WebEx_CMR:
                print "Externally Hosted Conference (CMR) is verified"
            elif particpt.text == "Dev 02 [%s]" % guest1:
                print "Guest %s is in the attendee list" % guest1
            elif particpt.text == "Dev Test01 [%s]" % guest2:
                print "Guest %s is in the attendee list" % guest2 
            elif particpt.text == "EsnaQCForTestingOnEsnaAgainAndAgain TestAccount [%s]" % guest3:
                print "Guest %s is in the attendee list" % guest3
            elif particpt.text == guest4:
                print guest4
            else:
                print "Meeting room or participant are not found"
        print "Changed meeting room and 4 intvited guests are verified"
        print "The meeting details are exactly same with those in created meeting"
        print ''
    verify_invited_guests()
    
    def verify_update_email_guest_received():
        print "Verify Guest received meeting invitation"
        login_meeting_attendee_email.guest_email_login(driver)
        up_email = "Updated Invitation: %s" % new_title
        xpath = "//a[contains(@title,'Inbox')]"
        Inbox_link = driver.find_element_by_xpath(xpath)
        Inbox_link.click()
        time.sleep(2)
        xpath_unread = "//span[@class='bog']/b[contains(.,'%s')]" % up_email
        xpath_read = "//span[contains(.,'%s')]" % up_email
        try:
            email_sjct = driver.find_element_by_xpath(xpath_unread)
            email_sjct.click()
            print "Email '%s' is verified received" % up_email
#             xpath = "//div[@aria-label='Delete']/div/div"
            xpath = "//*[@id=':5']/div[2]/div[1]/div/div[2]/div[3]/div/div"
            del_trash = driver.find_element_by_xpath(xpath)
            del_trash.click()
            print "Email'%s' is deleted" % up_email
            time.sleep(1)
        except:
            email_sjct = driver.find_element_by_xpath(xpath_read)
            email_sjct.click()
            print "Email '%s' is verified received" % up_email
            xpath = "//*[@id=':5']/div[2]/div[1]/div/div[2]/div[3]/div/div"
            del_trash = driver.find_element_by_xpath(xpath)
            del_trash.click()
            print "Email '%s' is deleted" % up_email
            time.sleep(1)
    verify_update_email_guest_received()
    
def verify_deleted_meeting():
    """Verify guest received updated email for meeting canceled"""
    def verify_guest_received_eventCancel_email():
        print "Verify Guest received meeting invitation"
        login_meeting_attendee_email.guest_email_login(driver)
        canceled_email = "Canceled Event: %s" % new_title
        xpath = "//a[contains(@title,'Inbox')]"
        Inbox_link = driver.find_element_by_xpath(xpath)
        Inbox_link.click()
        time.sleep(2)
        xpath_unread = "//span[@class='bog']/b[contains(.,'%s')]" % canceled_email
        xpath_read = "//span[contains(.,'%s')]" % canceled_email
        try:
            email_sjct = driver.find_element_by_xpath(xpath_unread)
            email_sjct.click()
            print "Email '%s' is verified received" % canceled_email
#             xpath = "//div[@aria-label='Delete']/div/div"
            xpath = "//*[@id=':5']/div[2]/div[1]/div/div[2]/div[3]/div/div"
            del_trash = driver.find_element_by_xpath(xpath)
            del_trash.click()
            print "Email'%s' is deleted" % canceled_email
            time.sleep(1)
        except:
            email_sjct = driver.find_element_by_xpath(xpath_read)
            email_sjct.click()
            print "Email '%s' is verified received" % canceled_email
            xpath = "//*[@id=':5']/div[2]/div[1]/div/div[2]/div[3]/div/div"
            del_trash = driver.find_element_by_xpath(xpath)
            del_trash.click()
            print "Email '%s' is deleted" % canceled_email
            time.sleep(1)
    verify_guest_received_eventCancel_email()
    
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