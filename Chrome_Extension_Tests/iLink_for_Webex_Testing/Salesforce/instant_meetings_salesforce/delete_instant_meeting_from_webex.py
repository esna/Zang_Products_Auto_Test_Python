# -*- coding: utf-8 -*-
'''
Created on Jul 24, 2017

@author: qcadmin
'''
from selenium import webdriver
from iLink_for_Webex_Testing import login_webex_account
import verify_instant_meeting_data
import re, time
# driver = webdriver.Chrome()
driver = verify_instant_meeting_data.verify_meeting_data()
time.sleep(2)
try:
    login_webex_account.webex_account_login(driver)
except:
    print "Webex account has already logged in"
url_mywebex = 'https://esna.webex.com/mw3200/mywebex/default.do?siteurl=esna&service=10'
topic_1 = 'Salesforce Instant Meeting from webex icon with reid template'
topic_2 = 'Salesforce Instant Meeting from Contact classic Interface'
topic_3 = 'Salesforce Instant Meeting from Contact lightning Interface'
time.sleep(2)
def delete_created_instant_meeting():
    def go_to_meeting_list():
        driver.switch_to_default_content()
        driver.switch_to_frame('mainFrame')
        driver.switch_to_frame('menu')
        xpath = "//span[contains(.,'My Meetings')]"
        driver.find_element_by_xpath(xpath).click()
        time.sleep(2)
        print "My Meetings link is clicked"
        driver.switch_to_default_content()
        driver.switch_to_frame('mainFrame')
        driver.switch_to_frame('main')
    go_to_meeting_list()
    
    def select_created_inst_meeting_delete():
        for topic in (topic_1, topic_2, topic_3):
            try:
                xpath = "//td[@class='meeting-name bs-tablelist-iconinline ']/a[@title = '%s']" % topic
                mt_title = driver.find_element_by_xpath(xpath)
                id = mt_title.get_attribute('id')
                id_num = re.findall('\d+', id)
                mt_id_num = id_num[0]
                chkbox_id = 'checkbox-mwx-chk-'+mt_id_num
                chkbox = driver.find_element_by_id(chkbox_id)
                chkbox.click()
                time.sleep(1)
                print "Cancel Meeting checkbox is checked"
                driver.find_element_by_id('mwx-btn-delete').click()
                print "Cancel button is clicked"
                time.sleep(2)
                try:
                    alert = driver.switch_to_alert()
                    alert.accept()
                    print "OK button on confirmation alert is clicked"
                except:
                    print "No confirmation alert is displayed"
                time.sleep(2)
                try:
                    driver.switch_to_window(driver.window_handles[-1])
                    driver.find_element_by_name('NoBtn').click()
                    print "Selected don't send option"
                except:
                    print "No send email options displayed"
                driver.switch_to_window(driver.window_handles[0])
                time.sleep(3)
            except:
                print "%s cannot be located with its xpath" % topic
                
    select_created_inst_meeting_delete()
    
# delete_created_instant_meeting()