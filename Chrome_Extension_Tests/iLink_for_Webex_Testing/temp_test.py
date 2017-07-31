'''
Created on May 31, 2017

@author: qcadmin
'''
'''
Created on Mar 28, 2014

@author: Administrator
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import ConfigParser, getopt, os, subprocess, sys
import datetime


driver = webdriver.Chrome()
driver.implicitly_wait(15)

driver.get("C:\\temp\\Esna Technologies Inc WebEx Enterprise Site.html")

for thing in driver.find_elements_by_tag_name('frame'):
        print thing.get_attribute('name')
        
driver.switch_to_frame('mainFrame')
driver.switch_to_frame('menu')
xpath = "//span[contains(.,'My Meetings')]"
driver.find_element_by_xpath(xpath).click()