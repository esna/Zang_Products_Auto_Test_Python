from iLink_for_Webex_Testing import add_login_webex_extension
from selenium.webdriver.support.ui import Select
import datetime, time

tmr = datetime.date.today() + datetime.timedelta(days=1)
tmr_plus_one = datetime.date.today() + datetime.timedelta(days=2)
d1 = datetime.datetime.strptime("%s" % tmr, '%Y-%m-%d')
d2 = datetime.datetime.strptime("%s" % tmr_plus_one, '%Y-%m-%d')
tomorrow = datetime.date.strftime(d1, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
tom_plus_one = datetime.date.strftime(d2, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
fromtime = "1:00 PM"
untiltime = "2:00 PM"
title = "Repeat meeting from google calendar - daily repeat for 3 times"
rept_fq = 3
reid_tem = 'reid test template'
tel_num = '905-707-9700'

add_login_webex_extension.login_ext_with_google()
time.sleep(10)
add_login_webex_extension.input_esna_webex_password()

driver = add_login_webex_extension.driver


def go_to_google_mail_calendar():
    print "Go to gmail account"
    driver.get('https://mail.google.com')
    time.sleep(5)
    print "Go to google calendar"
    driver.get("https://calendar.google.com/calendar/render?tab=mc#main_7")
    time.sleep(5)

def create_repeat_meeging():
    xpath = "//div[@id='createEventButtonContainer']//div[@class='goog-imageless-button-content']"
    create_btn = driver.find_element_by_xpath(xpath)
    create_btn.click()
    print "Click create button"
    time.sleep(5)
    
def input_meeting_title():
    xpath = "//div[@class='ui-sch ep-title']/input"
    create_btn = driver.find_element_by_xpath(xpath)
    create_btn.click()
    print "Input meeting title"
    xpath = "//input[@title='Event title']"
    meeting_title = driver.find_element_by_xpath(xpath)
    meeting_title.clear()
    meeting_title.send_keys(title)
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
    xpath = "//input[contains(@id,'endson_count_input')]"
    occu_fre = driver.find_element_by_xpath(xpath)
    occu_fre.clear()
    occu_fre.send_keys(rept_fq)
    xpath = "//td[@class='ep-rec-buttons-padding']/div/div"
    time.sleep(2)
    done_btn = driver.find_element_by_xpath(xpath)
    done_btn.click()
    print "Repeating cycle is set to daily for 3 times"
    
def save_meeting():
    driver.find_element_by_id('webex0addtext').click()
    print "Click webex meeting icon"
    time.sleep(2)
    driver.switch_to_frame('frameCreateWebex')
    templt = Select(driver.find_element_by_id('comboTemplates'))
    templt.select_by_visible_text(reid_tem)
    print "Select %s" % reid_tem
    aud_tp = Select(driver.find_element_by_id('id_wexAudio'))
    aud_tp.select_by_value('OTHER')
    print "Select audio type as Other"
    phone_num = driver.find_element_by_id('id_wexOtherTeleconfOptions')
    phone_num.clear()
    phone_num.send_keys(tel_num)
    print "Input phone number %s" % tel_num
    driver.find_element_by_id('createWebexSpan').click()
    print "Create meeting button is clicked"
    time.sleep(1)
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(1)
    xpath = "//div[@class='goog-imageless-button-content'][contains(., 'Save')]"
    save_btn = driver.find_element_by_xpath(xpath)
    save_btn.click()
    print "Click Save button on calendar"
    print "Scheduled meeting is saved"
    time.sleep(5)

# go_to_google_mail_calendar()
# create_repeat_meeging()
# input_meeting_title()
# set_meeting_schedule()
# set_repeating_cycle()
# save_meeting()




    