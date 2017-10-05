'''
Created on Jun 6, 2017

@author: qcadmin
'''
from iLink_for_Webex_Testing import add_login_webex_extension
from selenium.webdriver.support.ui import Select
import create_repeat_meetings
import time, datetime
from test.test_xml_etree import xpath_tokenizer

url_mywebex = 'https://esna.webex.com/mw3200/mywebex/default.do?siteurl=esna&service=10'
url_o365 = "https://login.microsoftonline.com/"
title = create_repeat_meetings.title
new_title = 'edited_o365_scheduled_repeat_meetings'
tom_plus_1 = datetime.date.today() + datetime.timedelta(days = 2)
tom_plus_6 = datetime.date.today() + datetime.timedelta(days = 6)
input_dt = tom_plus_1.strftime("%B %d, %Y")
end_dt = tom_plus_6.strftime("%B %d, %Y")
new_fr_time = "1:00 PM"
new_utl_time = "1:30 PM"
audio_type = 'WebEx Audio'

driver = add_login_webex_extension.driver

def go_to_O365_calendar():
#     print "Go to O365 account"
#     driver.get(url_o365)
#     time.sleep(3)
#     driver.find_element_by_id('O365_MainLink_NavMenu').click()
#     print "Click menu"
#     time.sleep(8)
#     print "Click calendar icon"
#     xpath = "//a[@id='O365_AppTile_Calendar']/div/span"
#     cal = driver.find_element_by_xpath(xpath)
#     cal.click()
#     time.sleep(30)
#     print "Delete the repeat meetings from calendar"
    cal_url = 'https://outlook.office365.com/owa/?realm=esnatech.onmicrosoft.com&exsvurl=1&ll-cc=1033&modurl=1&path=/calendar'
    print "Go to o365 calendar"
    driver.get(cal_url)
    time.sleep(20)

def locate_created_meeting():
    xpath = "//span[contains(., '%s')]" % title
    mt_label = driver.find_element_by_xpath(xpath)
    print "Found the edited meeting"
    mt_label.click()
    print "Click the meeting label"
    time.sleep(1)
    driver.switch_to_active_element
    xpath = "//span[contains(.,'Edit')]"
    edit = driver.find_element_by_xpath(xpath)
    print "Click Edit button"
    edit.click()
    print "Choose edit series"
    driver.find_element_by_xpath("//span[contains(.,'Edit series')]").click()
    time.sleep(3)
    
def change_meeting_title():
    xpath = "//input[@aria-label='Add a title for the event']"
    mt_title = driver.find_element_by_xpath(xpath)
    mt_title.clear()
    mt_title.send_keys(new_title)
    print "Meeting title is changed"

def edit_meeting_date_time():
    xpath = "//span[@class='_dx_5 owaimg ms-Icon--calendar ms-icon-tall-glyph ms-icon-font-size-16 ms-fcl-ns-b']"
    st_cal = driver.find_element_by_xpath(xpath)
    st_cal.click()
    time.sleep(1)
    print "Click Calendar Icon"
    cal_xpath = "//div[@class='_dx_6 ms-font-s ms-fwt-r ms-bgc-w contextMenuDropShadow']"
    tom_xpath = "%s//div/abbr[contains(@aria-label,'%s')]"% (cal_xpath, input_dt)
    tom_plus_1 = driver.find_element_by_xpath(tom_xpath)
    print "Input meeeting date"
    tom_plus_1.click()
    xpath = "//span[@class='_dx_4 ms-fwt-sl ms-font-s']"
    print "Input meeting time"
    from_time = driver.find_element_by_xpath("//input[@aria-label = 'start time']")
    until_time = driver.find_element_by_xpath("//input[@aria-label = 'end time']")
    from_time.clear()
    from_time.send_keys(new_fr_time)
    until_time.clear()
    until_time.send_keys(new_utl_time)
    print "Meeting schedule is set"
    time.sleep(2)

def change_repeat_cycle():
    xpath = "//button[@aria-labelledby='MeetingCompose.RepeatLabel MeetingCompose.RepeatDescriptionLabel']/div[2]/span"
    sel_btn = driver.find_element_by_xpath(xpath)
    print "Click the repeat period selector button"
    sel_btn.click()
    time.sleep(2)
    xpath = "//span[contains(.,'Every day')]"
    eve_day = driver.find_element_by_xpath(xpath)
    eve_day.click()
    print "Selected Every day repeat"
    time.sleep(2)
    repeat_cal_xpath = "(//div[@class='RepeatDatePicker'])[2]"
    end_dt_cal_xpath = "%s/div/button/span[2]" % repeat_cal_xpath
    end_dt_sel = driver.find_element_by_xpath(end_dt_cal_xpath)
    end_dt_sel.click()
    print "Click repeat end date calendar"
    time.sleep(2)
    rep_cal_xpath = "(//div[@class='_dx_h _dx_j ms-font-s ms-font-weight-semilight ms-font-color-neutralPrimary'])[3]"
    end_dt_xpath = "%s//div//abbr[contains(@aria-label,'%s')][contains(@style,'width: 30px')]"% (rep_cal_xpath, end_dt)
    end_day = driver.find_element_by_xpath(end_dt_xpath)
    print "Repeat meeting end date selected"
    end_day.click()
    print "Repeating cycle is set"
    
def edit_meeting_items_with_webex_icon():
    create_btn = driver.find_element_by_id('wexButtonEdit')
    create_btn.click()
    print "Click webex edit button"
    time.sleep(2)
    driver.switch_to_frame('frameCreateWebex')
    audio = Select(driver.find_element_by_id('id_wexAudio'))
    audio.select_by_visible_text(audio_type)
    print "Change the audio type to WebEx Audio"
    driver.find_element_by_id('createWebexSpan').click()
    print "Meeting is edited with webex icon"
    time.sleep(5)
    
def save_meeting_on_o365_calendar():
    driver.switch_to_default_content
    xpath = "//span[contains(.,'Save')]"
    save_btn = driver.find_element_by_xpath(xpath)
    save_btn.click()
    print "Save button is clicked"
    time.sleep(2)
    driver.switch_to_active_element()
    xpath = "//span[@class='_db_b ms-font-m ms-font-weight-semibold'][contains(.,'Save')]"
    confirm = driver.find_element_by_xpath(xpath)
    confirm.click()
    print "Edited repeat meeting is saved on calendar"
    time.sleep(5)
    
# go_to_O365_calendar()
# locate_created_meeting()
# change_meeting_title()
# edit_meeting_date_time()
# change_repeat_cycle()
# edit_meeting_items_with_webex_icon()
# save_meeting_on_o365_calendar()
    
    