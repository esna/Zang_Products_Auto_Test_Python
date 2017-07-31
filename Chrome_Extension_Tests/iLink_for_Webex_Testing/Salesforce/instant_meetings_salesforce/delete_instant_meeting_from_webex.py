'''
Created on Jul 24, 2017

@author: qcadmin
'''
from iLink_for_Webex_Testing.Salesforce import add_extention_sso_sf
import create_instant_meetings
import edit_instant_meetings
import verify_instant_meeting_data
import re, time

url_mywebex = 'https://esna.webex.com/mw3200/mywebex/default.do?siteurl=esna&service=10'
topic = create_instant_meetings.topic
driver = add_extention_sso_sf.extenstion_and_sso()
driver.get(url_mywebex)
time.sleep(2)
driver.switch_to_frame('mainFrame')

def delete_created_instant_meeting():
    try:
        verify_instant_meeting_data.webex_account_login()
    except:
        print "Webex account has been logged in"
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
    
delete_created_instant_meeting()