
# -*- coding: utf-8 -*-

from iLink_for_Webex_Testing import add_login_webex_extension
import edit_repeat_meetings
import time, re

url_mywebex = 'https://esna.webex.com/mw3200/mywebex/default.do?siteurl=esna&service=10'
url_o365 = "https://login.microsoftonline.com/"
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
    try:
        webex_account_login()
    except:
        print "Webex account has login already"
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
        time.sleep(2)
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
                print "Created meeting series is not deleted"
        except:
            print "The created repeat meetings is verified deleted"
    print ''
    delete_selected_meeting()
    
    
def delete_repeat_meetings_from_o365_calendar():
    def go_to_O365_calendar():
#         print "Go to O365 account"
#         driver.get(url_o365)
#         time.sleep(3)
#         driver.find_element_by_id('O365_MainLink_NavMenu').click()
#         print "Click menu"
#         time.sleep(8)
#         print "Click calendar icon"
#         xpath = "//a[@title='Calendar']"
#         driver.find_element_by_xpath(xpath).click()
#         time.sleep(15)
#         print "Delete the repeat meetings from calendar"
        cal_url = 'https://outlook.office365.com/owa/?realm=esnatech.onmicrosoft.com&exsvurl=1&ll-cc=1033&modurl=1&path=/calendar'
        print "Go to o365 calendar"
        driver.get(cal_url)
        time.sleep(20)
        
    def delete_edited_meeting():
        try:
            xpath = "//span[contains(., '%s')]" % new_title
            edt_meeting = driver.find_element_by_xpath(xpath)
            print "Found the edited meeting"
        except:
            xpath = "//button[@aria-label='NextWeek go to ']/span"
            driver.find_element_by_xpath(xpath).click()
            time.sleep(2)
            xpath = "//span[contains(., '%s')]" % new_title
            edt_meeting = driver.find_element_by_xpath(xpath)
            print "Found the edited meeting"
        edt_meeting.click()
        print "Click the meeting label"
        time.sleep(2)
        driver.switch_to_active_element
        xpath = "//span[contains(.,'Delete')]"
        del_btn = driver.find_element_by_xpath(xpath)
        del_btn.click()
        print "Click Delete button"
        time.sleep(2)
        xpath = "//span[contains(.,'Delete series')]"
        confirm = driver.find_element_by_xpath(xpath)
        confirm.click()
        try:
            xpath = "//span[contains(., '%s')]" % new_title
            edt_meeting = driver.find_element_by_xpath(xpath)
            if edt_meeting.is_displayed():
                print "The created meeting is still there"
        except:
            print "The repeat meetings are deleted from o365 calendar"
    go_to_O365_calendar()
    delete_edited_meeting()
    
# delete_edited_repeat_meetings_from_webex_server()
# delete_repeat_meetings_from_o365_calendar()