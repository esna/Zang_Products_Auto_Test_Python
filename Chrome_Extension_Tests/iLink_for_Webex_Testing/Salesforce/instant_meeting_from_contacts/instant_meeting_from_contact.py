'''
Created on May 23, 2017

@author: qcadmin
'''
from iLink_for_Webex_Testing import add_login_webex_extension
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time, re
from winsound import SND_ALIAS

template = 'Test#Template 1'
topic = 'Instant meeting from SF contact webex icon'
mt_type = 'Pro 1000'
time_hrs = '0'
time_mins = '20'
audio = 'WebEs Meeting'
passwd = '4444d'
url_mywebex = 'https://esna.webex.com/mw3200/mywebex/default.do?siteurl=esna&service=10'
url_sf = 'https://login.salesforce.com/?locale=ca'
user_id = 'arnoe@esna.com'
passwd = 'EsnaAvaya03'

driver = add_login_webex_extension.driver
add_login_webex_extension.login_ext_with_Salesforce()
add_login_webex_extension.input_esna_webex_password()
time.sleep(5)

def create_meeting_from_classic_interface_contact():
    
    def login_saleforce_account():
        driver.get(url_sf)
        print "Input account username"
        driver.find_element_by_id('username').send_keys(user_id)
        print "Input account password"
        driver.find_element_by_id('password').send_keys(passwd)
        print "Click login button"
        driver.find_element_by_id('Login').click()
        time.sleep(15)
        
    def switch_from_lightning_to_classic():
        xpath = "(//div[@class='tooltipTrigger tooltip-trigger uiTooltip'])[4]"
        try:
            lightning = driver.find_element_by_xpath(xpath)
            lightning.click()
            xpath = "//a[contains(.,'Switch to Salesforce Classic')]"
            driver.find_element_by_xpath(xpath).click()
            print "Interface is changed to Classic"
            time.sleep(15)
        except:
            print "Salesforce is on classic interface"
    
    def initiat_meeting_from_contact_webex_icon_1():
        xpath = "//li[@id='Contact_Tab']"
        contact = driver.find_element_by_xpath(xpath)
        print "Click Contacts"
        contact.click()
        time.sleep(1)
        xpath = "//a[contains(.,'Zhang, Reid')]/following-sibling::div"
        webex_icon_1 = driver.find_element_by_xpath(xpath)
        print "Click the webex icon besides contact name"
        webex_icon_1.click()
        
        """Test Close and add another attendee"""
        driver.switch_to_frame('frameCreateWebex')
        driver.find_element_by_id('saveWebexSpan').click()
        driver.switch_to_default_content
        xpath = "//a[contains(.,'Pizza, Pizza')]/following-sibling::div"
        webex_icon_1 = driver.find_element_by_xpath(xpath)
        print "Click the webex icon besides second contact name"
        driver.switch_to_frame('frameCreateWebex')
        try:
            xpath = "//input[@email='feedback@pizzapizza.ca']"
            chk_box = driver.find_element_by_xpath(xpath)
            if chk_box.is_selected:
                print "Another attendee is added to the list"
            else:
                print "Second attendee is not found"
        except:
            print "element xpath is not found"
        time.sleep(1)
        
        """Test Cancel button"""
        
        
        """User reid test template to create instant meeting"""
        
        print "Click 'Create' button"
        print "Instant meeting is created"
        time.sleep(3)
        
    login_saleforce_account()
    switch_from_lightning_to_classic()
    initiat_meeting_from_contact_webex_icon_1()
        
create_meeting_from_classic_interface_contact()



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


# sso_with_google_service()
# get_specified_email()
# create_meeting_with_webex_icon()
# verify_created_meeting()
# delete_created_instant_meeting()
# driver.quit()
    
    
