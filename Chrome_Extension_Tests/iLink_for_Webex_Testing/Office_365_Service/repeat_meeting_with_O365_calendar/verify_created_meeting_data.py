'''
Created on May 31, 2017

@author: qcadmin
'''
import create_repeat_meetings
from iLink_for_Webex_Testing import add_login_webex_extension
from selenium.webdriver.support.ui import Select
import datetime, time, re

url_mywebex = 'https://esna.webex.com/mw3200/mywebex/default.do?siteurl=esna&service=10'
url_calendar = 'https://calendar.google.com/calendar/render?tab=mc#main_7'
title = create_repeat_meetings.title
input_dt = create_repeat_meetings.input_dt
end_dt = create_repeat_meetings.end_dt
fromtime = create_repeat_meetings.fromtime
untiltime = create_repeat_meetings.untiltime
time_taken = '1 hour'
passwd = create_repeat_meetings.passwd
audio_type = 'Use VoIP only'
host_name = 'Reid Zhang'
driver = add_login_webex_extension.driver

def webex_account_login():
    driver.get(url_mywebex)
    time.sleep(2)
    driver.switch_to_frame('mainFrame')
    user_id = driver.find_element_by_id('mwx-ipt-username')
    user_id.click()
    user_id.send_keys('reidz')
    print "Input user id"
    passwd = driver.find_element_by_id('mwx-ipt-password')
    passwd.click()
    passwd.send_keys('Zang123!')
    time.sleep(2)
    print "Input password"
    driver.find_element_by_id('mwx-btn-logon').click()
    print "Webex account is logged in"
    time.sleep(2)

def verify_meeting_title():
    driver.switch_to_frame('menu')
    xpath = "//span[contains(.,'My Meetings')]"
    driver.find_element_by_xpath(xpath).click()
    driver.switch_to_default_content()
    driver.switch_to_frame('mainFrame')
    driver.switch_to_frame('main')
    driver.find_element_by_id('wcc-lnk-search').click()
    time.sleep(1)
    for num in range(0, 3):
        xpath = "//a[@title='%s'][@number='%d']" % (title, num)
        mt_title = driver.find_element_by_xpath(xpath)
        if mt_title.is_displayed():
            print "Meeting on day %d is found" % (num+1)
    print "Repeat meetings are verified scheduled for %d days" % (num+1)
    print "Meeting title is verified edited successfully"

def verify_meeting_time():
    for num in range(1, 4):
        xpath = "(//td[contains(.,'%s')])[%d]" % (fromtime.lower(), num)
        mt_st_time = driver.find_element_by_xpath(xpath)
        i = num
        v_date = datetime.date.today() + datetime.timedelta(days = i)
        input_tm = v_date.strftime("%b %d, %Y ").lstrip("0").replace(" 0", " ")
        input_time = input_tm + fromtime.lower()
        get_mt_time = mt_st_time.text
        print "Meeting start time on day %d is: %s" %  (num, get_mt_time)
        assert input_time == get_mt_time
    print "Meeting start time for %d days are verified edited correct" % num
    
def verify_meeting_data_from_webex_icon():
    xpath = "//a[@title='%s'][@number='0']" % (title)
    mt_title = driver.find_element_by_xpath(xpath)
    mt_title.click()
    mt_period = driver.find_element_by_id('mc-txt-duration')
    get_time_period = mt_period.text
    assert time_taken == get_time_period
    print "Meeting duration is verified correct"
    time.sleep(2)
    driver.find_element_by_id('mc-lnk-moreInfo').click()
    time.sleep(1)
    audio_tp = driver.find_element_by_id('mc-txt-teleconference')
    assert audio_type == audio_tp.text
    print "Meeting audio type is verified correct"
    host = driver.find_element_by_id('mc-txt-hostname')
    hostname = host.text
    assert 'Host: ' + host_name == hostname
    print "Meeting host is verified correct"
    al_host = driver.find_element_by_id('mc-txt-alternateHost')
    al_host_name = al_host.text
    assert host_name == al_host_name
    print "Meeting alternate host is verified correct"
    pwd = driver.find_element_by_id('mc-txt-password')
    assert passwd == pwd.text
    print "Meeting password is verifid correct"
    

# webex_account_login()
# verify_meeting_title()
# verify_meeting_time()
# verify_meeting_data_from_webex_icon()