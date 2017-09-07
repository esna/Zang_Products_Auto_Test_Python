'''
Created on Aug 29, 2017

@author: qcadmin
'''
import time
msg = 'test message from account1 to accont2'
msg2 = 'replied message from account2'
acct1 = 'Dev1'
acct2 = 'Zang'
acct2_email = acct2.lower()

def interact_messages_and_calls(driver1, driver2):

    def send_message_to_contact():
        driver = driver1
        xpath = "//input[@placeholder='Search or dial']"
        search_box = driver.find_element_by_xpath(xpath)
        print "Search the specified contact"
        search_box.clear()
        search_box.send_keys(acct2)
        time.sleep(5)
        try:
            driver.find_element_by_link_text('Got it')
            print "Acknowledge the remind message"
        except:
            print "Remind message is not displayed"
        xpath = "//a[contains(@title,'%s')]/div/div" % acct2_email
        conct = driver.find_element_by_xpath(xpath)
        conct.click()
        time.sleep(1)
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
        time.sleep(2)
            
    def validate_reply_message():
        driver = driver2
        driver.find_element_by_xpath("//a[@title='Menu']").click()
        time.sleep(1)
        try:
            xpath = "//a[contains(.,'Skip tutorial')]"
            driver.find_element_by_xpath(xpath).click()
            time.sleep(3)
            print "Account logged in, skipped tutorial"
        except:
            print "Account logged in, tutorial is not popped up"
        driver.find_element_by_xpath("//li[@class='iChat']/a/i").click()
        time.sleep(2)
        xpath = "//a[@href='ws://']//div[contains(.,'%s')]" % acct1
        driver.find_element_by_xpath(xpath).click()
        time.sleep(2)
        try:
            xpath = "//a[contains(.,'Skip tutorial')]"
            driver.find_element_by_xpath(xpath).click()
            time.sleep(3)
            print "Account logged in, skipped tutorial"
        except:
            print "Account logged in, tutorial is not popped up"
        xpath = "//div[@class='chat'][contains(.,'%s')]" % msg
        recv_msg = driver.find_element_by_xpath(xpath)
        if recv_msg.is_displayed():
            print "Account 2 received the message sent by account 1"
        else:
            print "Message sent by account 1 is not displayed"
        
        msg_icon = driver.find_element_by_link_text('MESSAGES')
        msg_icon.click()
        print "Click the Messages icon"
        try:
            xpath = "//div/textarea[@placeholder='Type a message...']"
            type_box = driver.find_element_by_xpath(xpath)
            type_box.clear()
            type_box.send_keys(msg2)
            send_btn = driver.find_element_by_link_text('SEND')
            send_btn.click()
            print "send reply message to account 1"
        except:
            print "The contact is not online"
        time.sleep(2)
                
    def verify_shared_received_messages():
        pass
                
    def phone_call():
        driver = driver1
        xpath = "//input[@placeholder='Search or dial']"
        search_box = driver.find_element_by_xpath(xpath)
        search_box.clear()
        search_box.send_keys(acct1)
        xpath = "//a/div/div[contains(.,'%s')]" % acct1
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
        
        
    send_message_to_contact()
    validate_reply_message()
#     phone_call()
        