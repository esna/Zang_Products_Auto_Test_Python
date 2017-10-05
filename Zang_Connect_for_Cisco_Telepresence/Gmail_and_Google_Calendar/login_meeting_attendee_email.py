'''
Created on Jul 12, 2017

@author: qcadmin
'''
import time

url = 'https://accounts.google.com/signin/v2/identifier?hl=en&continue=https%3A%2F%2Fmail.google.com\
%2Fmail&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession'
userid = 'dev01@esnaqc.com'
passwd = 'esnatech'

def guest_email_login(driver):
    driver.get(url)
    print "Go to gmail login interface"
    email = driver.find_element_by_id("identifierId")
    email.clear()
    email.send_keys(userid)
    print "User id is input"
    time.sleep(1)
    xpath = "//div[@id='identifierNext']/content/span"
    next_btn = driver.find_element_by_xpath(xpath)
    next_btn.click()
    print "Click next"
    time.sleep(3)
    Passwd = driver.find_element_by_name("password")
    Passwd.clear()
    Passwd.send_keys(passwd)
    print "User password is input"
    xpath = "//div[@id='passwordNext']/content/span"
    next_btn = driver.find_element_by_xpath(xpath)
    next_btn.click()
    print "Gmail account is logged in"
    time.sleep(3)
    
def go_to_google_calendar(driver):
    print "Go to google calendar"
    driver.get("https://calendar.google.com/calendar/render?tab=mc#main_7")
    time.sleep(5)
