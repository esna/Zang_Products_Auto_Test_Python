'''
Created on Jun 7, 2017

@author: qcadmin
'''
import time

user_id = 'arnoe@esna.com'
passwd = 'EsnaAvaya06'
url = 'https://login.salesforce.com/?locale=ca'

def login_saleforce_account(driver):
    driver.get(url)
    print "Input account username"
    driver.find_element_by_id('username').send_keys(user_id)
    print "Input account password"
    driver.find_element_by_id('password').send_keys(passwd)
    print "Click login button"
    driver.find_element_by_id('Login').click()
    time.sleep(15)
    return driver

#     def switch_from_classic_to_lightning():
#         try:
#             classic = driver.find_element_by_id('userNavLabel')
#             classic.click()
#             xpath = "//a[@title='Meet the Switcher. Use this link to switch between Salesforce Classic and Lightning Experience whenever you want.']"
#             driver.find_element_by_xpath(xpath).click()
#             print "Interface is changed to Lightning"
#             time.sleep(15)
#         except:
#             print "Salesforce is on Lightning interface"
#         
#     def switch_from_lightning_to_classic():
#         xpath = "(//div[@class='tooltipTrigger tooltip-trigger uiTooltip'])[4]"
#         try:
#             lightning = driver.find_element_by_xpath(xpath)
#             lightning.click()
#             xpath = "//a[contains(.,'Switch to Salesforce Classic')]"
#             driver.find_element_by_xpath(xpath).click()
#             print "Interface is changed to Classic"
#             time.sleep(15)
#         except:
#             print "Salesforce is on classic interface"

# login_saleforce_account()
# switch_from_lightning_to_classic()
# switch_from_classic_to_lightning()



