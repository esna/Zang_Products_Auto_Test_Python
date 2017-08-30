'''
Created on Aug 29, 2017

@author: qcadmin
'''
import time
msg = 'test message from account1 to accont2'
contact = 'Percy Teng'

def messages_and_calls(driver1):

    def send_message_to_contact():
        driver = driver1
        msg_icon = driver.find_element_by_link_text('MESSAGES')
        msg_icon.click()
        print "Click the Messages icon"
        try:
            xpath = "//div/textarea[@placeholder='Type a message...']"
            type_box = driver.find_element_by_xpath(xpath)
            type_box.clear()
            type_box.send_keys(msg)
            send_btn = driver.find_element_by_link_text('SEND')
            send_btn.click()
            print "test message sent to account 2"
        except:
            print "The contact is not online"
                
    def phone_call():
        driver = driver1
        xpath = "//input[@placeholder='Search or dial']"
        search_box = driver.find_element_by_xpath(xpath)
        search_box.clear()
        search_box.send_keys(contact)
        xpath = "//a/div/div[contains(.,'%s')]" % contact
        driver.find_element_by_xpath(xpath).click()
        time.sleep(1)
        try:
            driver.find_element_by_link_text("Skip tutorial").click()
            print "Skip the tutorial message"
            time.sleep(1)
        except:
            print "Tutorial is not displayed"
        driver.find_element_by_xpath("//a[@jsc_id='ActCall']").click()
        time.sleep(25)
        driver.switch_to_active_element()
        xpath = "//li[@class='iCall']/a/div[contains(.,'4346')]"
        dial = driver.find_element_by_xpath(xpath)
        dial.click()
        
        
#     send_message_to_contact()
    phone_call()
        
        
        
        
        
        
        
        