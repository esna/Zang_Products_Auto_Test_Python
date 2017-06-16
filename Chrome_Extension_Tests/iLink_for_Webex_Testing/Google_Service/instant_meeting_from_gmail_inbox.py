'''
Created on May 23, 2017

@author: qcadmin
'''
from iLink_for_Webex_Testing import add_login_webex_extension
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time, re

template = 'Test#Template 1'
topic = 'WebEx Meeting #111'
mt_type = 'Pro 1000'
time_hrs = '0'
time_mins = '20'
audio = 'VoIP'
email1 = 'esnaqc.testing@gmail.com'
email2 = 'itsupport@esna.com'
url_mywebex = 'https://esna.webex.com/mw3200/mywebex/default.do?siteurl=esna&service=10'
driver = add_login_webex_extension.driver

def sso_with_google_service():
    add_login_webex_extension.login_ext_with_google()
    add_login_webex_extension.input_esna_webex_password()
    time.sleep(6)

def get_specified_email():
    driver.get('https://mail.google.com')
    search = driver.find_element_by_id('gbqfq')
    search.clear()
    search.send_keys(email1)
    xpath = "//button[@aria-label='Search Esna.com Mail']/span"
    driver.find_element_by_xpath(xpath).click()
    time.sleep(2)
    
def create_meeting_with_webex_icon():
    def get_webex_meeting_window():
        xpath = "//div[@id=':ne']/span[@name='EsnaQC Testing']"
        driver.find_element_by_xpath(xpath).click()
        xpath = "//button[@class='wex_hotspot']"
        driver.find_element_by_xpath(xpath).click()
        time.sleep(2)
    get_webex_meeting_window()
    
    def close_and_add_another_attendee():
        driver.switch_to_frame('frameCreateWebex')
        time.sleep(2)
        driver.find_element_by_id('saveWebexSpan').click()
        driver.get('https://mail.google.com')
        search = driver.find_element_by_id('gbqfq')
        search.clear()
        search.send_keys(email2)
        xpath = "//button[@aria-label='Search Esna.com Mail']/span"
        driver.find_element_by_xpath(xpath).click()
        time.sleep(3)
        xpath = "//div[@id=':m6']/span[@email='%s']" % email2
        sender = driver.find_element_by_xpath(xpath)
        sender.click()
        xpath = "//button[@class='wex_hotspot']"
        driver.find_element_by_xpath(xpath).click()
        driver.switch_to_frame('frameCreateWebex')
        try:
            xpath = "//div[@id='fixedAttendeeName']//span/label[@title='%s']" % email2
            att_2 = driver.find_element_by_xpath(xpath)
            if att_2.is_displayed():
                print "Second attendees is added successfully"
        except:
            print "Second attendee is not displayed"
    close_and_add_another_attendee()
    
    def cancel_webex_window():
        print "Test if Cancel button works"
        driver.find_element_by_id('cancelWebexSpan').click()
        try:
            driver.switch_to_frame('frameCreateWebex')
            driver.find_element_by_id('createWebexSpan').click()
            print "Webex window is not canceled"
        except:
            print "Webex window is canceled successfully"
    cancel_webex_window()
    
    """Create instant meeting with default group based template"""
    get_specified_email()
    get_webex_meeting_window()
    driver.switch_to_frame('frameCreateWebex')
    time.sleep(2)
    print "Use the default values with groupe based template"
    driver.find_element_by_id('createWebexSpan').click()
    print "Click 'Create' button"
    print "Instant meeting is created"
    time.sleep(3)
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(1)
#     driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "\w")

def verify_created_meeting():
    driver.get(url_mywebex)
    def login_webex_website():
        print "Login webex account"
        driver.get(url_mywebex)
        driver.switch_to_frame('mainFrame')
        user_id = driver.find_element_by_id('mwx-ipt-username')
        user_id.click()
        user_id.send_keys('reidz')
        print "Input user id"
        passwd = driver.find_element_by_id('mwx-ipt-password')
        passwd.click()
        passwd.send_keys('Zang123!')
        print "Input password"
        driver.find_element_by_id('mwx-btn-logon').click()
        print "Webex account is logged in"
        time.sleep(5)
               
    def verify_meeting_title():
        print "Verify the created meeting's details"
        driver.switch_to_default_content()
        driver.switch_to_frame('mainFrame')
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
        
    def verify_meeting_time():
        mt_period = driver.find_element_by_id('mc-txt-duration')
        assert time_mins+' minutes' == mt_period.text
        print "Meeting duration is verified"
        time.sleep(2)

    def verify_audio_connection():
        driver.find_element_by_id('mc-lnk-moreInfo').click()
        time.sleep(1)
        audio = driver.find_element_by_id('mc-txt-teleconference')
        assert 'Use VoIP only' == audio.text
        print "Audio connection is verified correct"
    try:
        login_webex_website()
        verify_meeting_title()
        verify_meeting_time()
        verify_audio_connection()
    except:
        verify_meeting_title()
        verify_meeting_time()
        verify_audio_connection()
           
           
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
        driver.switch_to_window(driver.window_handles[2])
        driver.find_element_by_name('NoBtn').click()
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[1])
        try:
            xpath = "//a[@title = '%s']" % topic
            mt_title = driver.find_element_by_xpath(xpath)
            if mt_title.is_displayed():
                print "Created meeting is not deleted succeefully"
            else:
                print "Created meeting is not displayed in the meeting list"
        except:
            print "The created meeting is verified deleted"
    delete_selected_meeting()


sso_with_google_service()
get_specified_email()
create_meeting_with_webex_icon()
verify_created_meeting()
delete_created_instant_meeting()
driver.quit()
    
    
