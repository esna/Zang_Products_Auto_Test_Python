'''
Created on Jun 23, 2017

@author: qcadmin
'''
import time
# from Avaya_Communicator_for_Web.acw_functionalities import acw_account_login
from selenium.webdriver.common.keys import Keys

softphone = "Ready : Softphone [Reidz]"
# driver = acw_account_login.login_account_1_google()
time.sleep(2)

def settings_test(driver):
    aval_xpath = "//div[@class='imp']"
    aval = driver.find_element_by_xpath(aval_xpath)
    aval.click()
    time.sleep(2)
    print ''
    print "Click the Availability"
    xpath = "//li[@class='iPhoneSoft']/a[@href='ws://']/div[contains(.,'Softphone')]"
    s_phone = driver.find_element_by_xpath(xpath)
    s_phone.click()
    print "Select Softphone"
    time.sleep(10)
    """Need to manually click the 'Allow' button on WebRTC page"""
    try:
        xpath = "//div[@class='phone'][contains(.,'Ready')]"
        phone_type = driver.find_element_by_xpath(xpath)
        if phone_type.text == softphone:
            print "Phone type is switched to softphone"
        else:
            print"Softphone connection failed"
    except:
        print "WebRTC request is not response, soft phone is not connected."
    xpath = "//div[@class='icons left']/a[@title='Menu']"
    menu = driver.find_element_by_xpath(xpath)
    menu.click()
    time.sleep(2)
    print "Menu icon is clicked"
    try:
        xpath = "//a[contains(.,'Skip tutorial')]"
        driver.find_element_by_xpath(xpath).click()
        time.sleep(2)
        print "Account logged in, skipped tutorial"
    except:
        print "Account logged in, tutorial is not popped up"
    xpath = "//div[@class='icons right']/a[@title='Settings']"
    setting = driver.find_element_by_xpath(xpath)
    setting.click()
    time.sleep(1)
    print "Click settings button"
    
    def devices():
        xpath = "//div[@class='tabs']/a[contains(.,'Devices')]"
        device = driver.find_element_by_xpath(xpath)
        device.click()
        print "Click Devices tab"
        time.sleep(2)
        
        """Playback devices"""
        xpath = "//li[@_id='Playback_communications']/a/div"
        comm = driver.find_element_by_xpath(xpath)
        comm.click()
        print "Click Communications button"
        time.sleep(2)
        xpath = "//a[@href='ws://']/div[contains(.,'HD Audio')]"
        hd_audio = driver.find_element_by_xpath(xpath)
        hd_audio.click()
        time.sleep(2)
        print "Click the HD Audio button"
        xpath = "//a[@href='ws://']/div[contains(.,'Speakers')]"
        speakers = driver.find_element_by_xpath(xpath)
        speakers.click()
        time.sleep(2)
        print "Click the Speakers button"
        xpath = "//a[@href='ws://']/div[contains(.,'Default')]"
        default = driver.find_element_by_xpath(xpath)
#         driver.execute_script("arguments[0].scrollIntoView(true);", default)
        default.click()
        time.sleep(2)
        print "Click Default button"
        
        """recording devices"""
        xpath = "//li[@jsc_id='Recording_communications']/a/div"
        rec_comm = driver.find_element_by_xpath(xpath)
#         driver.execute_script("arguments[0].scrollIntoView(true);", default)
        rec_comm.click()
        print "Click recording communications button"
        time.sleep(2)
        xpath = "//a[@href='ws://']/div[contains(.,'Microphone')]"
        mic = driver.find_element_by_xpath(xpath)
        mic.click()
        print "Click Microphone icon"
        time.sleep(2)
        xpath = "//li[@class='Recording']/a/div[contains(.,'Stereo')]"
        stereo_mix = driver.find_element_by_xpath(xpath)
        driver.execute_script("arguments[0].scrollIntoView(true);", stereo_mix)
        stereo_mix.click()
        print "Click Stereo Mix button"
        time.sleep(2)
        xpath = "//li[@jsc_id='Recording_default']/a/div"
        rec_def = driver.find_element_by_xpath(xpath)
        rec_def.click()
        print "Click Recording Default button"
        time.sleep(2)
        
        """Device control packages"""
        xpath = "//li[@jsc_id='Control_jabra']/a/div"
        jabra = driver.find_element_by_xpath(xpath)
        jabra.click()
        print "Click Jabra icon"
        time.sleep(2) 
        xpath = "//li[@jsc_id='Control_plantronics']/a/div"
        plant = driver.find_element_by_xpath(xpath)
        plant.click()
        print "Click Plantronics icon"
        time.sleep(2) 
        xpath = "//li[@jsc_id='Control_none']/a/div"
        none = driver.find_element_by_xpath(xpath)
        none.click()
        print "Click None icon"
        print ''
        time.sleep(2) 
    
    def options():
        xpath = "//div[@class='tabs']/a[contains(.,'Options')]"
        device = driver.find_element_by_xpath(xpath)
        device.click()
        print "Click Options tab"
        time.sleep(2)
        """View all options, check all those unchecked"""
        check = 'checked'
        auto_xpath_1 = "//li[@class='icon iDial']/a/div"
        auto_xpath_2 = "//li[@class='icon iDial %s']/a/div" % check
        try:
            auto_answ_1 = driver.find_element_by_xpath(auto_xpath_1)
            auto_answ_1.click()
            print "Checked the Autoanswer when available"
        except:
            auto_answ_2 = driver.find_element_by_xpath(auto_xpath_2)
            if auto_answ_2.is_displayed():
                print "Autoanser when available option is already checked"
        video_xpath_1 = "//li[@class='icon iStartVideo']/a/div"
        video_xpath_2 = "//li[@class='icon iStartVideo %s']/a/div" % check
        try:
            video_1 = driver.find_element_by_xpath(video_xpath_1)
            video_1.click()
            print "Checked theStart Video automatically"
        except:
            video_2 = driver.find_element_by_xpath(video_xpath_2)
            if video_2.is_displayed():
                print "Start Video automatically option is already checked"
        e164_xpath_1 = "//li[@jsc_id='ActE164'][@class='icon iPhone']/a/div"
        e164_xpath_2 = "//li[@jsc_id='ActE164'][@class='icon iPhone %s']/a/div" % check
        try:
            e164_1 = driver.find_element_by_xpath(e164_xpath_1)
            e164_1.click()
            print "Checked the E.164 dialing"
        except:
            e164_2 = driver.find_element_by_xpath(e164_xpath_2)
            if e164_2.is_displayed():
                print "E.164 dialing option is already checked"
        time.sleep(2)
        
        all_m_xpath_1 = "//li[@jsc_id='ActDPEAll'][@class='icon iPhone']/a/div"
        all_m_xpath_2 = "//li[@jsc_id='ActDPEAll'][@class='icon iPhone %s']/a/div" % check
        try:
            all_m_1 = driver.find_element_by_xpath(all_m_xpath_1)
            driver.execute_script("arguments[0].scrollIntoView(true);", all_m_1)
            all_m_1.click()
            print "Checked the Always show all matches"
        except:
            all_m_2 = driver.find_element_by_xpath(all_m_xpath_2)
            driver.execute_script("arguments[0].scrollIntoView(true);", all_m_2)
            if all_m_2.is_displayed():
                print "Always show all matches option is already checked"
                
        g_cal_xpath_1 = "//li[@class='icon iCalendar']/a/div"
        g_cal_xpath_2 = "//li[@class='icon iCalendar %s']/a/div" % check
        try:
            g_cal_1 = driver.find_element_by_xpath(g_cal_xpath_1)
            g_cal_1.click()
            print "Checked Google Calendar"
        except:
            g_cal_2 = driver.find_element_by_xpath(g_cal_xpath_2)
            if g_cal_2.is_displayed():
                print "Google Calendar option is already checked"
        g_houts_xpath_1 = "//li[@class='icon iHangouts']/a/div"
        g_houts_xpath_2 = "//li[@class='icon iHangouts %s']/a/div" % check
        try:
            g_houts_1 = driver.find_element_by_xpath(g_houts_xpath_1)
            g_houts_1.click()
            print "Checked Google Hangouts"
        except:
            g_houts_2 = driver.find_element_by_xpath(g_houts_xpath_2)
            if g_houts_2.is_displayed():
                print "Google Hangouts option is already checked"
        embd_xpath_1 = "//li[@class='icon iEmbed']/a/div"
        embd_xpath_2 = "//li[@class='icon iEmbed %s']/a/div" % check
        try:
            embd_1 = driver.find_element_by_xpath(embd_xpath_1)
            embd_1.click()
            print "Checked Embed to all opened pages"
        except:
            embd_2 = driver.find_element_by_xpath(embd_xpath_2)
            if embd_2.is_displayed():
                print "Checked Embed to all opened pages option is already checked"
        time.sleep(2)
        
        tuto_xpath_1 = "//li[@class='icon iTutorial']/a/div"
        tuto_xpath_2 = "//li[@class='icon iTutorial %s']/a/div" % check
        try:
            tuto_1 = driver.find_element_by_xpath(tuto_xpath_1)
            tuto_1.click()
            tuto_1.click()
            print "Checked Show all tutorials"
        except:
            tuto_2 = driver.find_element_by_xpath(tuto_xpath_2)
            if tuto_2.is_displayed():
                print "Show all tutorials option is already checked"
        
        """Uncheck all the options"""
        auto_answ_2 = driver.find_element_by_xpath(auto_xpath_2)
        driver.execute_script("arguments[0].scrollIntoView(true);", auto_answ_2)
        auto_answ_2.click()
        video_2 = driver.find_element_by_xpath(video_xpath_2)
        video_2.click()
        time.sleep(1)
        e164_2 = driver.find_element_by_xpath(e164_xpath_2)
        e164_2.click()
        all_m_2 = driver.find_element_by_xpath(all_m_xpath_2)
        all_m_2.click()
        g_cal_2 = driver.find_element_by_xpath(g_cal_xpath_2)
        g_cal_2.click()
        g_houts_2 = driver.find_element_by_xpath(g_houts_xpath_2)
        g_houts_2.click()
        embd_2 = driver.find_element_by_xpath(embd_xpath_2)
        embd_2.click()
        tuto_2 = driver.find_element_by_xpath(tuto_xpath_2)
        tuto_2.click()
        print "All the options are unchecked"
    
    def alerts():
        xpath = "//div[@class='tabs']/a[contains(.,'Alerts')]"
        alerts = driver.find_element_by_xpath(xpath)
        alerts.click()
        print "Click Alerts tab"
        time.sleep(2)
        """View all alerts, check all those unchecked"""
        check = 'checked'
        sound_xpath_1 = "//li[@class='icon iSndUse']/a/div"
        sound_xpath_2 = "//li[@class='icon iSndUse %s']/a/div" % check
        try:
            use_sound_1 = driver.find_element_by_xpath(sound_xpath_1)
            use_sound_1.click()
            print "Checked the Autoanswer when available"
        except:
            use_sound_2 = driver.find_element_by_xpath(sound_xpath_2)
            if use_sound_2.is_displayed():
                print "Use Sound option is already checked"
        status_xpath_1 = "//li[@jsc_id='ActNtf']/following-sibling::li[@class='icon iNtf']/a/div"
        status_xpath_2 = "//li[@jsc_id='ActNtf']/following-sibling::li[@class='icon iNtf %s']/a/div" % check
        try:
            status_chg_1 = driver.find_element_by_xpath(status_xpath_1)
            status_chg_1.click()
            print "Check Online status change"
        except:
            status_chg_2 = driver.find_element_by_xpath(status_xpath_2)
            if status_chg_2.is_displayed():
                print "Online status change option is already checked"
        chat_xpath_1 = "//li[@jsc_id='ActChat'][@class='icon iNtf']/a/div"
        chat_xpath_2 = "//li[@jsc_id='ActChat'][@class='icon iNtf %s']/a/div" % check
        try:
            in_chat_1 = driver.find_element_by_xpath(chat_xpath_1)
            in_chat_1.click()
            print "Check Incoming chat"
        except:
            in_chat_2 = driver.find_element_by_xpath(chat_xpath_2)
            if in_chat_2.is_displayed():
                print "Incoming chat option is already checked"       
        avalchg_xpath_1 = "//ul[@class='list icons check']/li[6][@class='icon iNtf']"
        avalchg_xpath_2 = "//ul[@class='list icons check']/li[6][@class='icon iNtf %s']" % check
        try:
            aval_chg_1 = driver.find_element_by_xpath(avalchg_xpath_1)
            aval_chg_1.click()
            print "Check Available status change"
        except:
            aval_chg_2 = driver.find_element_by_xpath(avalchg_xpath_2)
            if aval_chg_2.is_displayed():
                print "Available status change option is already checked"
        call_xpath_1 = "//li[@jsc_id='ActCall'][@class='icon iNtf']/a/div"
        call_xpath_2 = "//li[@jsc_id='ActCall'][@class='icon iNtf %s']/a/div" % check
        try:
            act_call_1 = driver.find_element_by_xpath(call_xpath_1)
            act_call_1.click()
            print "Check Active call"
        except:
            act_call_2 = driver.find_element_by_xpath(call_xpath_2)
            if act_call_2.is_displayed():
                print "Active call option is already checked"
        onlstachg_xpath_1 = "//li[@jsc_id='ActEvtOnl'][@class='icon iNtf']/a/div"
        onlstachg_xpath_2 = "//li[@jsc_id='ActEvtOnl'][@class='icon iNtf %s']/a/div" % check
        try:
            online_stachg_1 = driver.find_element_by_xpath(onlstachg_xpath_1)
            online_stachg_1.click()
            print "Check Online status change"
        except:
            online_stachg_2 = driver.find_element_by_xpath(onlstachg_xpath_2)
            if online_stachg_2.is_displayed():
                print "Online status change option is already checked"
                
        prechg_xpath_1 = "//li[@jsc_id='ActEvtLoc'][@class='icon iNtf']/a/div"
        prechg_xpath_2 = "//li[@jsc_id='ActEvtLoc'][@class='icon iNtf %s']/a/div" % check
        try:
            presc_chg_1 = driver.find_element_by_xpath(prechg_xpath_1)
            presc_chg_1.click()
            print "Check Presence change"
        except:
            presc_chg_2 = driver.find_element_by_xpath(prechg_xpath_2)
            if presc_chg_2.is_displayed():
                print "Presence change option is already checked"
            
        calls_xpath_1 = "//li[@jsc_id='ActMbxCll'][@class='icon iNtf']/a/div"
        calls_xpath_2 = "//li[@jsc_id='ActMbxCll'][@class='icon iNtf %s']/a/div" % check
        try:
            timeln_calls_1 = driver.find_element_by_xpath(calls_xpath_1)
            timeln_calls_1.click()
            print "Check timeline Calls option"
        except:
            timeln_call_2 = driver.find_element_by_xpath(calls_xpath_2)
            if timeln_call_2.is_displayed():
                print "Timeline Calls option is already checked"
        
        """Uncheck all the Alerts options"""
        print "Uncheck all the Alerts options"
        driver.find_element_by_xpath(sound_xpath_2).click()
        driver.find_element_by_xpath(status_xpath_2).click()
        driver.find_element_by_xpath(avalchg_xpath_2)
        driver.find_element_by_xpath(avalchg_xpath_2).click()
        driver.find_element_by_xpath(chat_xpath_2).click()
        driver.find_element_by_xpath(call_xpath_2).click()
        driver.find_element_by_xpath(onlstachg_xpath_2).click()
        driver.find_element_by_xpath(prechg_xpath_2).click()
        driver.find_element_by_xpath(calls_xpath_2).click()
        print "All the Alerts options are unchecked"
        time.sleep(2)
        return driver
        
    devices()
    options()
    alerts()
    
# settings_test()