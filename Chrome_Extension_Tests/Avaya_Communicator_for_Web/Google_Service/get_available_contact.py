# -*- coding: utf-8 -*-
'''
Created on Jul 20, 2017

@author: qcadmin
'''
import time
from selenium.webdriver.common.keys import Keys

def add_get_available_contact(driver1):
    print "Test the interact activities between two accounts"
    def add_available_contact_to_favorite():
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
            conct.click()
            print "Contact is in Favorite group already"
            driver.find_element_by_xpath("//a[@title='People']").click()
            print "Click People icon"
            time.sleep(3)
        except:
            print "Add contact to favorite group"
            try:
                xpath = "//a[contains(.,'Skip tutorial')]"
                driver.find_element_by_xpath(xpath).click()
                time.sleep(2)
                print "Account logged in, skipped tutorial"
            except:
                print "Account logged in, tutorial is not popped up"
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
            driver.find_element_by_xpath("//a[@title='People']").click()
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
        
    add_available_contact_to_favorite()
    get_the_available_contact()
    
    