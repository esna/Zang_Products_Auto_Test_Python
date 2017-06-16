
# -*- coding: utf-8 -*-

from iLink_for_Webex_Testing import add_login_webex_extension
import edit_repeat_meetings
import time, re
from test.test_xml_etree import xpath_tokenizer

url_mywebex = 'https://esna.webex.com/mw3200/mywebex/default.do?siteurl=esna&service=10'
url_gmail = 'https://mail.google.com'
url_calendar = 'https://calendar.google.com/calendar/render?tab=mc#main_7'
new_title = edit_repeat_meetings.new_title

driver = add_login_webex_extension.driver

def delete_edited_repeat_meetings_from_webex_server():
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
    webex_account_login()
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
        xpath = "//a[@title = '%s']" % new_title
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
        time.sleep(2)
        driver.switch_to_active_element
        xpath = "//label[contains(.,'Cancel entire meeting series')]"
        sel_entire = driver.find_element_by_xpath(xpath)
        sel_entire.click()
        print "Select cancel entire meeting series"
        driver.find_element_by_id('mc-rd-del-btn-ok').click()
        print "Click OK button to confirm"
        alert = driver.switch_to_alert()
        try:
            alert.accept()
            print "OK button on confirmation alert is clicked"
        except:
            pass
        try:
            xpath = "//a[@title = '%s']" % new_title
            mt_title = driver.find_element_by_xpath(xpath)
            if mt_title.is_displayed():
                print "Created meeting is not deleted"
        except:
            print "The created instant meeting is verified deleted"
    print ''
    delete_selected_meeting()
    
    
def delete_repeat_meetings_from_google_calendar():
    edit_repeat_meetings.go_to_goolge_calendar()
    print "Delete the repeat meetings from calendar"
    def locate_edited_meeting():
        try:
            xpath = "//div[@class='cpchip']/span[contains(., '%s')]" % new_title
            edt_meeting = driver.find_element_by_xpath(xpath)
            print "Found the edited meeting"
            xpath = "//span[@class='chip-caption'][contains(.,'1p – 2p ')]"
            driver.find_element_by_xpath(xpath).click()
            print "Meeting link is clicked"
            time.sleep(2)
        except:
            print 'The edited meeting is not found'
            
    def delete_edited_meeting():

        def switch_to_pipup_delete_edit_iframe():
            name_str = 'apiproxyfaec9916fba1fb06304bf2a746a1d8ffabcab4ec0'
            frame_ref = driver.find_element_by_xpath("//iframe[contains(@name,'%s')]"% name_str)
            driver.switch_to_frame(frame_ref) 
            print "Swiched to the popup iframe"
        def delete_from_popup_iframe():
            xpath = "//span[contains(@id, 'footerleft')]/div"
            del_btn = driver.find_element_by_xpath(xpath)
            del_btn.click()

        xpath = "//div[@class='goog-imageless-button-content'][contains(.,'Delete')]"
        del_btn = driver.find_element_by_xpath(xpath)
        del_btn.click()
        print "Click Delete button"
        time.sleep(1)
        driver.switch_to_active_element
        xpath = "//div[@class='goog-imageless-button-content'][contains(.,'All events in the series')]"
        del_btn = driver.find_element_by_xpath(xpath)
        del_btn.click()
        print "Confirm delete all events in the meeting series"
        time.sleep(2)
        try:
            xpath = "//div[@class='cpchip']/span[contains(., '%s')]" % new_title
            edt_meeting = driver.find_element_by_xpath(xpath)
            if edt_meeting.is_displayed():
                print "The created meeting is still there"
        except:
            print "The repeat meetings are deleted from google calendar"
    locate_edited_meeting()
    delete_edited_meeting()
    
delete_edited_repeat_meetings_from_webex_server()
delete_repeat_meetings_from_google_calendar()