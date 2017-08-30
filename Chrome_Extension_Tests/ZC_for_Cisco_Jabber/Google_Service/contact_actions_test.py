# -*- coding: utf-8 -*-
'''
Created on Aug 29, 2017

@author: qcadmin
'''
import time

def contact_actions(driver1):
    driver = driver1
    msg_icon = driver.find_element_by_link_text('ACTIONS')
    
    def equinox_link():
        msg_icon.click()
        print "Click the Messages icon"
        time.sleep(1)
        webex = driver.find_element_by_link_text('WebEx')
        print "Click the WebEx link"
        webex.click()
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[-1])
        try:
            xpath = "//span[contains(.,'Esna iLink for WebEx is missed')]"
            not_inst = driver.find_element_by_xpath(xpath)
            if not_inst.is_displayed():
                print "Link works, WebEx is not installed"
            else:
                print "WebEx link does not work"
        except:
            print "WebEx link is not displayed"
        driver.find_element_by_xpath("//button[contains(.,'Close')]").click()
        print "tab of Equinox is closed"
        driver.switch_to_window(driver.window_handles[0])

    def google_hangouts():
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
        driver.switch_to_window(driver.window_handles[0])
        
    def share_location():
        msg_icon.click()
        share_loc = driver.find_element_by_link_text('Share location')
        share_loc.click()
        time.sleep(2)
        map = driver.find_element_by_link_text('I\'m at')
        if map.is_displayed():
            print "Shared location is sent out"
        else:
            print "Shared location does not work"
        
    def share_document():
        shared_doc_url = 'https://docs.google.com/document/d/1sNwpUtoLALl2kD1WAhQPZMDFVBa9DmUKOok6-ywBYe4/edit'
        driver.switch_to_window(driver.window_handles[1])
        driver.get(shared_doc_url)
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[0])
        msg_icon.click()
        share_doc = driver.find_element_by_link_text('Share document')
        share_doc.click()
        time.sleep(2)
        xpath = "//li[@jsc_id='1sNwpUtoLALl2kD1WAhQPZMDFVBa9DmUKOok6-ywBYe4']/a[@href='ws://']"
        shared_doc = driver.find_element_by_xpath(xpath)
        shared_doc.click()
        time.sleep(2)
        xpath = "//a[contains(@href,'docs.google.com/a/esna')]"
        shared_doc_link = driver.find_element_by_xpath(xpath)
        if shared_doc_link.is_displayed():
            print "Shared document is sent"
        else:
            print "Shared document link does not work"
    def share_web_page():
        msg_icon.click()
        share_doc = driver.find_element_by_link_text('Share web page').click()
        time.sleep(2)
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
    
    def clear_history():
        msg_icon.click()
        clear_his = driver.find_element_by_link_text('Clear history').click()
        time.sleep(1)
        xpath = "//div[@class='nodata hidden']"
        blank_area = driver.find_element_by_xpath(xpath)
        if blank_area.is_displayed():
            print "log histrory is cleared"
        else:
            print "Clear history does not work"
    
    def groups_link():
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
    
    def remove_contact():
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
            
    equinox_link()
    google_hangouts()
    share_location()
    share_document()
    share_web_page()
    clear_history()
    groups_link()
    remove_contact()
    
# contact_actions(driver1)