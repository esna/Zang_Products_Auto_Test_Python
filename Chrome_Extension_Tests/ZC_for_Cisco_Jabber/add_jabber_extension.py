'''
Created on May 18, 2017

@author: qcadmin
'''

from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options

# os.chdir(r'D:\Chrome_Extension_Tests\iLink_for_Webex_Testing')
    #     print os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
# print dir_path
jabber_file = dir_path + '\/jabber_10.1.17.1801.crx'
plugin_file = dir_path + '\/extension_3_1_0_363.crx'

def add_chrome_extension():
        chop = webdriver.ChromeOptions()
        print "Add the Cisco Communicator for Web plugin"
        chop.add_extension(plugin_file)
        print "Add Cisco Jabber Extension"
        chop.add_extension(jabber_file)
        driver = webdriver.Chrome(chrome_options=chop)
        time.sleep(2)
        return driver

# driver = add_chrome_extension()

    




