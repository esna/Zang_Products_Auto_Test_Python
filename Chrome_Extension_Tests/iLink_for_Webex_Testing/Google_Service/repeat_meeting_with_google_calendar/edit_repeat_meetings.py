'''
Created on May 31, 2017

@author: qcadmin
'''
# -*- coding: utf-8 -*-
import create_repeat_meetings
from iLink_for_Webex_Testing import add_login_webex_extension
from selenium.webdriver.support.ui import Select
import datetime, time

tmr_plus_one = datetime.date.today() + datetime.timedelta(days=2)
d2 = datetime.datetime.strptime("%s" % tmr_plus_one, '%Y-%m-%d')
tom_plus_one = datetime.date.strftime(d2, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
new_fr_time = "1:00 PM"
new_utl_time = "2:00 PM"
title = create_repeat_meetings.title
new_title = 'edited repeat meetings - change date, time and audio'
audio_type = 'None'
en_ex_tone = 'Announce name'
passwd = '2222b'

driver = add_login_webex_extension.driver

def go_to_goolge_calendar():
    create_repeat_meetings.go_to_google_mail_calendar()

def change_meeting_title():
    try:
        xpath = "//span[contains(., '%s')]" % title
        edt_meeting = driver.find_element_by_xpath(xpath)
        print "Found the created meeting"
        edt_meeting.click()
        print "Meeting link is clicked"
        time.sleep(2)
    except:
        print 'The created meeting is not found'
    xpath = "//input[@title='Event title']"
    meeting_title = driver.find_element_by_xpath(xpath)
    meeting_title.clear()
    meeting_title.send_keys(new_title)
    print "Meeting title is changed to a new one"
    
def change_meeting_date_time():
    from_date = driver.find_element_by_xpath("//input[@title = 'From date']")
    until_date = driver.find_element_by_xpath("//input[@title = 'Until date']")
    from_time = driver.find_element_by_xpath("//input[@title = 'From time']")
    until_time = driver.find_element_by_xpath("//input[@title = 'Until time']")
    from_date.clear()
    from_date.send_keys(tom_plus_one)
    until_date.clear()
    until_date.send_keys(tom_plus_one)
    from_time.clear()
    from_time.send_keys(new_fr_time)
    until_time.clear()
    until_time.send_keys(new_utl_time)
    print "Meeting schedule is changed"
    print ''
    
def change_meeting_type_audio_with_webex_icon():
    driver.find_element_by_id('webex0edit').click()
    time.sleep(3)
    driver.switch_to_frame('frameCreateWebex')
    audio = Select(driver.find_element_by_id('id_wexAudio'))
    audio.select_by_visible_text(audio_type)
    print "Audio tyoe is selected as %s" % audio_type
#     tone = Select(driver.find_element_by_id('id_wexTone'))
#     tone.select_by_visible_text(en_ex_tone)
#     print "Entry/exit tone is selected as %s" % en_ex_tone
    pwd = driver.find_element_by_id('id_txtPin')
    pwd.clear()
    pwd.send_keys(passwd)
    driver.find_element_by_id('createWebexSpan').click()
    print "Click Done button, webex items are edited"
    time.sleep(2)
    
def save_edited_repeat_meetings():
    xpath = "//div[@class='goog-imageless-button-content'][contains(., 'Save')]"
    save_btn = driver.find_element_by_xpath(xpath)
    save_btn.click()
    driver.switch_to_active_element()
    driver.find_element_by_xpath("(//td[@class='ep-es-button-cell']/div)[3]").click()
    print "Edited meeting is saved"
    print ''
    
# go_to_goolge_calendar()
# change_meeting_title()
# change_meeting_date_time()
# change_meeting_type_audio_with_webex_icon()
# save_edited_repeat_meetings()

    