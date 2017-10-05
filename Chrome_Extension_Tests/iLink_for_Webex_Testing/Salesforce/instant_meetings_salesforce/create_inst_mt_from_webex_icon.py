'''
Created on May 19, 2017

@author: qcadmin
'''
from selenium.webdriver.support.ui import Select
from iLink_for_Webex_Testing import add_login_webex_extension
import time, re
prefix = 'chrome-extension://'
testing_page = 'popup'
subfix = '/%s.html' % testing_page
unique_id = ''
template_1 = 'reid test template'
mt_type = 'Default'
audio = "WebEx Audio"
topic_1 = 'Salesforce Instant Meeting from webex icon with reid template'
time_hrs = '1'
time_mins = '15'
passwd_1 = '1111a'
url = 'https://login.salesforce.com/?locale=ca'

driver = add_login_webex_extension.driver
add_login_webex_extension.login_ext_with_Salesforce()
add_login_webex_extension.input_esna_webex_password()

def create_inst_meeting_from_webex_icon():
    def get_inst_meeting_window():
        current_url = driver.current_url
        find_unique_id = re.search('//'+'(.+?)'+'/', current_url)
        if find_unique_id:
            unique_id = find_unique_id.group(1)
        driver.get(prefix + unique_id + subfix)
        time.sleep(2)
        
    def create_instant_meeting():
        def input_meeting_topic():
            print "Select Applied tmeplate"
            templ = Select(driver.find_element_by_id('comboTemplates'))
            templ.select_by_visible_text(template_1)
            print "The template selected is %s" % template_1
            print "Input meeting topic"
            mt_title = driver.find_element_by_id('id_wexTopic')
            mt_title.clear()
            mt_title.send_keys(topic_1)
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
            
        print driver.current_url
        select_meeting_type_set_duration()
        
        def select_audio_set_pwd_create_meeting():
            print "Select Audio tyep"
            audio_type = Select(driver.find_element_by_id('id_wexAudio'))
            audio_type.select_by_visible_text(audio)
            toll_free = driver.find_element_by_id('id_wexTollFree')
            if toll_free.is_selected() == False:
                toll_free.click()
            call_in = driver.find_element_by_id('id_wexCallIn')
            if call_in.is_displayed() == False:
                call_in.click()
            pwd = driver.find_element_by_id('id_txtPin')
            pwd.clear()
            pwd.send_keys(passwd_1)
            print "Input meeting password"
            driver.find_element_by_id('createWebexSpan').click()
            print "Instant meeting is created"
            time.sleep(5)
            print ''
        select_audio_set_pwd_create_meeting()
        
    get_inst_meeting_window()
    create_instant_meeting()
    driver.switch_to_window(driver.window_handles[0])
    return driver

# create_inst_meeting_from_webex_icon()





