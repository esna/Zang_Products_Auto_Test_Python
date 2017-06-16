'''
Created on May 30, 2017

@author: qcadmin
'''

from selenium import webdriver
driver = webdriver.Chrome



def print_frame_names():
    for thing in driver.find_elements_by_tag_name('frame'):
        print thing.get_attribute('name')
        
        
def print_multiple_widnow_names():
    for handle in driver.window_handles:
        print "Handle = ",handle
        driver.switch_to_window(handle);
        elem = driver.find_element_by_tag_name("title")
        print elem.get_attribute("value")
        print driver.title