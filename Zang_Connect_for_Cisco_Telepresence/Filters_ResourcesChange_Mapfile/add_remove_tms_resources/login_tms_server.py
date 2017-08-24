'''
Created on May 11, 2017

@author: qcadmin
'''
import Login_Gmail_Get_Calendar
import time

pswd = "Esnareid9"
driver = Login_Gmail_Get_Calendar.driver
url = '192.168.1.164/tms/default.aspx?pageId=77'

def login_tms_server():
    driver.get('http://reidz@esna.main:%s@%s'% (pswd, url))
    print "Login tms server and display the conference list"
    time.sleep(2)