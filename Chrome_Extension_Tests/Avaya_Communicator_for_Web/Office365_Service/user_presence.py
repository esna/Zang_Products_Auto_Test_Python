'''
Created on Jun 20, 2017

@author: qcadmin
'''
import time
# from Avaya_Communicator_for_Web.acw_functionalities import acw_account_login
from selenium.webdriver.common.keys import Keys

new_label = "New Presence Label"
softphone = "Ready : Softphone [Reidz]"
aval_status1 = 'Available'
aval_status2 = 'Busy'
aval_status3 = 'Unavailable'
aval_status4 = 'Offline'
# driver = acw_account_login.login_account_1_google()
time.sleep(2)

def presence_test(driver):
    aval_xpath = "//div[@class='imp']"
    aval = driver.find_element_by_xpath(aval_xpath)
    aval.click()
    print "Click the Availability"
    time.sleep(2)
    if aval.text == aval_status1:
        print "%s is displayed on the main panel" % aval_status1
    elif aval.text == aval_status2:
        print "%s is displayed on the main panel" % aval_status2
    elif aval.text == aval_status3:
        print "%s is displayed on the main panel" % aval_status3
    elif aval.text == aval_status4:
        print "%s is displayed on the main panel" % aval_status4
    else:
        print "Availability status is not found"
    
    for aval_status in (aval_status1, aval_status2, aval_status3):
        if aval.text == aval_status:
            next
        else:
            xpath = "//ul[@class='list icons radio']//li/a/div[contains(.,'%s')]" % aval_status
            radio_btn = driver.find_element_by_xpath(xpath)
            print "Click %s" % aval_status
            radio_btn.click()
            time.sleep(1)
            radio_btn.click()
            time.sleep(1)
            print "%s is displayed on the main panel" % aval_status
    
    xpath = "//input[@placeholder='Enter presence label']"
    input_label = driver.find_element_by_xpath(xpath)
    input_label.clear()
    input_label.send_keys(new_label)
    time.sleep(2)
    input_label.send_keys(Keys.RETURN)
    print "A presence label is input"
    time.sleep(3)
    aval_xpath = "//div[@class='imp']"
    aval = driver.find_element_by_xpath(aval_xpath)
    if aval.text == new_label:
        print "The %s is displayed on the main panel" % new_label
    else:
        print "The new label is not displayed on main panel"
    time.sleep(2)
    xpath = "//li[@jsc_id='ActOnline']/a[@href='ws://']/div[contains(.,'Available')]"
    avail = driver.find_element_by_xpath(xpath)
    avail.click()
    print "Click Available"
    time.sleep(2)
    aval = driver.find_element_by_xpath(aval_xpath)
    aval_label = 'Available'
    assert aval_label == aval.text
    print "%s is displayed on the main panel" % aval_label
    time.sleep(2)
    return driver
    
#     xpath = "//a[@href='ws://']/div[contains(.,'Softphone')]"
#     s_phone = driver.find_element_by_xpath(xpath)
#     s_phone.click()
#     print "Select Softphone"
#     time.sleep(10)
#     """Need to manually click the 'Allow' button on WebRTC page"""
#     xpath = "//div[@class='phone'][contains(.,'Ready')]"
#     phone_type = driver.find_element_by_xpath(xpath)
#     if phone_type.text == softphone:
#         print "Phone type is switched to softphone"
#     else:
#         print"Softphone has problem"

# presence_test()