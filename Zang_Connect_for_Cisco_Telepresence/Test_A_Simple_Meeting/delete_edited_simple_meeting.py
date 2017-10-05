'''
Created on May 11, 2017

@author: qcadmin
'''
import time
import Login_Gmail_Get_Calendar
import edit_created_simple_meeting

new_mt_room = edit_created_simple_meeting.new_mt_room
driver = Login_Gmail_Get_Calendar.driver

def locate_edited_meeting():
    try:
        xpath = "//div[@class='cpchip']/span[contains(., '%s')]" % new_mt_room
        driver.find_element_by_xpath(xpath)
        edt_meeting = driver.find_element_by_xpath(xpath)
        print "Found the edited meeting"
        edt_meeting.click()
        print "Meeting link is clicked"
        time.sleep(2)
    except:
        print 'The edited meeting is not found'
        driver.close()
        driver.quit()
    
def delete_edited_meeting():
    driver.switch_to_active_element()
    xpath = "//div[@class='neb-footer']/span[2]/div[1]"
    del_btn = driver.find_element_by_xpath(xpath)
    del_btn.click()
    driver.switch_to_active_element()
    try:
        confirm_btn = driver.find_element_by_name("yes")
        confirm_btn.click()
        print "The simple meeting is deleted from google calendar"
    except:
        print "The simple meeting is deleted from google calendar"
    
# if __name__ == '__main__':
    
#     Login_Gmail_Get_Calendar.login_gmail_account()
#     Login_Gmail_Get_Calendar.go_to_google_calendar()
#     locate_edited_meeting()
#     delete_edited_meeting()
#     driver.quit()