'''
Created on Jul 7, 2017

@author: qcadmin
'''
import os, csv, sys

dir_resource = "C:\TMS_Resources"
dir_uctms = "C:\UC\UCTMS"
os.chdir(dir_resource)

tms_webmt = "WebEx meeting"
tms_wcmr = "WebEx CMR meeting"
tms_newintern = "new intern testing room"
tms_roomA = "New Room A"
tms_abc1 = "Test ABC1"

prefix = "TMSUCREID - "
gcal_test1 = prefix + "test1"
gcal_0_138 = prefix + "No Name (192.168.0.138)"
gcal_wcmr = prefix + "New Room A"
gcal_qc01 = "TMSUCREID qc test 01"
gcal_confA = "Conference A"
gcal_confB = "Conference Room B"

notes_webmt = "Google TMSUCREID test 1-> TMS Webex Meeting"
notes_wcmr = "Google TMSUCREID No Name 0.38 -> TMS Webex CMR"
notes_match1 = "Conference A in Google -> New Room A in TMS"
notes_match2 = "Conference Room B in Google -> new intern testing room in TMS"
notes_match3 = "qc test 01 Google -> Test ABC1 in TMS"

"""get tms resources id from exported resources file"""
with open ('resources_tms.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if tms_webmt in row:
            tid_webmt = row[0]
        elif tms_wcmr in row:
            tid_wcmr = row[0]
        elif tms_newintern in row:
            tid_newintern = row[0]
        elif tms_roomA in row:
            tid_roomA = row[0]
        elif "Test ABC1" in row:
            tid_abc1 = row[0]
print "Got tms resource id from exported resource files"
"""get google resources id from exported resources file"""
with open ('resources_google.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if gcal_test1 in row:
            gid_test1 = row[0]
        elif gcal_0_138 in row:
            gid_0_138 = row[0]
        elif gcal_confB in row:
            gid_confB = row[0]
        elif gcal_confA in row:
            gid_confA = row[0]
        elif gcal_qc01 in row:
            gid_qc01 = row[0]
print "Got google resource id from exported resource files"
"""Write tid, gid, and notes for mapping to map file"""
lst = [tid_roomA, gid_confA, notes_match1, \
       tid_newintern, gid_confB, notes_match2, \
       tid_abc1, gid_qc01, notes_match3, \
       tid_webmt, gid_test1, notes_webmt, \
       tid_wcmr, gid_0_138, notes_wcmr]
#Write to list with 3 elements per line
os.chdir(dir_uctms)
map_file = 'resources_map_google.csv'
if os.path.isfile(map_file):
    print "Map file has existed in folder already %s" % dir_uctms
    sys.exit()
with open(map_file, 'w') as f:
    n = m = 0
    while m < len(lst):
        m = m+3
        f.write(",".join(lst[n:m]))
        f.write("\n")
        n = m
print "write google map file to folder %s" % dir_uctms

            
        
    