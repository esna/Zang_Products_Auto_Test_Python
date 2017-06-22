'''
Created on Jun 20, 2017

@author: qcadmin
'''
import time
import acw_account_login
from selenium.webdriver.common.keys import Keys

new_label = "New Presence Label"
softphone = "Ready : Softphone [Reidz]"
driver = acw_account_login.login_account_1_google()
time.sleep(2)

def presence_test():
    aval_xpath = "//div[@class='imp']"
    aval = driver.find_element_by_xpath(aval_xpath)
    aval.click()
    print "Click the Availability"
    time.sleep(2)
    aval_label = 'Available'
    assert aval_label == aval.text
    print "%s is displayed on the main panel" % aval_label
    
    xpath = "//li[@class='iAway']/a/div[contains(.,'Busy')]"
    busy = driver.find_element_by_xpath(xpath)
    busy.click()
    busy.click()
    print "Click Busy"
    time.sleep(2)
    aval = driver.find_element_by_xpath(aval_xpath)
    aval_label = 'Busy'
    assert aval_label == aval.text
    print "%s is displayed on the main panel" % aval_label
    
    xpath = "//a[@href='ws://']/div[contains(.,'Unavailable')]"
    un_aval = driver.find_element_by_xpath(xpath)
    un_aval.click()
    print "Click Unavailable"
    time.sleep(2)
    aval = driver.find_element_by_xpath(aval_xpath)
    aval_label = 'Unavailable'
    assert aval_label == aval.text
    print "%s is displayed on the main panel" % aval_label
    
    xpath = "//input[@placeholder='Enter presence label']"
    input_label = driver.find_element_by_xpath(xpath)
    input_label.clear()
    input_label.send_keys(new_label)
    time.sleep(2)
    input_label.send_keys(Keys.RETURN)
    print "A presence label is input"
    time.sleep(2)
    aval_xpath = "//div[@class='imp']"
    aval = driver.find_element_by_xpath(aval_xpath)
    if aval_label == aval.text:
        print "The %s is displayed on the main panel" % new_label
    else:
        print "The new label is not displayed on main panel"
    
    xpath = "//a[@href='ws://']/div[contains(.,'Available')]"
    avail = driver.find_element_by_xpath(xpath)
    avail.click()
    print "Click Available"
    time.sleep(2)
    aval = driver.find_element_by_xpath(aval_xpath)
    aval_label = 'Available'
    assert aval_label == aval.text
    print "%s is displayed on the main panel" % aval_label
    
    xpath = "//a[@href='ws://']/div[contains(.,'Softphone')]"
    s_phone = driver.find_element_by_xpath(xpath)
    s_phone.click()
    print "Select Softphone"
    time.sleep(10)
    """Need to manually click the 'Allow' button on WebRTC page"""
    xpath = "//div[@class='phone'][contains(.,'Ready')]"
    phone_type = driver.find_element_by_xpath(xpath)
    if phone_type.text == softphone:
        print "Phone type is switched to softphone"
    else:
        print"Softphone has problem"

def group_add_edit_delete():
    print "Click People icon"
    driver.find_element_by_xpath("//a[@title='People']").click()
    print "Click Group button"
    driver.find_element_by_xpath("//a[@jsc_id='ActGroups']").click
    xpath = "//a[@href='ws://']/div[contains(.,'Add group')]"
    add_gp = driver.find_element_by_xpath(xpath)
    add_gp.click()
    
    
presence_test()