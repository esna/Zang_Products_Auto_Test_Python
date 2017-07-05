'''
Created on May 31, 2017

@author: qcadmin
'''
import datetime
import time
import calendar

tmr = datetime.date.today() + datetime.timedelta(days=1)
tmr_plus_one = datetime.date.today() + datetime.timedelta(days=2)
d1 = datetime.datetime.strptime("%s" % tmr, '%Y-%m-%d')
d2 = datetime.datetime.strptime("%s" % tmr_plus_one, '%Y-%m-%d')
tomorrow = datetime.date.strftime(d1, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
tom_plus_one = datetime.date.strftime(d2, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
fromtime = "12:00 PM"

# print tomorrow
# print tmr
# print calendar.month_name[5]
# print tmr.strftime("%B %d, %Y")
# 
# s = "12:00 PM"
# print(s.lower())


tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
tom_plus_3 = datetime.date.today() + datetime.timedelta(days = 3)
input_dt = tomorrow.strftime("%B %d, %Y")
end_dt = tom_plus_3.strftime("%B %d, %Y")
# print end_dt

input_time = tmr.strftime("%b %d, %Y ") + fromtime.lower()
print input_time

