
'''
Created on Jun 20, 2017

@author: qcadmin
'''
import time

new_label = "New Presence Label"
new_group = 'Test1'
softphone = "Ready : Softphone [Reidz]"
member1 = "Alec"
member2 = "Percy"
# driver = acw_account_login.login_account_1_google()
time.sleep(2)

def group_test(driver):
    def add_group():
        print "Click People icon"
        driver.find_element_by_xpath("//a[@title='People']").click()
        time.sleep(1)
        print "Click Group button"
        driver.find_element_by_xpath("//a[@jsc_id='ActGroups'][contains(.,'Groups')]").click()
        time.sleep(1)
        xpath = "//a[@class='nodata-link nodata-add']/div[contains(.,'Add group')]"
        add_gp = driver.find_element_by_xpath(xpath)
        print "Click Add Group button"
        add_gp.click()
        time.sleep(2)
        xpath = "/html/body/div/div[1]/div[3]/div[1]/div/div[2]/input"
        gp_name = driver.find_element_by_xpath(xpath)
        gp_name.click()
        gp_name.clear()
        print "Input new group name"
        gp_name.send_keys(new_group)
        xpath = "//a[@href='ws://'][contains(.,'OK')]"
        ok_btn = driver.find_element_by_xpath(xpath)
        print "Click OK button"
        ok_btn.click()
        time.sleep(2)
        
    def add_group_member():
        print "Search first group member"
        search_xpath = "//input[@placeholder='Search people']"
        search = driver.find_element_by_xpath(search_xpath)
        search.click()
        search.clear()
        search.send_keys('Alec')
        time.sleep(2)
        mbr_xpath = "//a[@href='ws://']/div/div/div[contains(.,'%s')]" % member1
        new_mbr = driver.find_element_by_xpath(mbr_xpath)
        driver.execute_script("arguments[0].scrollIntoView(true);", new_mbr)
        time.sleep(2)
        try:
            xpath = "//a[@class='tut-view-next done']"
            driver.find_element_by_xpath(xpath).click()
            print "Company vs Contact notice is clicked"
        except:
            print "Company vs Contact notice is not displayed"
        new_mbr.click()
        print "Click member icon"  
        driver.find_element_by_xpath("//a[@title='Add to group']").click()
        print "Click add to group"
        time.sleep(1)
        print "The first member is added to group"
        
        print "Inpunt second group member"
        search.clear()
        search.send_keys('Percyt')
        time.sleep(5)
        mbr_xpath_2 = "//a[@href='ws://'][@title='percyt@esna.com']//div[contains(.,'%s')]" % member2
        new_mbr_2 = driver.find_element_by_xpath(mbr_xpath_2)
#         driver.execute_script("arguments[0].style.visibility = 'visible';", new_mbr_2)
        time.sleep(2)
        new_mbr_2.click()
        print "Click member icon"  
        driver.find_element_by_xpath("//a[@title='Add to group']").click()
        print "Click add to group"
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='icon iOK']/a[contains(.,'Close')]").click()
        print "Second member is input"
        time.sleep(2)
        print "Click People icon"
        driver.find_element_by_xpath("//a[@title='People']").click()
        time.sleep(2)
        
    def remove_group_member():
        print "Click Group button"
        driver.find_element_by_xpath("//a[@jsc_id='ActGroups'][contains(.,'Groups')]").click()
        time.sleep(1)
        xpath = "//a[@jsc_id='%s']/div" % new_group
        added_gp = driver.find_element_by_xpath(xpath)
        added_gp.click()
        time.sleep(2)
        edit_xpath = "//a[@title='Manage group members']"
        edit_mbr = driver.find_element_by_xpath(edit_xpath)
        edit_mbr.click()
        print "Click edit icon"
        xpath = "//div[contains(.,'%s')]" % member2
        mbr_2 = driver.find_element_by_xpath(xpath)
        print "Click added member 2"
        mbr_2.click()
        time.sleep(2)
        mbr_xpath = "//a[@href='ws://']//div[contains(.,'%s')]" % member2
        mbr_2 = driver.find_element_by_xpath(mbr_xpath)
        mbr_2.click()
        print "Click trash icon"
        driver.find_element_by_xpath("//li[contains(@_id,'%s')]/a[2]" % member2.lower()).click()
        driver.find_element_by_xpath("//div[@class='icon iOK']/a[contains(.,'Close')]").click()
        time.sleep(2)
        print "Second member is deleted"
        print "Click People icon"
        driver.find_element_by_xpath("//a[@title='People']").click()
        time.sleep(2)
        
    def remove_added_group():
        print "Click Group button"
        driver.find_element_by_xpath("//a[@jsc_id='ActGroups'][contains(.,'Groups')]").click()
        time.sleep(1)
        xpath = "//a[@jsc_id='%s']/div" % new_group
        added_gp = driver.find_element_by_xpath(xpath)
        added_gp.click()
        time.sleep(2)
        edit_gp_xpath = "//a[@title='Edit']"
        edit_gp = driver.find_element_by_xpath(edit_gp_xpath)
        edit_gp.click()
        time.sleep(2)
        print "Click edit group icon"
        xpath = "//div[@class='icon iDelete']/a"
        del_gp = driver.find_element_by_xpath(xpath)
        del_gp.click()
        time.sleep(1)
        xpath = "//div[@class='icon iOK']/a"
        ok_btn = driver.find_element_by_xpath(xpath)
        ok_btn.click()
        print "Added group %s is removed" % new_group
        time.sleep(1)
        print "Click People icon"
        driver.find_element_by_xpath("//a[@title='People']").click()
        time.sleep(2)
        return driver
    
    add_group()
    add_group_member()
    remove_group_member()
    remove_added_group()
