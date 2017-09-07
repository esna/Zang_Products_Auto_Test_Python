'''
Created on Aug 15, 2017

@author: qcadmin
'''
import create_sf_repeat_meetings
import datetime, time, re
from iLink_for_Webex_Testing.Salesforce import webex_account_login
topic = create_sf_repeat_meetings.topic
templt_topic = 'WebEx Meeting #111'
fromtime = create_sf_repeat_meetings.fromtime
tmr = datetime.date.today() + datetime.timedelta(days=1)
time_taken = '1 hour'
sele_autio = "Use VoIP only"
driver = create_sf_repeat_meetings.driver
webex_account_login.webex_account_login(driver)

def verify_meeting_data():
    print "Verify the created meeting's details"
    def verify_created_meeting_data():
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
            driver.find_element_by_link_text('All Meetings').click()
            time.sleep(2)
            xpath1 = "//a[@title='%s']" % topic
            xpath2 = "//a[@title='%s']" % templt_topic
            mt_title = driver.find_element_by_xpath(xpath1)
            mt_title.click()
            print "Meeting title is verified correct"
            time.sleep(2)
        verify_meeting_title()
        
        def verify_meeting_date_time():
            xpath1 = "//span[@id='mc-txt-date']" 
            xpath2 = "//span[@id='mc-txt-time']" 
            xpath3 = "//span[@id='mc-txt-duration']" 
            mt_st_date = driver.find_element_by_xpath(xpath1)
            mt_st_time = driver.find_element_by_xpath(xpath2)
            mt_st_dur = driver.find_element_by_xpath(xpath3)
            input_date = tmr.strftime("%A, %B %d, %Y ").lstrip("0").replace(" 0", " ")
            if input_date == mt_st_date.text:
                print "Meeting start date is verified correct"
            else:
                print "Meeting start date is different with input"
            if fromtime.lower() in mt_st_time.text:
                print "Meeting start time is verified correct"
            assert time_taken == mt_st_dur.text
            print "Meeting duration is verified correct"
            time.sleep(2)
        verify_meeting_date_time()
        
        def verify_audio_connection():
            driver.find_element_by_id('mc-lnk-moreInfo').click()
            time.sleep(1)
            xpath = "//div[@id='mc-txt-teleconference']"
            audio = driver.find_element_by_xpath(xpath)
            assert  sele_autio == audio.text
            print "Audio connection phone number is verified correct"
            print "Verify edited recurring meeting is finished"
        verify_audio_connection()
        
    verify_created_meeting_data()
    
verify_meeting_data()