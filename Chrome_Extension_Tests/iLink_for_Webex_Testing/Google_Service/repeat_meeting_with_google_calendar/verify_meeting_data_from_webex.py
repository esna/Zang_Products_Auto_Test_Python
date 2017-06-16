'''
Created on May 31, 2017

@author: qcadmin
'''
import create_repeat_meetings
import edit_repeat_meetings
from iLink_for_Webex_Testing import add_login_webex_extension
from selenium.webdriver.support.ui import Select
import datetime, time, re

url_mywebex = 'https://esna.webex.com/mw3200/mywebex/default.do?siteurl=esna&service=10'
url_gmail = 'https://mail.google.com'
url_calendar = 'https://calendar.google.com/calendar/render?tab=mc#main_7'
new_title = edit_repeat_meetings.new_title
new_fr_time = edit_repeat_meetings.new_fr_time
new_utl_time = edit_repeat_meetings.new_utl_time
tom_plus_one = edit_repeat_meetings.tom_plus_one
tmr_plus_one = edit_repeat_meetings.tmr_plus_one
time_taken = '1 hour'
passwd = edit_repeat_meetings.passwd
audio_type = edit_repeat_meetings.audio_type
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
    for num in range(0, 5):
        xpath = "//a[@title='%s'][@number='%d']" % (new_title, num)
        mt_title = driver.find_element_by_xpath(xpath)
        if mt_title.is_displayed():
            print "Meeting on day %d is found" % (num+1)
    print "Repeat meetings are verified scheduled for %d days" % (num+1)
    print "Meeting title is verified edited successfully"

def verify_meeting_time():
    for num in range(1, 6):
        xpath = "(//td[contains(.,'%s')])[%d]" % (new_fr_time.lower(), num)
        mt_st_time = driver.find_element_by_xpath(xpath)
        i = num+1
        v_date = datetime.date.today() + datetime.timedelta(days = i)
        input_tm = v_date.strftime("%b %d, %Y ").lstrip("0").replace(" 0", " ")
        input_time = input_tm + new_fr_time.lower()
        get_mt_time = mt_st_time.text
        print "Meeting start time on day %d is: %s" %  (num, get_mt_time)
        assert input_time == get_mt_time
    print "Meeting start time for 5 days are verified edited correct"
    
def verify_changed_data_from_webex_icon():
    xpath = "//a[@title='%s'][@number='0']" % (new_title)
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
    print audio_type
    print audio_tp.text
    assert audio_type == audio_tp.text
    print "Meeting audio type is verified correct"
    pwd = driver.find_element_by_id('mc-txt-password')
    assert passwd == pwd.text
    print "Meeting password is verifid correct"
    

webex_account_login()
verify_meeting_title()
verify_meeting_time()
verify_changed_data_from_webex_icon()