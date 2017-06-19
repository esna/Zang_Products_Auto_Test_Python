from selenium import webdriver
from Avaya_Communicator_for_Web import add_acw_extension
from Avaya_Communicator_for_Web import acw_account_login
from Avaya_Communicator_for_Web import sso_login
import time

username_1 = 'Reidz@esna.com'
username_2 = 'Percyt@esna.com'
acw_file = add_acw_extension.acw_file


"""Login acw account 1"""
driver = add_acw_extension.add_chrome_extension()
time.sleep(2)
sso_login.login_ext_with_google(driver)
acw_account_login.ipoffice_login(driver, username_1)


"""Login acw account 2"""
driver = add_acw_extension.add_chrome_extension()
time.sleep(2)
sso_login.login_ext_with_google(driver)
acw_account_login.ipoffice_login(driver, username_2)

