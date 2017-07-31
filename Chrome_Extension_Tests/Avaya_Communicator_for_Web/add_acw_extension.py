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
acw_file = dir_path + '\/avaya_1.0.17.1725.crx'
def add_chrome_extension():
    chop = webdriver.ChromeOptions()
    chop.add_extension(acw_file)
#     disable = webdriver.ChromeOptions.add_argument("--enable-save-password-bubble=false")
    driver = webdriver.Chrome(chrome_options=chop)
    time.sleep(3)
    return driver

# driver = add_chrome_extension()

    




