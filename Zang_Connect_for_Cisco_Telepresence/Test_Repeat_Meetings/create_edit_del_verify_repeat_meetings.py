'''
Created on Feb 6, 2017
@author: qcadmin
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import unittest, time, re
import datetime
import time
import ConfigParser, getopt, os, subprocess, sys



Config = ConfigParser.ConfigParser()
#Config.read("D:\escloud\escloud\QC_Auto_Test_Python\OnEsna_Testing\onesna_testing.ini")
Config.read("../configuration.ini")

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        #print option
        try:
            dict1[option] = Config.get(section, option)
            def DebugPrint(msg):
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

tmr = datetime.date.today() + datetime.timedelta(days=1)
d1 = datetime.datetime.strptime("%s" % tmr, '%Y-%m-%d')
# tomorrow = datetime.date.strftime(d1, "%m/%d/%Y").lstrip("0").replace(" 0", " ")
tomorrow = datetime.date.strftime(d1, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
tmr_plus_one = datetime.date.today() + datetime.timedelta(days=2)
d2 = datetime.datetime.strptime("%s" % tmr_plus_one, '%Y-%m-%d')
tom_plus_one = datetime.date.strftime(d2, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
fromtime = "2:00 PM"
untiltime = "3:00 PM"
new_from_time = "1:00 PM"
new_untl_time = "2:00 PM"
ori_title = 'Repeat meeting, two meeting rooms, repeat daily for 5 times'
new_title = "Repeat meeting edited, three meeting rooms, start time 1:00pm"
meeting_room_1 = 'WebEx meeting'
meeting_room_2 = 'No Name (192.168.1.38)'
new_mt_room_1 = 'Back Boardroom EX90'
new_mt_room_2 = 'new intern testing room'
room_list_1 = (meeting_room_1, meeting_room_2)
room_list_2 = (new_mt_room_1, new_mt_room_2)
userid = ConfigSectionMap("Account")['essultn_id_2']
passwd = ConfigSectionMap("Account")['essultn_pwd']
guest1 = 'reidz@esna.com'
guest2 = 'esnaqc.testing@gmail.com'

date_list = []
for i in range(1, 6):
    tmr = datetime.date.today() + datetime.timedelta(days=i)
    di = datetime.datetime.strptime("%s" % tmr, '%Y-%m-%d')
    date_got = datetime.date.strftime(di, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
    date_list.append(date_got)

class Zang_Connect_for_Cisco_Telepresence_Test(unittest.TestCase):
    
    def setUp(self):
        onusing_browser = ConfigSectionMap("Browser")['onusing']
        if onusing_browser == "1":
            self.driver = webdriver.Firefox()
        elif onusing_browser == "2":
            self.driver = webdriver.Chrome()
        else:
            print "We don't support other browsers currently."
        self.driver.implicitly_wait(15)
        self.base_url = "https://www.google.ca/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_gmail_account_login(self):
        driver = self.driver
        def login_to_gmail_account():
            driver.get(self.base_url + "/?gfe_rd=cr&ei=7oUPU7rNBcOC8QfL9ID4Cw")
            driver.find_element_by_id("gb_70").click()
            time.sleep(5)
            def google_account_login_new_interface():
                email = driver.find_element_by_id("identifierId")
                email.clear()
                email.send_keys(userid)
                time.sleep(1)
                xpath = "//div[@id='identifierNext']/content/span"
                next_btn = driver.find_element_by_xpath(xpath)
                next_btn.click()
                time.sleep(3)
                Passwd = driver.find_element_by_name("password")
                Passwd.clear()
                Passwd.send_keys(passwd)
                xpath = "//div[@id='passwordNext']/content/span"
                next_btn = driver.find_element_by_xpath(xpath)
                next_btn.click()
                time.sleep(3)
            def google_account_login_old_interface():
                email = driver.find_element_by_id("Email")
                email.clear()
                email.send_keys(userid)
                time.sleep(1)
                xpath = "//input[@id='next']"
                next_btn = driver.find_element_by_xpath(xpath)
                next_btn.click()
                time.sleep(3)
                Passwd = driver.find_element_by_id("Passwd")
                Passwd.clear()
                Passwd.send_keys(passwd)
                signin_btn = driver.find_element_by_id("signIn")
                signin_btn.click()
                time.sleep(2)
                gmail = driver.find_element_by_link_text("Mail")
                gmail.click()
                print "Account for %s is logged in" % userid
                time.sleep(5)    
            try:
                google_account_login_new_interface()
            except:
                google_account_login_old_interface()
        
        def create_repeat_meeting_from_calnedar():
            def go_to_google_calendar():
                print "Go to google calendar"
                driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
                driver.get("https://calendar.google.com/calendar/render?tab=mc#main_7")
                time.sleep(5)
            
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
                    
            def save_meeting():
                xpath = "//div[@class='goog-imageless-button-content'][contains(., 'Save')]"
                save_btn = driver.find_element_by_xpath(xpath)
                save_btn.click()
                print "Scheduled repeat meeting is saved"
                time.sleep(60)
                
            go_to_google_calendar()
            input_meeting_title()
            set_meeting_schedule()
            set_repeating_cycle()
            select_meeting_rooms()
            save_meeting()
            
        def verify_created_repeat_meeting():
            def login_tms_server():
                url = '192.168.1.164/tms/default.aspx?pageId=77'
                driver.get('http://reidz@esna.main:Esnareid7@%s'% url)
                print "Login tms server and display the conference lsit"
                time.sleep(2)
            login_tms_server()
            
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
                        self.assertEqual(ori_title, title_content)
                        print "Meeting title on day %d is exactly same with that created" % day_num
                    verify_meeting_title()
                    
                    def verify_meeting_date():
                        date_xpath = "//table[@id='ctl00_uxContent_ctl01_conferenceGrid']/tbody/tr[%d]/td[5]/span" % i
                        st_date = driver.find_element_by_xpath(date_xpath)
                        ori_st_date = date_list[ori_date]
                        st_date = st_date.text
                        self.assertEqual(st_date, ori_st_date)
                        print "Meeting start date on day %d is verified" % day_num
                    verify_meeting_date()
                    
                    def verify_meeting_start_time():
                        st_time_xpath = "//table[@id='ctl00_uxContent_ctl01_conferenceGrid']/tbody/tr[%d]/td[6]/span" % i
                        st_time = driver.find_element_by_xpath(st_time_xpath)
                        st_time = st_time.text
                        self.assertEqual(fromtime, st_time)
                        print "Meeting start time on day %d is verified" % day_num
                    verify_meeting_start_time()
                    
                    def verify_meeting_end_time():
                        ed_time_xpath = "//table[@id='ctl00_uxContent_ctl01_conferenceGrid']/tbody/tr[%d]/td[7]/span" % i
                        ed_time = driver.find_element_by_xpath(ed_time_xpath)
                        ed_time = ed_time.text
                        self.assertEqual(untiltime, ed_time)
                        print "Meeting end time on day %d is verified" % day_num
                        print ''
                    verify_meeting_end_time()
                    day_num += 1
                    ori_date += 1
            verify_meeting_title_date_time()
            
            def verify_meeting_rooms():
                print "View the meeting details"
                title_xpath = "//a[@id='ctl00_uxContent_ctl01_conferenceGrid_ctl02_viewButton']"
                title = driver.find_element_by_xpath(title_xpath)
                title.click()
                time.sleep(2)
                xpath = "//nobr[contains(., 'Cisco WebEx Meeting')]"
                webex = driver.find_element_by_xpath(xpath)
                if webex.is_displayed():
                    print "%s is verified in participant list" % meeting_room_1
                else:
                    print "%s is not found in participant list" % meeting_room_1
                xpath = "//font[contains(., '%s')]" % meeting_room_2
                mt_room = driver.find_element_by_xpath(xpath)
                if mt_room.is_displayed():
                    print "%s is verified in participant list" % meeting_room_2
                else:
                    print "%s is not found in participant list" % meeting_room_2
            verify_meeting_rooms()

           
        def edit_created_repeat_meetings():
            
            def go_to_google_calendar():
                driver.get("https://calendar.google.com/calendar/render?tab=mc#main_7")
                print "Go to google calendar"
                time.sleep(3)
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
            
            def change_meeting_title():
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
                print "Meeting schedule is set"
                
            def change_meeting_room():
                """remove webex meeting"""
                xpath = "//div[@aria-label='TMSUCREID - WebEx meeting, accepted']/div/div/span[2]"
                remove_icon = driver.find_element_by_xpath(xpath)
                remove_icon.click()
                print "Webex meeting is removed"
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
                time.sleep(60)
            go_to_google_calendar()
            change_meeting_title()
            change_meeting_time()
            change_meeting_room()
            save_edited_meeting()
        
        
        def verify_edited_repeat_meeting():
            def login_tms_server():
                url = '192.168.1.164/tms/default.aspx?pageId=77'
                driver.get('http://reidz@esna.main:Esnareid7@%s'% url)
                print "Login tms server and display the conference lsit"
                time.sleep(2)
            login_tms_server()
            
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
                        self.assertEqual(new_title, title_content)
                        print "Meeting title on day %d is exactly same with that created" % day_num
                    verify_meeting_title()
                    
                    def verify_meeting_start_time():
                        st_time_xpath = "//table[@id='ctl00_uxContent_ctl01_conferenceGrid']/tbody/tr[%d]/td[6]/span" % i
                        st_time = driver.find_element_by_xpath(st_time_xpath)
                        st_time = st_time.text
                        self.assertEqual(new_from_time, st_time)
                        print "Meeting start time on day %d is verified" % day_num
                    verify_meeting_start_time()
                    
                    def verify_meeting_end_time():
                        ed_time_xpath = "//table[@id='ctl00_uxContent_ctl01_conferenceGrid']/tbody/tr[%d]/td[7]/span" % i
                        ed_time = driver.find_element_by_xpath(ed_time_xpath)
                        ed_time = ed_time.text
                        self.assertEqual(new_untl_time, ed_time)
                        print "Meeting end time on day %d is verified" % day_num
                        print ''
                    verify_meeting_end_time()
                    day_num += 1
                    ori_date += 1
            verify_meeting_title_date_time()
            
            def verify_meeting_rooms():
                print "View the meeting details"
                title_xpath = "//a[@id='ctl00_uxContent_ctl01_conferenceGrid_ctl02_viewButton']"
                title = driver.find_element_by_xpath(title_xpath)
                title.click()
                time.sleep(2)
                for mt_room in (meeting_room_2, new_mt_room_1, new_mt_room_2):
                    xpath = "//nobr[contains(., '%s')]" % mt_room
                    webex = driver.find_element_by_xpath(xpath)
                    if webex.is_displayed():
                        print "%s is verified in participant list" % mt_room
                    else:
                        print "%s is not found in participant list" % mt_room
            verify_meeting_rooms()
        
        def delete_edited_repeat_meeting():
            def go_to_google_calendar():
                driver.get("https://calendar.google.com/calendar/render?tab=mc#main_7")
                print "Go to google calendar"
                time.sleep(3)
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
                
            def delete_meeting():
                driver.switch_to_active_element()
                xpath = "//div[@class='neb-footer']/span[2]/div[1]"
                del_btn = driver.find_element_by_xpath(xpath)
                del_btn.click()
                driver.switch_to_active_element()
                driver.find_element_by_xpath("(//td[@class='ep-es-button-cell']/div)[3]").click()
                driver.switch_to_active_element()
                confirm_btn = driver.find_element_by_name("no")
                confirm_btn.click()
                print "The simple meeting is deleted from google calendar"
                print ''
                time.sleep(60)
            go_to_google_calendar()
            delete_meeting()
            
        def verify_deleted_repeat_meeting():
            def login_tms_server():
                print "Go to tms server"
                url = '192.168.1.164/tms/default.aspx?pageId=77'
                driver.get('http://reidz@esna.main:Esnareid7@%s'% url)
                time.sleep(2)
            def verify_meeting_deleted():
                try:
                    xpath = "//td[contains(., 'No results found. Try widening your search by using fewer criteria.')]"
                    no_result = driver.find_element_by_xpath(xpath)
                    if no_result.is_displayed():
                        print "No meeting list is diaplyed, the edited meeting is deleted"
                    else:
                        print "A meeting list is displayed"
                except:
                    for j in range(2, 7):
                        title_xpath = "//table[@id='ctl00_uxContent_ctl01_conferenceGrid']/tbody/tr[%d]/td[4]/div/div/a" % j
                        title = driver.find_element_by_xpath(title_xpath)
                        title_content = title.text
                        if title_content == new_title:
                            print "Repeat meeting still exists"
                        else:
                            print "Repeat meetging is not found, has been deleted"
                    try:
                        xpath = "//a[contains(., '%s')]" % new_title
                        meeting_title = driver.find_element_by_xpath(xpath)
                        xpath = "//span[@id='ctl00_uxContent_ctl01_conferenceGrid_ctl02_StartDate']"
                        start_date = driver.find_element_by_xpath(xpath)
                        st_date = start_date.text
                        self.assertEqual(tomorrow, st_date)
                        if meeting_title.is_displayed():
                            print "The meeting is still there, not deleted"
                        else:
                            print "Edited meeting is not found in meeting list, it was deleted"
                    except:
                        print "Some error occurred"
            login_tms_server()
            verify_meeting_deleted()
         
         
#         login_to_gmail_account()
#         create_repeat_meeting_from_calnedar()
#         verify_created_repeat_meeting()
#         edit_created_repeat_meetings()
#         verify_edited_repeat_meeting()
#         delete_edited_repeat_meeting()
        verify_deleted_repeat_meeting()
        
        
        
        
if __name__ == '__main__':
    unittest.main()