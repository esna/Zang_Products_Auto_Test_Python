# -*- coding: utf-8 -*-
'''
Created on Jul 20, 2017

@author: qcadmin
'''
import time
from selenium.webdriver.common.keys import Keys

def messages_call_actions(driver1):
    print "Test the interact activities between two accounts"
    def add_available_contact_to_favorite(driver1):
        driver = driver1
        driver.find_element_by_xpath("//a[@title='People']").click()
        time.sleep(2)
        driver.find_element_by_link_text('GROUPS').click()
        time.sleep(1)
        xpath = "//a[@class='header']//div[contains(.,'Favorites')]"
        driver.find_element_by_xpath(xpath).click()
        time.sleep(2)
        try:
            xpath = "//a[@href='ws://'][@title='percyt@esna.com']"
            conct = driver.find_element_by_xpath(xpath)
            if conct.is_displayed():
                print "Contact is in Favorite group already"
                driver.find_element_by_xpath("//a[@title='People']").click()
                time.sleep(3)
            else:
                print "Add contact to favorite group"
        except:
            driver.find_element_by_xpath("//a[@title='Manage group members']").click()
            time.sleep(2)
            xpath = "//input[@placeholder='Search people']"
            search_box = driver.find_element_by_xpath(xpath)
            print "Search the specified contact"
            search_box.send_keys('Percy')
            time.sleep(3)
            try:
                driver.find_element_by_link_text('Got it')
                print "Acknowledge the remind message"
            except:
                print "Remind message is not displayed"
            xpath = "//a[@title='percyt@esna.com']/div/div"
            conct = driver.find_element_by_xpath(xpath)
            conct.click()
            time.sleep(1)
            print "Add the contact"
            driver.find_element_by_xpath("//a[@class='icon iPlus']").click()
            time.sleep(1)
            print "The contact is added in"
            driver.find_element_by_link_text("Close").click()
            time.sleep(1)
            driver.find_element_by_xpath("//a[@title='People']").click()
            time.sleep(5)
            
    
    def get_the_available_contact():
        driver = driver1
        try:
            xpath = "//ul[@class='list']/li[@class='online chat dial']/a[@href='ws://'][@title='percyt@esna.com']"
            conct = driver.find_element_by_xpath(xpath)
            conct.click()
            time.sleep(2)
        except:
            driver.find_element_by_link_text('GROUPS').click()
            time.sleep(1)
            xpath = "//a[@class='header']//div[contains(.,'Favorites')]"
            driver.find_element_by_xpath(xpath).click()
            time.sleep(2)
            xpath = "//a[@href='ws://'][@title='percyt@esna.com']"
            conct = driver.find_element_by_xpath(xpath)
            conct.click()
            time.sleep(2)
        try:
            driver.find_element_by_link_text("Skip tutorial").click()
            print "Skip the tutorial message"
            time.sleep(1)
        except:
            print "Tutorial is not displayed"
        
    def send_message_to_contact():
        driver = driver1
        msg_icon = driver.find_element_by_link_text('MESSAGES')
        msg_icon.click()
        print "Click the Messages icon"
        xpath = "//div/textarea[@placeholder='Type a message...']"
        type_box = driver.find_element_by_xpath(xpath)
        type_box.clear()
        type_box.send_keys('test message from account1 to accont2')
        send_btn = driver.find_element_by_link_text('SEND')
        send_btn.click()
        print "test message sent to account 2"
        
    def contact_actions():
        driver = driver1
        msg_icon = driver.find_element_by_link_text('ACTIONS')
        msg_icon.click()
        print "Click the Messages icon"
        time.sleep(1)
        equinox = driver.find_element_by_link_text('Equinox Conferencing')
        print "Click the Equinox Conferencing link"
        equinox.click()
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[-1])
        try:
            xpath = "//span[contains(.,'Esna iLink for Avaya Scopia® Desktop not installed')]"
            not_inst = driver.find_element_by_xpath(xpath)
            if not_inst.is_displayed():
                print "Link works, equinox is not installed"
            else:
                print "Equinox link does not work"
        except:
            print "Equinox link is not displayed"
        driver.find_element_by_xpath("//button[contains(.,'Close')]").click()
        print "tab of Equinox is closed"
        driver.switch_to_window(driver.window_handles[0])
        
        msg_icon.click()
        hangout = driver.find_element_by_link_text('Hangout')
        hangout.click()
        time.sleep(1)
        driver.switch_to_window(driver.window_handles[-1])
        hangouts_url = driver.current_url
        if "https://hangouts.google.com" in hangouts_url:
            print "Hangouts is activated"
        else:
            print "Hangouts link does not work"
        time.sleep(2)
        driver.close()
        shared_doc_url = 'https://docs.google.com/document/d/1sNwpUtoLALl2kD1WAhQPZMDFVBa9DmUKOok6-ywBYe4/edit'
        driver.switch_to_window(driver.window_handles[1])
        driver.get(shared_doc_url)
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[0])
        
        msg_icon.click()
        share_loc = driver.find_element_by_link_text('Share location')
        share_loc.click()
        time.sleep(2)
        map = driver.find_element_by_link_text('I\'m at')
        if map.is_displayed():
            print "Shared location is sent out"
        else:
            print "Shared location does not work"
            
        msg_icon.click()
        share_doc = driver.find_element_by_link_text('Share document')
        share_doc.click()
        time.sleep(1)
        xpath = "//li[@jsc_id='1sNwpUtoLALl2kD1WAhQPZMDFVBa9DmUKOok6-ywBYe4']/a[@href='ws://']"
        shared_doc = driver.find_element_by_xpath(xpath)
        shared_doc.click()
        time.sleep(1)
        xpath = "//a[contains(@href,'docs.google.com/a/esna')]"
        shared_doc_link = driver.find_element_by_xpath(xpath)
        if shared_doc_link.is_displayed():
            print "Shared document is sent"
        else:
            print "Shared document link does not work"
     
        msg_icon.click()
        share_doc = driver.find_element_by_link_text('Share web page').click()
        time.sleep(1)
        xpath = "//a[@href='ws://'][contains(@icon,'docs.google.com/document')]"
        shared_web = driver.find_element_by_xpath(xpath)
        shared_web.click()
        print "shared web site clicked"
        time.sleep(2)
        xpath = "//a[contains(@href,'docs.google.com/document')]"
        shared_web_link = driver.find_element_by_xpath(xpath)
        if shared_web_link.is_displayed():
            print "Shared website is sent"
        else:
            print "Shared website link does not work"
        
        msg_icon.click()
        clear_his = driver.find_element_by_link_text('Clear history').click()
        time.sleep(1)
        xpath = "//div[@class='nodata hidden']"
        blank_area = driver.find_element_by_xpath(xpath)
        if blank_area.is_displayed():
            print "log histrory is cleared"
        else:
            print "Clear history does not work"
            
        msg_icon.click()
        share_doc = driver.find_element_by_link_text('Groups').click()
        time.sleep(2)
        xpath = "//div[contains(.,'Favorites')]"
        if driver.find_element_by_xpath(xpath).is_displayed():
            print "Groups page is displayed"
            driver.find_element_by_link_text('Close').click()
            time.sleep(1)
        else:
            print "Groups link does not work"
        
        msg_icon.click()
        share_doc = driver.find_element_by_link_text('Remove').click()
        driver.find_element_by_xpath("//a[@title='People']").click()
        try:
            xpath = "//a[@href='ws://'][@title='percyt@esna.com']"
            conct = driver.find_element_by_xpath(xpath)
            conct.click()
            print "Contact is not removed"
        except:
            print "Contact is removed"
     
    add_available_contact_to_favorite()
    get_the_available_contact()
    send_message_to_contact()
    contact_actions()
    