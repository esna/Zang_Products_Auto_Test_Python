'''
Created on May 9, 2017

@author: qcadmin
'''
from selenium import webdriver
import os, time
import ConfigParser
from distutils.sysconfig import project_base
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)
# print BASE_DIR
config_file = BASE_DIR + "\configuration.ini"
Config = ConfigParser.ConfigParser()
Config.read(config_file)

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        #print option
        try:
            dict1[option] = Config.get(section, option)
            def DebugPrint(msg):
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
userid = ConfigSectionMap("Account")['essultn_id_1']
passwd = ConfigSectionMap("Account")['essultn_pwd']

def setUp():
    onusing_browser = ConfigSectionMap("Browser")['onusing']
    if onusing_browser == "1":
        driver = webdriver.Firefox()
    elif onusing_browser == "2":
        driver = webdriver.Chrome()
    else:
        print "We don't support other browsers currently."
    driver.implicitly_wait(15)
    return driver
driver = setUp()

def login_gmail_account():
    driver.get('https://mail.google.com')
    time.sleep(5)
    print "Go to gmail login interface"
    try:
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
    except:
        print "Input password directly"
    Passwd = driver.find_element_by_name("password")
    Passwd.clear()
    Passwd.send_keys(passwd)
    print "User password is input"
    xpath = "//div[@id='passwordNext']/content/span"
    next_btn = driver.find_element_by_xpath(xpath)
    next_btn.click()
    print "Gmail account is logged in"
    time.sleep(3)
    
def go_to_google_calendar():
    print "Go to google calendar"
    driver.get("https://calendar.google.com/calendar/b/2/render?tab=mc#eventpage_6")
    time.sleep(5)



# if __name__ == '__main__':
#     login_gmail_account()
#     go_to_google_calendar()