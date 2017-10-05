import datetime, time

tmr = datetime.date.today() + datetime.timedelta(days=1)
tmr_plus_one = datetime.date.today() + datetime.timedelta(days=2)
tmr_plus_3 = datetime.date.today() + datetime.timedelta(days = 3)
d1 = datetime.datetime.strptime("%s" % tmr, '%Y-%m-%d')
# d2 = datetime.datetime.strptime("%s" % tmr_plus_one, '%Y-%m-%d')
d3 = datetime.datetime.strptime("%s" % tmr_plus_3, '%Y-%m-%d')
tomorrow = datetime.date.strftime(d1, 'X%d/X%m/X%Y').replace('X0', 'X').replace('X', '')
# tom_plus_one = datetime.date.strftime(d2, 'X%m/X%d/X%Y').replace('X0', 'X').replace('X', '')
tom_plus_3 = datetime.date.strftime(d3, 'X%d/X%m/X%Y').replace('X0', 'X').replace('X', '')
input_dt = tomorrow
end_dt = tom_plus_3

print input_dt
print end_dt