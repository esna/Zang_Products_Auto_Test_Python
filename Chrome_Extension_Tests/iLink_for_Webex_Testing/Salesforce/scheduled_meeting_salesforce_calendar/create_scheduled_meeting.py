from selenium.webdriver.support.ui import Select
from iLink_for_Webex_Testing import add_login_webex_extension
import datetime, time

contact_url_classic = 'https://na88.salesforce.com/003/o'
template = 'Test#Template 1'
topic = 'Salesforce scheduled meeting'
passwd = '5555e'
tmr = datetime.date.today() + datetime.timedelta(days=1)
tmr_plus_one = datetime.date.today() + datetime.timedelta(days=2)
d1 = datetime.datetime.strptime("%s" % tmr, '%Y-%m-%d')
d2 = datetime.datetime.strptime("%s" % tmr_plus_one, '%Y-%m-%d')
tomorrow = datetime.date.strftime(d1, 'X%d/X%m/X%Y').replace('X0', 'X').replace('X', '')
tom_plus_one = datetime.date.strftime(d2, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
fromtime = "12:00 PM"
untiltime = "1:00 PM"

driver = add_login_webex_extension.driver
add_login_webex_extension.login_ext_with_Salesforce()
add_login_webex_extension.input_esna_webex_password()

def create_schdeuled_mting_with_classic_interface():
    driver.get(contact_url_classic)
    time.sleep(8)
    print "logged in salesforce with Classic interface"
    driver.find_element_by_link_text('Home').click()
    time.sleep(2)
    driver.find_element_by_name('newEvent').click()
    time.sleep(2)
    try:
        driver.find_element_by_id('wexFirstTimerButton').click()
    except:
        print "No remind message window popped up"
    sbjt = driver.find_element_by_id('evt5')
    sbjt.clear()
    sbjt.send_keys(topic)
    
    st_date = driver.find_element_by_name('StartDateTime')
    st_date.clear()
    st_date.send_keys(tomorrow)
    ed_date = driver.find_element_by_name('EndDateTime')
    ed_date.clear()
    ed_date.send_keys(tomorrow)
    st_time = driver.find_element_by_id('StartDateTime_time')
    st_time.clear()
    st_time.send_keys(fromtime)
    ed_time = driver.find_element_by_id('EndDateTime_time')
    ed_time.clear()
    ed_time.send_keys(untiltime)
    
    driver.find_element_by_id('wex0B7Cr1').click()
    driver.switch_to_frame('frameCreateWebex')
    create = Select(driver.find_element_by_xpath("//select[@id='comboTemplates']"))
    create.select_by_value('siteLevel1')
    time.sleep(1)
    driver.find_element_by_id('createWebexSpan').click()
    print "Create meeting button is clicked"
    
    """detect and close the popup window of sf calendar"""
    time.sleep(2)
    try:
        default_handle = driver.current_window_handle
        handles = list(driver.window_handles)
        assert len(handles) > 1
        handles.remove(default_handle)
        assert len(handles) > 0
        driver.switch_to_window(handles[0])
        print "Close the popup window"
        driver.close()
        driver.switch_to_window(default_handle)
    except:
        print "No popup window"
        
    driver.find_element_by_name('save').click()
    time.sleep(2)

# create_schdeuled_mting_with_classic_interface()
    