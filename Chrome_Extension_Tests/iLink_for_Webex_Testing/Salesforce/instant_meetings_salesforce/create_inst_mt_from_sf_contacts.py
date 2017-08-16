'''
Created on Jul 25, 2017

@author: qcadmin
'''
from selenium.webdriver.support.ui import Select
import create_inst_mt_from_webex_icon

import time

contact_url_lighting = 'https://na88.lightning.force.com/one/one.app?source=aloha#/sObject/Contact/list?filterName=Recent'
contact_url_classic = 'https://na88.salesforce.com/003/o'
template_2 = 'Test#Template 1'
topic_2 = 'Salesforce Instant Meeting from Contact classic Interface'
topic_3 = 'Salesforce Instant Meeting from Contact lightning Interface'
passwd_2 = '2222b'
passwd_3 = '3333c'
driver = create_inst_mt_from_webex_icon.driver
from iLink_for_Webex_Testing.Salesforce import login_to_salesforce
login_to_salesforce.login_saleforce_account(driver)

def create_inst_mt_from_contact_classic():
    driver.get(contact_url_classic)
    time.sleep(8)
    """detect and close the popup window of sf calendar"""
    try:
        default_handle = driver.current_window_handle
        handles = list(driver.window_handles)
        assert len(handles) > 1
        handles.remove(default_handle)
        assert len(handles) > 0
        driver.switch_to_window(handles[0])
        print "Close the popup window"
        driver.close()
        driver.switch_to_window(default_handle)
    except:
        print "No popup window"
    xpath = "//a[@title='Reid Zhang']/following-sibling::div[@title='WebEx']"
    driver.find_element_by_xpath(xpath).click()
    time.sleep(2)
    
    def input_meeting_topic():
        driver.switch_to_frame("frameCreateWebex")
        print "Select Apply tmeplate"
        templ = Select(driver.find_element_by_id('comboTemplates'))
        templ.select_by_visible_text(template_2)
        print "The template selected is %s" % template_2
        print "Input meeting topic"
        mt_title = driver.find_element_by_id('id_wexTopic')
        mt_title.clear()
        mt_title.send_keys(topic_2)
        print "Meeting title for %s is input" % topic_2
    input_meeting_topic()
    
    def set_password_create_meeting():
        pwd = driver.find_element_by_id('id_txtPin')
        pwd.clear()
        pwd.send_keys(passwd_2)
        print "Input meeting password"
        driver.find_element_by_id('createWebexSpan').click()
        print "Instant meeting is created"
        time.sleep(5)
        print ''
    set_password_create_meeting()
    driver.close

def create_inst_mt_from_contact_lightning():
    driver.get(contact_url_lighting)
    time.sleep(8)
    """detect and close the popup window of sf calendar"""
    try:
        default_handle = driver.current_window_handle
        handles = list(driver.window_handles)
        assert len(handles) > 1
        handles.remove(default_handle)
        assert len(handles) > 0
        driver.switch_to_window(handles[0])
        print "Close the popup window"
        driver.close()
        driver.switch_to_window(default_handle)
    except:
        print "No popup window"
    xpath = "//a[@title='Reid Zhang']/following-sibling::div[@title='WebEx']"
    driver.find_element_by_xpath(xpath).click()
    time.sleep(2)

    def input_meeting_topic():
        driver.switch_to_frame("frameCreateWebex")
        print "Select Apply tmeplate"
        templ = Select(driver.find_element_by_id('comboTemplates'))
        templ.select_by_visible_text(template_2)
        print "The template selected is %s" % template_2
        print "Input meeting topic"
        mt_title = driver.find_element_by_id('id_wexTopic')
        mt_title.clear()
        mt_title.send_keys(topic_3)
        print "Meeting title is input"
    input_meeting_topic()
    
    def set_password_create_meeting():
        pwd = driver.find_element_by_id('id_txtPin')
        pwd.clear()
        pwd.send_keys(passwd_3)
        print "Input meeting password"
        driver.find_element_by_id('createWebexSpan').click()
        print "Instant meeting is created"
        time.sleep(5)
        try:
            default_handle = driver.current_window_handle
            handles = list(driver.window_handles)
            assert len(handles) > 1
            handles.remove(default_handle)
            assert len(handles) > 0
            driver.switch_to_window(handles[0])
            print "Close the popup window"
            driver.close()
            driver.switch_to_window(default_handle)
        except:
            print "No popup window"
        print ''
    set_password_create_meeting()
    driver.close
    
# create_inst_mt_from_contact_classic()
# create_inst_mt_from_contact_lightning()
    
