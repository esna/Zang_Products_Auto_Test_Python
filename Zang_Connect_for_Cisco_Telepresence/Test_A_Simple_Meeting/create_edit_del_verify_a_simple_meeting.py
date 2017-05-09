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
tmr_plus_one = datetime.date.today() + datetime.timedelta(days=2)
d1 = datetime.datetime.strptime("%s" % tmr, '%Y-%m-%d')
d2 = datetime.datetime.strptime("%s" % tmr_plus_one, '%Y-%m-%d')
tomorrow = datetime.date.strftime(d1, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
tom_plus_one = datetime.date.strftime(d2, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
fromtime = "12:00 PM"
untiltime = "1:00 PM"
title = 'Default meeting with single meeting room'
new_title = 'Default meeting is changed to WebEx CMR meeting'
meeting_room = 'test1'
new_mt_room = 'WebEx CMR meeting'
userid = ConfigSectionMap("Account")['essultn_id_2']
passwd = ConfigSectionMap("Account")['essultn_pwd']
guest1 = 'reidz@esna.com'
guest2 = 'esnaqc.testing@gmail.com'

class GmailAccountVerifyPy(unittest.TestCase):
    
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
                
        def create_simple_meeting():
            def go_to_google_calendar():
                print "Go to google calendar"
                driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
                driver.get("https://calendar.google.com/calendar/render?tab=mc#main_7")
                time.sleep(5)
            
            def create_meeting_from_calnedar():
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
                input_meeting_title()
                
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
                set_meeting_schedule()
                    
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
                    select_room = 'TMSUCREID - %s' % meeting_room
                    room_filter.send_keys(select_room)
                    return select_room
                    time.sleep(2)
                    print "Meeting room is selected"
                select_room = select_meeting_room()
                
                def save_created_meeting():
                    try:
                        xpath = "//span[contains(., '%s')]" % select_room
                        driver.find_element_by_xpath(xpath).click()
                        time.sleep(2)
                        print "Save the created meeting"
                        xpath = "//div[@class='goog-imageless-button-content'][contains(., 'Save')]"
                        save_btn = driver.find_element_by_xpath(xpath)
                        save_btn.click()
                        time.sleep(60)
                        print "Created meeting is saved"
                        print ''
                    except:
                        print "The meeting room is not available, meeting is not created."
                        print ''
                save_created_meeting()
                
            go_to_google_calendar()
            create_meeting_from_calnedar()
                
        def verify_created_meeting_details():
            def login_tms_server():
                url = '192.168.1.164/tms/default.aspx?pageId=77'
                driver.get('http://reidz@esna.main:Esnareid7@%s'% url)
                print "Login tms server and display the conference lsit"
                time.sleep(2)
            def verify_meeting_details():
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
                self.assertEqual(title, title_content)
                print "Meeting title is verified"
                self.assertEqual(tomorrow, st_date)
                self.assertEqual(tomorrow, ed_date)
                self.assertEqual(fromtime, st_time)
                self.assertEqual(untiltime, ed_time)
                print "Meeting date, start and end time are verified"
                self.assertEqual(meeting_room, mt_room)
                print "Meeting room is verified"
                print "The meeting details are exactly same with those in created meeting"
                print ''
            login_tms_server()
            verify_meeting_details()
            
        def edit_the_simple_meeting():
            def goto_google_calendar():
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
                xpath = "(//span[@class='ep-gc-icon ep-gc-icon-response'][@title='Yes'])[2]"
                remove_symbol = driver.find_element_by_xpath(xpath)
                remove_symbol.click()
                print "Old meeting room is removed"
                xpath = "//input[@title='Event title']"
                meeting_title = driver.find_element_by_xpath(xpath)
                meeting_title.clear()
                meeting_title.send_keys(new_title)
                print "Meeting title is changed to a new one"
                
            def change_meeting_room():
                xpath = "//span[@id='ui-ltsr-tab-1']"
                room_menu = driver.find_element_by_xpath(xpath)
                room_menu.click()
                time.sleep(2)
                xpath = "//input[@title='Search rooms']"
                room_filter = driver.find_element_by_xpath(xpath)
                room_filter.click()
                room_filter.clear()
#                 select_room = 'TMSUCREID - %s' % meeting_room
                select_room = new_mt_room
                room_filter.send_keys(select_room)
                time.sleep(2)
                print "New meeting room is selected"
                try:
                    select_room = 'TMSUCREID - %s' % new_mt_room
                    xpath = "//span[contains(., '%s')]" % select_room
                    driver.find_element_by_xpath(xpath).click()
                    time.sleep(2)
                    print "Meeting room is changed to %s" % select_room
                except:
                    print "The meeting room is not available, meeting is not created."
                    
            def add_guests():
                guests = driver.find_element_by_id("ui-ltsr-tab-0")
                guests.click()
                time.sleep(1)
                add_box = driver.find_element_by_xpath("//input[@title='Add guests']")
                for guests in (guest1, guest2):
                    add_box.clear()
                    add_box.send_keys(guests)
                    add_box.send_keys(Keys.RETURN)
                    time.sleep(2)
                print "Two new guests are added"
                
            def save_edited_meeting():
                xpath = "//div[@class='goog-imageless-button-content'][contains(., 'Save')]"
                save_btn = driver.find_element_by_xpath(xpath)
                save_btn.click()
                driver.switch_to_active_element()
                send_btn = driver.find_element_by_name('no')
                send_btn.click()
                time.sleep(60)
                print "Edited meeting is saved"
                print ''
            goto_google_calendar()
            change_meeting_title()
            change_meeting_room()
            add_guests()
            save_edited_meeting()
        
        def verify_edited_meeting_details():
            def login_tms_server():
                url = '192.168.1.164/tms/default.aspx?pageId=77'
                driver.get('http://reidz@esna.main:Esnareid7@%s'% url)
                print "Login tms server and display the conference lsit"
                time.sleep(2)
                
            def verify_meeting_details():
                WebEx_CMR = 'Externally Hosted Conference'
                values_list = []
                
                def locate_edited_meeting():
                    try:
                        xpath = "//a[contains(., '%s')]" % new_title
                        meeting_title = driver.find_element_by_xpath(xpath)
                        meeting_title.click()
                        print "Edited meeting is found"
                    except:
                        print "Edited meeting is not found"
                    time.sleep(1)
                    
                def verify_meeting_title():
                    xpath = "//td[@class='PropertyValue']"
        #             xpath = "%s/following-sibling::td[@class='PropertyValue']/span" % title_xpath
                    title_item = driver.find_elements_by_xpath(xpath)
                    for elem in title_item:
                        values_list.append(elem.text)
                    title_content = values_list[0]
                    self.assertEqual(new_title, title_content)
                    print "Changed meeting title is verified"
                    
                def verify_invited_guests():
                    for num in (2, 3, 4):
                        xpath = "//table[@id='ctl00_uxContent_ctl01_uxConferenceParticipants_participantGrid']/tbody/tr[%d]/td[2]/nobr" % num
                        particpt = driver.find_element_by_xpath(xpath)
                        room_or_partipant = particpt.text
                        if num == 2:
                            partipt = WebEx_CMR
                        elif num == 3:
                            partipt = "Reid Zhang [%s]" % guest1
                        elif num == 4:
                            partipt = "EsnaQC Testing [%s]" % guest2
                        else:
                            print "Meeting room or participant are not found"
                        self.assertEqual(partipt, room_or_partipant)
                    print "Changed meeting room and 2 intvited guests are verified"
                    print "The meeting details are exactly same with those in created meeting"
                    print ''
                locate_edited_meeting()
                verify_meeting_title()
                verify_invited_guests()
                
            login_tms_server()
            verify_meeting_details()
            
        def delete_created_meeting():
            print "Go to google calendar"
            driver.get("https://calendar.google.com/calendar/render?tab=mc#main_7")
            time.sleep(3)
            def locate_edited_meeting():
                try:
                    xpath = "//span[@class='chip-caption']"
                    fl_menu = driver.find_element_by_xpath(xpath)
                    fl_menu.click()
                    print "Found the edited meeting"
                except:
                    print 'The created meeting is not found'
                time.sleep(1)
            def delete_edited_meeting():
                driver.switch_to_active_element()
                xpath = "//div[@class='neb-footer']/span[2]/div[1]"
                del_btn = driver.find_element_by_xpath(xpath)
                del_btn.click()
                driver.switch_to_active_element()
                confirm_btn = driver.find_element_by_name("no")
                confirm_btn.click()
                print "The simple meeting is deleted from google calendar"
                print ''
                time.sleep(60)
            locate_edited_meeting()
            delete_edited_meeting()
            
        def verify_deleted_meeting():
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
            
            
        login_to_gmail_account()
#         create_simple_meeting()
#         verify_created_meeting_details()
#         edit_the_simple_meeting()
#         verify_edited_meeting_details()
#         delete_created_meeting()
#         verify_deleted_meeting()
        
        
#     def tearDown(self):
#         self.driver.quit()
        
        
if __name__ == '__main__':
    unittest.main()