# -*- coding: utf-8 -*-
'''
Created on Jun 12, 2017

@author: qcadmin
'''

import Login_Gmail_Get_Calendar
import login_tms_server
import time

name_list = ('Test ABC5', 'Test ABC6')

driver = Login_Gmail_Get_Calendar.driver
driver.implicitly_wait(5)
login_tms_server.login_tms_server()

xpath = "//a[contains(.,'System')]"
sys_tab = driver.find_element_by_xpath(xpath)
sys_tab.click()
time.sleep(2)
for new_res_names in name_list:
    try:
        xpath = "//span[contains(.,'%s')]" % new_res_names
        new_res = driver.find_element_by_xpath(xpath)
        if new_res.text == new_res_names:
            print "Resource %s has existed" % new_res_names
            next
    except:
        print "Add %s to tms resources" % new_res_names
        xpath = "//input[@value='Add Systems']"
        add_sys = driver.find_element_by_xpath(xpath)
        add_sys.click()
        time.sleep(1)
        id_un_end = 'ctl00_uxContent_ctl01_folderPageHost_uxAddSystemModule_uxAddRoomTab'
        add_un_end = driver.find_element_by_id(id_un_end)
        add_un_end.click()
        res_name = 'ctl00$uxContent$ctl01$folderPageHost$uxAddSystemModule$addRoomsPage$roomNameTextBox'
        add_name = driver.find_element_by_name(res_name)
        add_name.send_keys(new_res_names)
        xpath = "//input[@value='Next »']"
        next_btn = driver.find_element_by_xpath(xpath)
        next_btn.click()
        time.sleep(2)
        xpath = "//input[@value='Next »']"
        next_btn = driver.find_element_by_xpath(xpath)
        next_btn.click()
        time.sleep(2)
        print "New resource %s is added into tms resources" % new_res_names
print "Test ends"
# driver.quit()

