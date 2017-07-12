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
print "Get the Company Name list"
time.sleep(2)

for new_res_names in name_list:
    try:
        xpath = "//*[contains(.,'%s')]/preceding-sibling::td/input" % new_res_names
        chk_box = driver.find_element_by_xpath(xpath)
        chk_box.click()
        print "Select %s" % new_res_names
        time.sleep(1)
        del_btn = driver.find_element_by_name('ctl00$uxContent$ctl01$folderPageHost$uxFolderPageViewModule$deleteButton')
        print "Click Delete button"
        del_btn.click()
        time.sleep(1)
        driver.switch_to_active_element()
        pur_btn = driver.find_element_by_id('ctl00_uxContent_ctl01_folderPageHost_uxFolderPageViewModule_uxDeleteButton')
        pur_btn.click()
        print "Click Delete button to confirm"
        time.sleep(1)
        try:
            xpath = "//span[contains(.,'%s')]" % new_res_names
            new_res = driver.find_element_by_xpath(xpath)
            if new_res.is_displayed():
                print "%s is still existed, delete is not successful" % new_res_names
        except:
            print "%s is deleted" % new_res_names
    except:
        time.sleep(1)
        print "Resource %s is not found" % new_res_names
    
print "Test ends"


        
    



    
    