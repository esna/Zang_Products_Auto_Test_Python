# -*- coding: utf-8 -*-
'''
Created on Jul 20, 2017

@author: qcadmin
'''
import time
from selenium.webdriver.common.keys import Keys

def messages_call_actions(driver):
    print "Test the interact activities between two accounts"
    def add_available_contact_to_favorite():
        
        driver.find_element_by_xpath("//a[@title='People']").click()
        time.sleep(1)
        driver.find_element_by_link_text('GROUPS').click()
        xpath = "//a[@class='header']//div[contains(.,'Favorites')]"
        driver.find_element_by_xpath(xpath).click()
        time.sleep(5)
        
        xpath = "//a[@title='percyt@esna.com']//div[contains(.,'Percy')]"
        conct = driver.find_element_by_xpath(xpath)
        if conct.is_displayed():
            print "Contact is in Favorite group already"
            driver.find_element_by_xpath("//a[@title='People']").click()
            time.sleep(3)
        else:
            print "Add contact to favorite group"
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
            time.sleep(2)
    
    def get_the_available_contact():
        xpath = "//ul[@class='list people square']/li[1]/ul/li/a[1]/div/div[contains(.,'Percy Teng')]"
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
        msg_icon = driver.find_element_by_link_text('ACTIONS')
        msg_icon.click()
        print "Click the Messages icon"
        time.sleep(1)
        equinox = driver.find_element_by_link_text('Equinox Conferencing')
        print "Click the Equinox Conferencing link"
        equinox.click()
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
        driver.switch_to_window(driver.window_handles[0])
        msg_icon.click()
        driver.switch_to_window(driver.window_handles[-1])
        driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "\w")
        driver.switch_to_window(driver.window_handles[0])
        hangout = driver.find_element_by_link_text('Hangout')
        hangout.click()
        time.sleep(1)
        xpath = "//div[@class='chat'][contains(.,'I've invited you to join a Hangout via the following link: ')]"
        link1 = driver.find_element_by_xpath(xpath)
        print link1.text
        link2 = driver.find_element_by_xpath("%s/a[contains(@href,'https://hougouts.google.com')]" % xpath) 
        if link2.is_displayed():
            print "Hougout link works"
        else:
            print "Hougout link does not work"
        
        
        
        
     
    add_available_contact_to_favorite()
    get_the_available_contact()
    send_message_to_contact()
    contact_actions()
    