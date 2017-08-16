'''
Created on Jul 24, 2017

@author: qcadmin
'''

import create_inst_mt_from_webex_icon
import create_inst_mt_from_sf_contacts
import time, re
from iLink_for_Webex_Testing.Salesforce import webex_account_login

url_mywebex = 'https://esna.webex.com/mw3200/mywebex/default.do?siteurl=esna&service=10'
toll_free_num = '1-855-244-8681 Call-in toll-free number (US/Canada)'
toll_number = '1-650-479-3207 Call-in toll number (US/Canada)'
# driver = create_instant_meetings.driver
topic_1 = create_inst_mt_from_webex_icon.topic_1
topic_2 = create_inst_mt_from_sf_contacts.topic_2
topic_3 = create_inst_mt_from_sf_contacts.topic_3
time_hrs = create_inst_mt_from_webex_icon.time_hrs
time_mins = create_inst_mt_from_webex_icon.time_mins
passwd_1 = create_inst_mt_from_webex_icon.passwd_1
passwd_2 = create_inst_mt_from_sf_contacts.passwd_2
passwd_3 = create_inst_mt_from_sf_contacts.passwd_3

driver = create_inst_mt_from_sf_contacts.driver

driver.get(url_mywebex)
driver.switch_to_frame('mainFrame')

webex_account_login.webex_account_login(driver)

def verify_meeting_data():
    print "Verify the created meeting's details"
    def verify_instant_meeting_webex_icon():
        def verify_meeting_title():
            try:
                driver.switch_to_frame('menu')
            except:
                driver.switch_to_default_content()
                driver.switch_to_frame('mainFrame')
                driver.switch_to_frame('menu')
            xpath = "//span[contains(.,'My Meetings')]"
            driver.find_element_by_xpath(xpath).click()
            driver.switch_to_default_content()
            driver.switch_to_frame('mainFrame')
            driver.switch_to_frame('main')
            xpath = "//a[@title='%s']" % topic_1
            mt_title = driver.find_element_by_xpath(xpath)
            mt_title.click()
            print "Meeting title is verified correct"
        verify_meeting_title()
        def verify_meeting_time():
            mt_period = driver.find_element_by_id('mc-txt-duration')
            assert time_hrs+' hour '+time_mins+' minutes' == mt_period.text
            print "Meeting duration is verified"
            time.sleep(2)
        verify_meeting_time()
        def verify_audio_connection():
            driver.find_element_by_id('mc-lnk-moreInfo').click()
            xpath1 = "//div[@id='mc-txt-teleconference']/p[2]"
            xpath2 = "//div[@id='mc-txt-teleconference']/p[3]"
            toll_free = driver.find_element_by_xpath(xpath1)
            toll_num = driver.find_element_by_xpath(xpath2)
            assert toll_free_num == toll_free.text
            assert toll_number == toll_num.text
            print "Audio connection numbers are verified"
            glo_call_nums = driver.find_element_by_link_text('Global call-in numbers')
            toll_free_restrict = driver.find_element_by_link_text('Show toll-free dialing restrictions')
            try:
                if glo_call_nums.is_displayed() and toll_free_restrict.is_displayed():
                    print "Global and toll free restrctions file links are displayed"
                else:
                    print "Global call numbers and/or toll free restriction file are not found"
            except:
                print "Specified xpath are not found"
        verify_audio_connection()
        def verify_password():
            pwd = driver.find_element_by_id('mc-txt-password')
            assert passwd_1 == pwd.text
            print "Meeting password is verified correct"
            print ''
        verify_password()
    
    def verify_inst_mt_sf_contact_classic():
        def verify_meeting_title():
            driver.switch_to_default_content()
            driver.switch_to_frame('mainFrame')
            driver.switch_to_frame('menu')
            xpath = "//span[contains(.,'My Meetings')]"
            driver.find_element_by_xpath(xpath).click()
            driver.switch_to_default_content()
            driver.switch_to_frame('mainFrame')
            driver.switch_to_frame('main')
            xpath = "//a[@title='%s']" % topic_2
            mt_title = driver.find_element_by_xpath(xpath)
            mt_title.click()
            print "Meeting title for %s is verified correct" % topic_2
        verify_meeting_title()
        
        def verify_meeting_time():
            mt_period = driver.find_element_by_id('mc-txt-duration')
            assert '20 minutes' == mt_period.text
            print "Meeting duration for %s is verified" % topic_2
            time.sleep(2)
        verify_meeting_time()
        
        def verify_audio_connection():
            driver.find_element_by_id('mc-lnk-moreInfo').click()
            time.sleep(1)
            audio = driver.find_element_by_id('mc-txt-teleconference')
            assert 'Use VoIP only' == audio.text
            print "Audio connection for %s is verified correct" % topic_2
        verify_audio_connection()
        
        def verify_password():
            pwd = driver.find_element_by_id('mc-txt-password')
            assert passwd_2 == pwd.text
            print "Meeting password for %s is verified correct" % topic_2
            print ''
            time.sleep(2)
        verify_password()
        
    def verify_inst_mt_sf_contact_lightning():
        def verify_meeting_title():
            driver.switch_to_default_content()
            driver.switch_to_frame('mainFrame')
            driver.switch_to_frame('menu')
            xpath = "//span[contains(.,'My Meetings')]"
            driver.find_element_by_xpath(xpath).click()
            driver.switch_to_default_content()
            driver.switch_to_frame('mainFrame')
            driver.switch_to_frame('main')
            xpath = "//a[@title='%s']" % topic_3
            mt_title = driver.find_element_by_xpath(xpath)
            mt_title.click()
            print "Meeting title for %s is verified correct" % topic_3
        verify_meeting_title()
        
        def verify_meeting_time():
            mt_period = driver.find_element_by_id('mc-txt-duration')
            assert '20 minutes' == mt_period.text
            print "Meeting duration for %s is verified" % topic_3
            time.sleep(2)
        verify_meeting_time()
        
        def verify_audio_connection():
            driver.find_element_by_id('mc-lnk-moreInfo').click()
            time.sleep(1)
            audio = driver.find_element_by_id('mc-txt-teleconference')
            assert 'Use VoIP only' == audio.text
            print "Audio connection for %s is verified correct" % topic_3
        verify_audio_connection()
        
        def verify_password():
            pwd = driver.find_element_by_id('mc-txt-password')
            assert passwd_3 == pwd.text
            print "Meeting password for %s is verified correct" % topic_3
            print ''
            time.sleep(2)
        verify_password()
        
    def delete_meeting_from_webex():
        def go_to_meeting_list():
            driver.switch_to_default_content()
            driver.switch_to_frame('mainFrame')
            driver.switch_to_frame('menu')
            xpath = "//span[contains(.,'My Meetings')]"
            driver.find_element_by_xpath(xpath).click()
            time.sleep(2)
            print "My Meetings link is clicked"
            driver.switch_to_default_content()
            driver.switch_to_frame('mainFrame')
#             driver.switch_to_frame('main')
        go_to_meeting_list()
        
    verify_instant_meeting_webex_icon()
    verify_inst_mt_sf_contact_classic()
    verify_inst_mt_sf_contact_lightning()   
    return driver
        
# webex_account_login()
# verify_meeting_data()

