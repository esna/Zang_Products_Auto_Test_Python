# -*- coding: utf-8 -*-
from iLink_for_Webex_Testing import add_login_webex_extension
import datetime, time, re
from selenium.webdriver.support.ui import Select

tmr = datetime.date.today() + datetime.timedelta(days=1)
tmr_plus_one = datetime.date.today() + datetime.timedelta(days=2)
d1 = datetime.datetime.strptime("%s" % tmr, '%Y-%m-%d')
d2 = datetime.datetime.strptime("%s" % tmr_plus_one, '%Y-%m-%d')
tomorrow = datetime.date.strftime(d1, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
tom_plus_one = datetime.date.strftime(d2, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
fromtime = "12:00 PM"
untiltime = "1:00 PM"
time_taken = '1 hour'
title = "Scheduled meeting from google calendar"
template = 'reid test template'
al_host_email = 'reidz@esna.com'
al_hostname = 'Reid Zhang'
mt_type = 'Pro 1000'
ph_num = '(905)707-9700'
delegate_cl = 'Matheesan Manokaran'
url_mywebex = 'https://esna.webex.com/mw3200/mywebex/default.do?siteurl=esna&service=10'
url_gmail = 'https://mail.google.com'
url_calendar = 'https://calendar.google.com/calendar/render?tab=mc#main_7'

driver = add_login_webex_extension.driver
add_login_webex_extension.login_ext_with_google()
time.sleep(20)
add_login_webex_extension.input_esna_webex_password()

def go_to_google_mail_calendar():
    print "Go to gmail account"
    driver.get(url_gmail)
    time.sleep(5)
    print "Go to google calendar"
    driver.get(url_calendar)
    time.sleep(5)

def create_scheduled_meeging_with_delegate_calendar():
    xpath = "//div[@id='createEventButtonContainer']//div[@class='goog-imageless-button-content']"
    create_btn = driver.find_element_by_xpath(xpath)
    create_btn.click()
    print "Click create button"
    time.sleep(3)
    calendar = Select(driver.find_element_by_id(':1d.calendar'))
    calendar.select_by_visible_text(delegate_cl)
    print "Select %s's calendar as delegate calendar" % delegate_cl
    
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
    print ''
    
def create_meeting_with_webex_icon():
    print "Create meeting with webex tool"
    driver.find_element_by_id('webex0addtext').click()
    print "Click webex meeting icon"
    time.sleep(2)
    driver.switch_to_frame('frameCreateWebex')
    def select_meeting_template():
        templ = Select(driver.find_element_by_id('comboTemplates'))
        templ.select_by_visible_text(template)
        print "The template selected is %s" % template
    def input_alter_host():
        alter_host = driver.find_element_by_id('id_altHosts')
        alter_host.clear()
        alter_host.send_keys(al_host_email)
        print "Alter host selected is %s" % al_host_email
    def select_meeting_type():
        m_type = Select(driver.find_element_by_id('meetingtype_combo'))
        m_type.select_by_visible_text(mt_type)
        print "Meeting type selected is %s" % mt_type
    def select_join_before_start():
        join_bf = Select(driver.find_element_by_id('id_joinBeforeTimeCount'))
        join_bf.select_by_value('5')
        print "First attendee can join meeting 5 minutes before starting"
    def check_first_attendee():
        driver.find_element_by_id('id_joinBeforeTimeFirstPresenter').click()
        print "First attendee is set as presenter"
    def select_audio_type():
        join_bf = Select(driver.find_element_by_id('id_wexAudio'))
        join_bf.select_by_value('OTHER')
        other_phone = driver.find_element_by_id('id_wexOtherTeleconfOptions')
        other_phone.clear()
        other_phone.send_keys(ph_num)
        print "Audio type selected is other service, phone number input %s" % ph_num
    def input_generated_password():
        driver.find_element_by_id('wexGeneratePin').click()
        time.sleep(2)
        print "Meeting password is generated randomly"
    select_meeting_template()
    input_alter_host()
    select_meeting_type()
    select_join_before_start()
    check_first_attendee()
    select_audio_type()
    input_generated_password()
        
def save_meeting():
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
    print ''

def verify_created_google_inst_meeting():
    driver.get(url_mywebex)
    time.sleep(2)
    def webex_account_login():
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
    webex_account_login()
    
    def verify_meeting_data():
        print "Verify the created meeting's details"
        def verify_meeting_title():
            driver.switch_to_frame('menu')
            xpath = "//span[contains(.,'My Meetings')]"
            driver.find_element_by_xpath(xpath).click()
            driver.switch_to_default_content()
            driver.switch_to_frame('mainFrame')
            driver.switch_to_frame('main')
            driver.find_element_by_id('wcc-lnk-search').click()
            time.sleep(1)
            xpath = "//a[@title='%s']/i" % title
            mt_title = driver.find_element_by_xpath(xpath)
            print "Meeting title is verified correct"
        
        def verify_meeting_time():
            xpath = "//td[contains(.,'%s')]" % fromtime.lower()
            mt_st_time = driver.find_element_by_xpath(xpath)
            input_time = tmr.strftime("%b %d, %Y ").lstrip("0").replace(" 0", " ") + fromtime.lower()
            get_mt_time = mt_st_time.text
            
            print input_time
            print get_mt_time
            
            assert input_time == get_mt_time
            
            print "Meeting start time is verified correct"
            xpath = "//a[@title='%s']/i" % title
            mt_title = driver.find_element_by_xpath(xpath)
            mt_title.click()
            mt_period = driver.find_element_by_id('mc-txt-duration')
            get_time_period = mt_period.text
            assert time_taken == get_time_period
            print "Meeting duration is verified correct"
            time.sleep(2)

        def verify_meeting_hosts_audio_connection():
            driver.find_element_by_id('mc-lnk-moreInfo').click()
            host = driver.find_element_by_id('mc-txt-hostname')
            host_nmae = host.text
            al_host = driver.find_element_by_id('mc-txt-alternateHost')
            al_host_name = al_host.text
            assert 'Host: ' + delegate_cl == host_nmae
            print "Meeting host is verified correct"
            assert al_hostname == al_host_name
            print "Meeting alternate host is verified correct"
            xpath = "//div[@id='mc-txt-teleconference']/div/p"
            audio = driver.find_element_by_xpath(xpath)
            assert  ph_num == audio.text
            print "Audio connection phone number is verified correct"
            
        verify_meeting_title()
        verify_meeting_time()
        verify_meeting_hosts_audio_connection()
        
    verify_meeting_data()
    print ''
    
def delete_created_schdeuled_meeting():
    def go_to_meeting_list():
        driver.switch_to_default_content()
        driver.switch_to_frame('mainFrame')
        driver.switch_to_frame('menu')
        xpath = "//span[contains(.,'My Meetings')]"
        driver.find_element_by_xpath(xpath).click()
        print "My Meetings link is clicked"
        driver.switch_to_default_content()
        driver.switch_to_frame('mainFrame')
        driver.switch_to_frame('main')
        driver.find_element_by_id('wcc-lnk-search').click()
        print "Click All Meeting tab"
        driver.switch_to_default_content()
        driver.switch_to_frame('mainFrame')
        driver.switch_to_frame('main')
    go_to_meeting_list()
    def select_created_inst_meeting():
        xpath = "//a[@title = '%s']" % title
        mt_title = driver.find_element_by_xpath(xpath)
        num = mt_title.get_attribute('number')
        num = re.findall('\d+', num)
        event_num = num[0]
        chkbox_id = 'checkbox-link-mwx-checkbox-event-' + event_num
        chkbox = driver.find_element_by_id(chkbox_id)
        chkbox.click()
        print "Cancel Meeting checkbox is checked"
    select_created_inst_meeting()
    def delete_selected_meeting():
        driver.find_element_by_id('mwx-link-delete').click()
        print "Cancel button is clicked"
        alert = driver.switch_to_alert()
        alert.accept()
        print "OK button on confirmation alert is clicked"
        try:
            xpath = "//a[@title = '%s']" % title
            mt_title = driver.find_element_by_xpath(xpath)
            if mt_title.is_displayed():
                print "Created meeting is not deleted succeefully"
        except:
            print "The created instant meeting is verified deleted"
    print ''
    delete_selected_meeting()
    
    
def delete_meeting_on_calendar():
    driver.get(url_calendar)
    time.sleep(2)
    def locate_edited_meeting():
        try:
            xpath = "//div[@class='cpchip']/span[contains(., '%s')]" % title
            edt_meeting = driver.find_element_by_xpath(xpath)
            print "Found the edited meeting"
            xpath = "//span[@class='chip-caption'][contains(.,'12p – 1p ')]"
            driver.find_element_by_xpath(xpath).click()
            print "Meeting link is clicked"
            time.sleep(2)
        except:
            print 'The edited meeting is not found'
    def delete_edited_meeting():
        driver.switch_to_active_element()
        xpath = "//div[@class='neb-footer']/span[2]/div[1]"
        del_btn = driver.find_element_by_xpath(xpath)
        del_btn.click()
        try:
            xpath = "//div[@class='cpchip']/span[contains(., '%s')]" % title
            edt_meeting = driver.find_element_by_xpath(xpath)
            if edt_meeting.is_displayed():
                print "The created meeting is still there"
        except:
            print "The simple meeting is deleted from google calendar"
    locate_edited_meeting()
    delete_edited_meeting()
    
go_to_google_mail_calendar()
create_scheduled_meeging_with_delegate_calendar()
input_meeting_title()
set_meeting_schedule()
create_meeting_with_webex_icon()
save_meeting()
verify_created_google_inst_meeting()
delete_created_schdeuled_meeting()
delete_meeting_on_calendar()
print "test ends"
driver.quit()


    
    