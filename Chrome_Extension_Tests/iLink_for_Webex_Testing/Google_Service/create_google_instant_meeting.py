'''
Created on May 19, 2017

@author: qcadmin
'''
from selenium import webdriver
from iLink_for_Webex_Testing import add_login_webex_extension
from selenium.webdriver.support.ui import Select
import time, re


prefix = 'chrome-extension://'
testing_page = 'popup'
subfix = '/%s.html' % testing_page
unique_id = ''
template = 'reid test template'
topic = 'Google Instant Meeting with Group Template'
mt_type = 'Default'
time_hrs = '1'
time_mins = '15'
audio = "WebEx Audio"
passwd = '1111a'
url_mywebex = 'https://esna.webex.com/mw3200/mywebex/default.do?siteurl=esna&service=10'
toll_free_num = '1-855-244-8681 Call-in toll-free number (US/Canada)'
toll_number = '1-650-479-3207 Call-in toll number (US/Canada)'

driver = add_login_webex_extension.driver
add_login_webex_extension.login_ext_with_google()
time.sleep(30)
add_login_webex_extension.input_esna_webex_password()
time.sleep(5)

def get_inst_meeting_window():
    current_url = driver.current_url
    find_unique_id = re.search('//'+'(.+?)'+'/', current_url)
    if find_unique_id:
        unique_id = find_unique_id.group(1)
    driver.get(prefix + unique_id + subfix)
    
def create_inst_meeting():
    def input_meeting_topic():
        print "Select Apply tmeplate"
        templ = Select(driver.find_element_by_id('comboTemplates'))
        templ.select_by_visible_text(template)
        print "The template selected is %s" % template
        print "Input meeting topic"
        mt_title = driver.find_element_by_id('id_wexTopic')
        mt_title.clear()
        mt_title.send_keys(topic)
        print "Meeting title is input"
    input_meeting_topic()
    def select_meeting_type_set_duration():
        print "Select meeting type"
        mt_type = Select(driver.find_element_by_id('meetingtype_combo'))
        mt_type.select_by_value('false')
        print "Set duration"
        mt_time_h = Select(driver.find_element_by_id('id_wexDuration_h'))
        mt_time_h.select_by_value(time_hrs)
        mt_time_m = Select(driver.find_element_by_id('id_wexDuration_m'))
        mt_time_m.select_by_value(time_mins)
    select_meeting_type_set_duration()
    def select_audio_set_password():
        print "Select Audio tyep"
        audio_type = Select(driver.find_element_by_id('id_wexAudio'))
        audio_type.select_by_visible_text(audio)
        toll_free = driver.find_element_by_id('id_wexTollFree')
        if toll_free.get_attribute('checked'):
            print "toll free box is checked"
        else:
            toll_free.click()
            print "toll free box is not checked, check it"
        call_in = driver.find_element_by_id('id_wexCallIn')
        if call_in.get_attribute('checked'):
            print "Call_in box is checked"
        else:
            toll_free.click()
            print "Call_in box is not checked, check it"
        pwd = driver.find_element_by_id('id_txtPin')
        pwd.clear()
        pwd.send_keys(passwd)
        print "Input meeting password"
        driver.find_element_by_id('createWebexSpan').click()
        print "Instant meeting is created"
        time.sleep(5)
        print ''
    select_audio_set_password()
    
def verify_created_google_inst_meeting():
    driver.switch_to_window(driver.window_handles[0])
    driver.get(url_mywebex)
    driver.switch_to_frame('mainFrame')
    
    def webex_account_login():
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
        
    def verify_meeting_data():
        print "Verify the created meeting's details"
        def verify_meeting_title():
            driver.switch_to_frame('menu')
            xpath = "//span[contains(.,'My Meetings')]"
            driver.find_element_by_xpath(xpath).click()
            driver.switch_to_default_content()
            driver.switch_to_frame('mainFrame')
            driver.switch_to_frame('main')
            xpath = "//a[@title='%s']" % topic
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
            assert passwd == pwd.text
            print "Meeting password is verified correct"
            print ''
            time.sleep(2)
        verify_password()
    try:
        webex_account_login()
        verify_meeting_data()
    except:
        verify_meeting_data()
    
    
def delete_created_instant_meeting():
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
    go_to_meeting_list()
    def select_created_inst_meeting():
        xpath = "//a[@title = '%s']" % topic
        mt_title = driver.find_element_by_xpath(xpath)
        id = mt_title.get_attribute('id')
        id_num = re.findall('\d+', id)
        mt_id_num = id_num[0]
        chkbox_id = 'checkbox-mwx-chk-'+mt_id_num
        chkbox = driver.find_element_by_id(chkbox_id)
        chkbox.click()
        print "Cancel Meeting checkbox is checked"
    select_created_inst_meeting()
    def delete_selected_meeting():
        driver.find_element_by_id('mwx-btn-delete').click()
        print "Cancel button is clicked"
        alert = driver.switch_to_alert()
        alert.accept()
        print "OK button on confirmation alert is clicked"
        try:
            xpath = "//a[@title = '%s']" % topic
            mt_title = driver.find_element_by_xpath(xpath)
            if mt_title.is_displayed():
                print "Created meeting is not deleted succeefully"
        except:
            print "The created instant meeting is verified deleted"
    delete_selected_meeting()
        
get_inst_meeting_window()
create_inst_meeting()
verify_created_google_inst_meeting()
delete_created_instant_meeting()
print 'test ends'