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
        print ""
        time.sleep(1)
    except:
        time.sleep(1)
        print "Resource %s is not found"
        
    



    
    