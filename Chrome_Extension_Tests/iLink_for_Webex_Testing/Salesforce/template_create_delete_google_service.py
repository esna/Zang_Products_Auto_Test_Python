'''
Created on May 24, 2017

@author: qcadmin
'''
from selenium.webdriver.support.ui import Select
import add_extention_sso_sf
import time

new_templt = 'Webex New Template Testing'

def sso_with_sf_credential():
    driver = add_extention_sso_sf.extenstion_and_sso()
    return driver
driver = sso_with_sf_credential()

def create_template():
    driver.find_element_by_id('tabHeaderTemplates').click()
    print "Click Templates tab"
    time.sleep(2)
    driver.switch_to_frame('tpl_iframe')
    create = Select(driver.find_element_by_xpath("//select[@id='comboTemplates']"))
    create.select_by_value('create')
    templt_name = driver.find_element_by_id('id_wexTemplateName')
    templt_name.clear()
    templt_name.send_keys(new_templt)
    print "Input new template name"
    time.sleep(2)
    
def save_new_temaplate():
    save_btn = driver.find_element_by_id('buttonWexTemplateSav')
    save_btn.click()
    print "Save button is clicked"
    time.sleep(2)
    print "Verify the new template"
    try:
        verify = Select(driver.find_element_by_xpath("//select[@id='comboTemplates']"))
        verify.select_by_visible_text('Webex New Template Testing')
        print "New template is created successfully"
    except:
        print "New template is not saved successfully"
    time.sleep(2)
    
def delete_created_template():
    delete = Select(driver.find_element_by_xpath("//select[@id='comboTemplates']"))
    delete.select_by_visible_text('Webex New Template Testing')
    print "Created template is selected"
    time.sleep(2)
    del_btn = driver.find_element_by_id('buttonWexTemplateDel')
    del_btn.click()
    print "Delete button is clicked"
    time.sleep(2)
    print "Verify created temaplate is deleted"
    try:
        verify = Select(driver.find_element_by_xpath("//select[@id='comboTemplates']"))
        verify.select_by_visible_text('Webex New Template Testing')
        print "New template is still there, it's not deleted"
    except:
        print "New template is not found in template list"
    print 'Test ends'
    
sso_with_sf_credential()
create_template()
save_new_temaplate()
delete_created_template()
driver.quit()
    
# driver.quit()
