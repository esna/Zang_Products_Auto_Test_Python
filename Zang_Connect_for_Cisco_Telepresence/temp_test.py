'''
Created on May 2, 2017

@author: qcadmin
'''
# import datetime
# 
# date_list = []
# for i in range(1, 6):
#     tmr = datetime.date.today() + datetime.timedelta(days=i)
#     di = datetime.datetime.strptime("%s" % tmr, '%Y-%m-%d')
#     date_got = datetime.date.strftime(di, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
#     date_list.append(date_got)
# print date_list[0]

# import signal
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# 
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.service.process.send_signal(signal.SIGTERM)

# map_file = "C:/TMS_Resources/resources_map_google.csv"
# with open (map_file, 'r') as f:
#     firstline = f.readline()
#     tid = firstline.split(",")[0]
#     gid = firstline.split(",")[1]


a = 2
b = 3
c = 2

assert a == c
assert a == b

 













