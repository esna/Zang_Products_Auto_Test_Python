'''
Created on May 2, 2017

@author: qcadmin
'''
import datetime

date_list = []
for i in range(1, 6):
    tmr = datetime.date.today() + datetime.timedelta(days=i)
    di = datetime.datetime.strptime("%s" % tmr, '%Y-%m-%d')
    date_got = datetime.date.strftime(di, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
    date_list.append(date_got)
print date_list[0]