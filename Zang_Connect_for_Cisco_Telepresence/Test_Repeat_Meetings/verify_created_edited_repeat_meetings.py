'''
Created on May 11, 2017

@author: qcadmin
'''
'''
Created on May 11, 2017

@author: qcadmin
'''
import Login_Gmail_Get_Calendar
import login_tms_server
import create_repeat_meetings
import edit_created_repeat_meetings
import datetime
import time

driver = Login_Gmail_Get_Calendar.driver
ori_title = create_repeat_meetings.ori_title
new_title = edit_created_repeat_meetings.new_title
tomorrow = create_repeat_meetings.tomorrow
fromtime = create_repeat_meetings.fromtime
untiltime = create_repeat_meetings.untiltime
new_from_time = edit_created_repeat_meetings.new_from_time
new_untl_time = edit_created_repeat_meetings.new_untl_time
meeting_room_1 = create_repeat_meetings.meeting_room_1
meeting_room_2 = create_repeat_meetings.meeting_room_2
new_mt_room_1 = edit_created_repeat_meetings.new_mt_room_1
new_mt_room_2 = edit_created_repeat_meetings.new_mt_room_2

date_list = []
for i in range(1, 6):
    tmr = datetime.date.today() + datetime.timedelta(days=i)
    di = datetime.datetime.strptime("%s" % tmr, '%Y-%m-%d')
    date_got = datetime.date.strftime(di, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
    date_list.append(date_got)

def verify_created_repeat_meeting():
    def verify_meeting_title_date_time():
        """check if the info line is correct"""
        for j in range(2, 11):
            title_xpath = "//table[@id='ctl00_uxContent_ctl01_conferenceGrid']/tbody/tr[%d]/td[4]/div/div/a" % j
            title = driver.find_element_by_xpath(title_xpath)
            title_content = title.text
            if title_content == ori_title:
                break
            else:
                continue
        day_num = 1
        ori_date = 0
        for i in range (j, j+5):
            def verify_meeting_title():
                title_xpath = "//table[@id='ctl00_uxContent_ctl01_conferenceGrid']/tbody/tr[%d]/td[4]/div/div/a" % i
                title = driver.find_element_by_xpath(title_xpath)
                title_content = title.text
                assert ori_title == title_content
                print "Meeting title on day %d is exactly same with that created" % day_num
            verify_meeting_title()
            
            def verify_meeting_date():
                date_xpath = "//table[@id='ctl00_uxContent_ctl01_conferenceGrid']/tbody/tr[%d]/td[5]/span" % i
                st_date = driver.find_element_by_xpath(date_xpath)
                ori_st_date = date_list[ori_date]
                st_date = st_date.text
                assert st_date == ori_st_date
                print "Meeting start date on day %d is verified" % day_num
            verify_meeting_date()
            
            def verify_meeting_start_time():
                st_time_xpath = "//table[@id='ctl00_uxContent_ctl01_conferenceGrid']/tbody/tr[%d]/td[6]/span" % i
                st_time = driver.find_element_by_xpath(st_time_xpath)
                st_time = st_time.text
                assert fromtime == st_time
                print "Meeting start time on day %d is verified" % day_num
            verify_meeting_start_time()
            
            def verify_meeting_end_time():
                ed_time_xpath = "//table[@id='ctl00_uxContent_ctl01_conferenceGrid']/tbody/tr[%d]/td[7]/span" % i
                ed_time = driver.find_element_by_xpath(ed_time_xpath)
                ed_time = ed_time.text
                assert untiltime == ed_time
                print "Meeting end time on day %d is verified" % day_num
                print ''
            verify_meeting_end_time()
            day_num += 1
            ori_date += 1
    verify_meeting_title_date_time()
    
    def verify_declined_email_sent(mt_room):
        print "Go to email account to verify Declined email is received"
        driver.get("https://mail.google.com")
        declined_email = "Declined: %s" % ori_title
        xpath = "//a[contains(@title,'Inbox')]"
        Inbox_link = driver.find_element_by_xpath(xpath)
        Inbox_link.click()
        time.sleep(2)
        xpath_unread = "//span[@class='bog']/b[contains(.,'%s')]" % declined_email
        xpath_read = "//span[contains(.,'%s')]" % declined_email
        xpath_sender = "//span[@name='%s']" % mt_room
        try:
            email_sjct = driver.find_element_by_xpath(xpath_unread)
            email_sjct.click()
            print "Email '%s' is verified received" % declined_email
#             xpath = "//div[@aria-label='Delete']/div/div"
            xpath = "//*[@id=':5']/div[2]/div[1]/div/div[2]/div[3]/div/div"
            del_trash = driver.find_element_by_xpath(xpath)
            del_trash.click()
            print "Email'%s' is deleted" % declined_email
            time.sleep(2)
        except:
            email_sjct = driver.find_element_by_xpath(xpath_read)
            email_sjct.click()
            print "Email '%s' is verified received" % declined_email
            xpath = "//*[@id=':5']/div[2]/div[1]/div/div[2]/div[3]/div/div"
            del_trash = driver.find_element_by_xpath(xpath)
            del_trash.click()
            print "Email '%s' is deleted" % declined_email
            time.sleep(2)
        print "logout email account"
        logo = driver.find_element_by_xpath("//a[contains(@title,'qc@esnaqc.com')]/span")
        logo.click()
        driver.switch_to_active_element
        signout = driver.find_element_by_xpath("//a[contains(.,'Sign out')]")
        signout.click()
        time.sleep(2)
        print "Go back to tms server console"
        driver.get("http://192.168.1.164/tms/default.aspx?pageId=79&ConfId=17747&View=true")
    
    def verify_meeting_rooms():
        xpath = "//a[contains(., '%s')]" % ori_title
        title = driver.find_element_by_xpath(xpath)
        print "Edited meeting is found"
        title.click()
        print "View meeting details"
        time.sleep(2)
        
        for mt_room in (meeting_room_1, meeting_room_2):
            try:
                xpath = "//nobr[contains(., '%s')]" % mt_room
                particpt = driver.find_element_by_xpath(xpath)
                if particpt.is_displayed():
                    print "%s is verified in participant list" % mt_room
                else:
                    print "%s is not listed as participant for unknown reason (check ZC log)" % mt_room
            except:
                print "%s is not found in participant list" % mt_room
                verify_declined_email_sent(mt_room)
        print ''
        
    verify_meeting_rooms()
    
def verify_edited_repeat_meetings():
    def verify_meeting_title_date_time():
        """check if the info line is correct"""
        for j in range(2, 11):
            title_xpath = "//table[@id='ctl00_uxContent_ctl01_conferenceGrid']/tbody/tr[%d]/td[4]/div/div/a" % j
            title = driver.find_element_by_xpath(title_xpath)
            title_content = title.text
            if title_content == new_title:
                break
            else:
                continue
        day_num = 1
        ori_date = 0
        for i in range (j, j+5):
            def verify_meeting_title():
                title_xpath = "//table[@id='ctl00_uxContent_ctl01_conferenceGrid']/tbody/tr[%d]/td[4]/div/div/a" % i
                title = driver.find_element_by_xpath(title_xpath)
                title_content = title.text
                assert new_title == title_content
                print "Meeting title on day %d is exactly same with that created" % day_num
            verify_meeting_title()
            
            def verify_meeting_start_time():
                st_time_xpath = "//table[@id='ctl00_uxContent_ctl01_conferenceGrid']/tbody/tr[%d]/td[6]/span" % i
                st_time = driver.find_element_by_xpath(st_time_xpath)
                st_time = st_time.text
                assert new_from_time == st_time
                print "Meeting start time on day %d is verified" % day_num
            verify_meeting_start_time()
            
            def verify_meeting_end_time():
                ed_time_xpath = "//table[@id='ctl00_uxContent_ctl01_conferenceGrid']/tbody/tr[%d]/td[7]/span" % i
                ed_time = driver.find_element_by_xpath(ed_time_xpath)
                ed_time = ed_time.text
                assert new_untl_time == ed_time
                print "Meeting end time on day %d is verified" % day_num
                print ''
            verify_meeting_end_time()
            day_num += 1
            ori_date += 1
    verify_meeting_title_date_time()
    
    def verify_declined_email_received(mt_room):
        print "Check if diclined email is received"
        driver.get('http://mail.google.com')
        dcln_email = "Declined: %s" % new_title
        xpath = "//a[contains(@title,'Inbox')]"
        Inbox_link = driver.find_element_by_xpath(xpath)
        Inbox_link.click()
        time.sleep(2)
        xpath_unread = "//span[@class='bog']/b[contains(.,'%s')]" % dcln_email
        xpath_read = "//span[contains(.,'%s')]" % dcln_email
        room_prefix = "TMSUCREID - "
        xpath_sender = "//span[@name='%s']" % (room_prefix + mt_room)
        try:
            email_sjct = driver.find_element_by_xpath(xpath_unread)
            email_sender = driver.find_element_by_xpath(xpath_sender)
            print "Find declined email sent by %s" % mt_room
            email_sjct.click()
            print "Email '%s' is verified received" % dcln_email
            xpath = "//*[@id=':5']/div[2]/div[1]/div/div[2]/div[3]/div/div"
            del_trash = driver.find_element_by_xpath(xpath)
            del_trash.click()
            print "Email'%s' is deleted" % dcln_email
            time.sleep(1)
        except:
            email_sjct = driver.find_element_by_xpath(xpath_read)
            email_sender = driver.find_element_by_xpath(xpath_sender)
            print "Find declined email sent by %s" % mt_room
            email_sjct.click()
            print "Email '%s' is verified received" % dcln_email
            xpath = "//*[@id=':5']/div[2]/div[1]/div/div[2]/div[3]/div/div"
            del_trash = driver.find_element_by_xpath(xpath)
            del_trash.click()
            print "Email '%s' is deleted" % dcln_email
            time.sleep(2)
        print "logout email account"
        logo = driver.find_element_by_xpath("//a[contains(@title,'qc@esnaqc.com')]/span")
        logo.click()
        driver.switch_to_active_element
        signout = driver.find_element_by_xpath("//a[contains(.,'Sign out')]")
        signout.click()
        time.sleep(2)
        print "Go back to tms server console"
        driver.get("http://192.168.1.164/tms/default.aspx?pageId=79&ConfId=17747&View=true")
    
    def verify_meeting_rooms():
        print "View the meeting details"
        title_xpath = "//a[@id='ctl00_uxContent_ctl01_conferenceGrid_ctl02_viewButton']"
        title = driver.find_element_by_xpath(title_xpath)
        title.click()
        time.sleep(2)
        for mt_room in (new_mt_room_1, new_mt_room_2):
            try:
                xpath = "//nobr[contains(., '%s')]" % mt_room
                particpt = driver.find_element_by_xpath(xpath)
                if particpt.is_displayed():
                    print "%s is verified in participant list" % mt_room
            except:
                print "%s is not in the participant list" % mt_room
                verify_declined_email_received(mt_room)
    verify_meeting_rooms()
    
    
def verify_deleted_meeting():
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
            if meeting_title.is_displayed() and tomorrow == st_date:
                print "The meeting is still there, not deleted"
        except:
            print "Edited repeat meeting is not found, it is deleted"

# if __name__ == '__main__':
#     
#     login_tms_server.login_tms_server()
#     verify_created_repeat_meeting()
#     verify_edited_repeat_meetings()
#     verify_deleted_meeting()
#     driver.quit()