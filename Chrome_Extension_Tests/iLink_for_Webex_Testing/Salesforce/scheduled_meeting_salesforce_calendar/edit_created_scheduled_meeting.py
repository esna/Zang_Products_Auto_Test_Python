'''
Created on Aug 16, 2017

@author: qcadmin
'''
import create_scheduled_meeting
import datetime, time
from selenium.webdriver.support.ui import Select

topic = create_scheduled_meeting.topic
new_topic = 'Edited Saleforce scheduled meeting'
contact_url_classic = create_scheduled_meeting.contact_url_classic
tmr_plus_one = datetime.date.today() + datetime.timedelta(days=2)
d2 = datetime.datetime.strptime("%s" % tmr_plus_one, '%Y-%m-%d')
tom_plus_one = datetime.date.strftime(d2, 'X%d/X%m/X%Y').replace('X0', 'X').replace('X', '')
from_time = "2:00 PM"
until_time = "2:30 PM"
al_host_invalid = "qc@esnaqc.com"
al_host_valid = "reidz@esna.com"
driver = create_scheduled_meeting.driver

def edit_scheduled_meeting():
    
    def edit_salesforce_calendar():
        print "Edit salesforce calendar"
        driver.get(contact_url_classic)
        time.sleep(8)
        print "logged in salesforce with Classic interface"
        print "Click Home tab"
        driver.find_element_by_link_text('Home').click()
        time.sleep(2)
        print "Search the created scheduled meeting"
        try:
            title = driver.find_element_by_link_text(topic)
            driver.execute_script("arguments[0].scrollIntoView(true);", title)
            title.click()
        except:
            print "Created scheduled meeting is not found"
        print "Click the meeting and click edit"
        driver.find_element_by_name('edit').click()
        print "Change the meeting topic"
        sbjt = driver.find_element_by_id('evt5')
        sbjt.clear()
        sbjt.send_keys(new_topic)
        print "Input new start date and time"
        st_date = driver.find_element_by_name('StartDateTime')
        st_date.clear()
        st_date.send_keys(tom_plus_one)
        ed_date = driver.find_element_by_name('EndDateTime')
        ed_date.clear()
        ed_date.send_keys(tom_plus_one)
        st_time = driver.find_element_by_id('StartDateTime_time')
        st_time.clear()
        st_time.send_keys(from_time)
        ed_time = driver.find_element_by_id('EndDateTime_time')
        ed_time.clear()
        ed_time.send_keys(until_time)
        try:
            driver.find_element_by_id('wexFirstTimerButton').click()
        except:
            print "No remind message window popped up"
        time.sleep(2)
    edit_salesforce_calendar()
        
    def edit_webex_menu():
        print "Edit webex menu"
        driver.find_element_by_id('wex0B7Md1').click()
        driver.switch_to_frame('frameCreateWebex')
        time.sleep(1)
        al_host = driver.find_element_by_id('id_altHosts')
        al_host.clear()
        al_host.send_keys(al_host_invalid)
        print "Input an invalid alternate host"
        time.sleep(1)
        xpath = "//span[@id='createWebexSpan']"
        driver.find_element_by_xpath(xpath).click()
        print 'Click Done button'
        time.sleep(2)
        alert = driver.switch_to_alert()
        print "Alert should be popped up, click OK button"
        alert.accept()
        time.sleep(2)
        driver.find_element_by_id('wex0B7Md1').click()
        driver.switch_to_frame('frameCreateWebex')
        time.sleep(1)
        al_host = driver.find_element_by_id('id_altHosts')
        al_host.clear()
        al_host.send_keys(al_host_valid)
        print "Reopen menu and input a valid alternate host"
        time.sleep(1)
        print "Select audio as NONE"
        audio = Select(driver.find_element_by_id('id_wexAudio'))
        audio.select_by_value('NONE')
        driver.find_element_by_xpath(xpath).click()
        print "Click Done button to send out the edit"
        print ""
        time.sleep(2)
        print "Edit scheduled meeting is finished"
    edit_webex_menu()
    
edit_scheduled_meeting()