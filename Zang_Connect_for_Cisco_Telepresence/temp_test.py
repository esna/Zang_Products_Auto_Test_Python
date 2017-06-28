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



import csv


map_file = "C:/TMS_Resources/resources_map_google.csv"
tms_res = "C:/TMS_Resources/resources_tms.csv"
tms_res_dict = {}

tms_res_room1 = ''
tms_res_room2 = ''

"""read first line from mapping file, get google id"""
with open (map_file, 'r') as f:
    lines = f.readlines()
    line = lines[0]
    tid1 = line.split(",")[0]
    line = lines[1]
    tid2 = line.split(",")[0]


"""get tms resource name from csv file"""
reader = csv.reader(open(tms_res, 'r'))
for row in reader:
    k = row[0]
    v = row[1]
    tms_res_dict[k] = v
    
for v in tms_res_dict:
    if v == tid1:
        tms_res_room1 = tms_res_dict[v]
#     elif v == tid2:
#         tms_res_room2 = tms_res_dict[v]
        break
    else:
        continue

print tms_res_room1
    


 













