'''
Created on May 24, 2017

@author: qcadmin
'''
from iLink_for_Webex_Testing import add_login_webex_extension
from selenium.webdriver.support.ui import Select
import time

new_templt = 'Webex New Template Testing'
driver = add_login_webex_extension.driver

def test_save_delete_template_with_Google_service():
    print "Test save and delete template with google service"
    def sso_with_google_credential():
        add_login_webex_extension.login_ext_with_google()
        add_login_webex_extension.input_esna_webex_password()
        time.sleep(5)
    
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
        print ''
        time.sleep(2)
        
    sso_with_google_credential()
    create_template()
    save_new_temaplate()
    delete_created_template()
    driver.quit()
    
def test_save_delete_template_with_0ffice365_service():
    print "Test save and delete template with office365 service"
    driver = add_login_webex_extension.driver
    def sso_with_o365_credential():
        add_login_webex_extension.login_ext_with_office365()
        add_login_webex_extension.input_esna_webex_password()
        time.sleep(5)
    
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
        print ''
        time.sleep(2)
    
    sso_with_o365_credential()
    create_template()
    save_new_temaplate()
    delete_created_template()
    
    
test_save_delete_template_with_Google_service()
# test_save_delete_template_with_0ffice365_service()
# driver.quit()
