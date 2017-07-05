from iLink_for_Webex_Testing import add_login_webex_extension
import datetime, time

tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
tom_plus_3 = datetime.date.today() + datetime.timedelta(days = 3)
input_dt = tomorrow.strftime("%B %d, %Y")
end_dt = tom_plus_3.strftime("%B %d, %Y")
fromtime = "2:00 PM"
untiltime = "3:00 PM"
title = "Repeat meeting from office 365 calendar"
alter_host = "reidz@esna.com"
passwd = "3333c"
url_o365 = "https://login.microsoftonline.com/"

driver = add_login_webex_extension.driver
add_login_webex_extension.login_ext_with_office365()
time.sleep(20)
add_login_webex_extension.input_esna_webex_password()

def go_to_O365_calendar():
#     print "Go to O365 account"
#     driver.get(url_o365)
#     time.sleep(3)
#     driver.find_element_by_id('O365_MainLink_NavMenu').click()
#     print "Click menu"
#     time.sleep(3)
#     print "Click calendar icon"
#     xpath = "//a[@id='O365_AppTile_Calendar']/div/span"
#     driver.find_element_by_xpath(xpath).click()
#     time.sleep(20)
    cal_url = 'https://outlook.office365.com/owa/?realm=esnatech.onmicrosoft.com&exsvurl=1&ll-cc=1033&modurl=1&path=/calendar'
    print "Go to o365 calendar"
    driver.get(cal_url)
    time.sleep(20)

def input_meeging_data_from_calendar():
    print "input meeting data begin"
    def input_meeting_title():
        print "Click 'New' tab"
        xpath = "//button[@aria-labelledby='_ariaId_29']"
        new_btn = driver.find_element_by_xpath(xpath)
        new_btn.click()
        time.sleep(5)
        xpath = "//input[@aria-label='Add a title for the event']"
        mt_title = driver.find_element_by_xpath(xpath)
        mt_title.clear()
        mt_title.send_keys(title)
        print "Meeting title is input"

    def set_meeting_schedule():
        xpath = "//span[@class='_dx_5 owaimg ms-Icon--calendar ms-icon-tall-glyph ms-icon-font-size-16 ms-fcl-ns-b']"
        st_cal = driver.find_element_by_xpath(xpath)
        st_cal.click()
        time.sleep(1)
        print "Click Calendar Icon"
        cal_xpath = "//div[@class='_dx_6 ms-font-s ms-fwt-r ms-bgc-w contextMenuDropShadow']"
        tom_xpath = "%s//div/abbr[contains(@aria-label,'%s')]"% (cal_xpath, input_dt)
        tom = driver.find_element_by_xpath(tom_xpath)
        print "Input meeeting date"
        tom.click()
        xpath = "//span[@class='_dx_4 ms-fwt-sl ms-font-s']"
        print "Input meeting time"
        from_time = driver.find_element_by_xpath("//input[@aria-label = 'start time']")
        until_time = driver.find_element_by_xpath("//input[@aria-label = 'end time']")
        from_time.clear()
        from_time.send_keys(fromtime)
        until_time.clear()
        until_time.send_keys(untiltime)
        print "Meeting schedule is set"
        time.sleep(2)
        
    def set_repeating_cycle():
        xpath = "//button[@aria-labelledby='MeetingCompose.RepeatLabel MeetingCompose.RepeatDescriptionLabel']/div[2]/span"
        sel_btn = driver.find_element_by_xpath(xpath)
        print "Click the repeat period selector button"
        sel_btn.click()
        time.sleep(2)
        xpath = "//span[contains(.,'Every day')]"
        eve_day = driver.find_element_by_xpath(xpath)
        eve_day.click()
        print "Selected Every day repeat"
        time.sleep(2)
        repeat_cal_xpath = "(//div[@class='RepeatDatePicker'])[2]"
        end_dt_cal_xpath = "%s/div/button/span[2]" % repeat_cal_xpath
        end_dt_sel = driver.find_element_by_xpath(end_dt_cal_xpath)
        end_dt_sel.click()
        print "Click repeat end date calendar"
        time.sleep(2)
        rep_cal_xpath = "(//div[@class='_dx_h _dx_j ms-font-s ms-font-weight-semilight ms-font-color-neutralPrimary'])[3]"
        end_dt_xpath = "%s//div//abbr[contains(@aria-label,'%s')][contains(@style,'width: 30px')]"% (rep_cal_xpath, end_dt)
        end_day = driver.find_element_by_xpath(end_dt_xpath)
        print "Repeat meeting end date selected"
        end_day.click()
        print "Repeating cycle is set"
    input_meeting_title()
    set_meeting_schedule()
    set_repeating_cycle()
    
def create_meeting_from_webex_icon():
    create_btn = driver.find_element_by_id('wexButtonAdd')
    create_btn.click()
    print "Click create button"
    time.sleep(2)
    driver.switch_to_frame('frameCreateWebex')
    print "Test the cancel button"
    driver.find_element_by_id('cancelWebexSpan').click()
    print "Cancel button works"
    time.sleep(1)
    driver.switch_to_default_content()
    create_btn = driver.find_element_by_id('wexButtonAdd')
    create_btn.click()
    time.sleep(1)
    driver.switch_to_frame('frameCreateWebex')
    print "Input alternate host"
    al_host = driver.find_element_by_id('id_altHosts')
    al_host.clear()
    al_host.send_keys(alter_host)
    print "Input password"
    pwd = driver.find_element_by_id('id_txtPin')
    pwd.clear()
    pwd.send_keys(passwd)
    print "Click Done button"
    driver.find_element_by_id('createWebexSpan').click()
    print "Meeting is created from webex icon"
    time.sleep(5)
    
def save_meeting_on_o365_calendar():
    driver.switch_to_default_content
    xpath = "//span[contains(.,'Save')]"
    save_btn = driver.find_element_by_xpath(xpath)
    save_btn.click()
    print "Repeat meeting is saved on calendar"
    time.sleep(5)
    
    
go_to_O365_calendar()
input_meeging_data_from_calendar()
create_meeting_from_webex_icon()
save_meeting_on_o365_calendar()
    