'''
Created on May 9, 2017

@author: qcadmin
'''
import csv

map_file = "C:/TMS_Resources/resources_map_google.csv"
tms_res = "C:/TMS_Resources/resources_tms.csv"
google_res = "C:/TMS_Resources/resources_google.csv"

map_dict = {}
google_res_dict = {}
tms_res_dict = {}

"""read the first line of mapping file"""
def get_tmsid_from_mapping_file():
    with open (map_file, 'r') as f:
        firstline = f.readline()
        tid = firstline.split(",")[0]
        gid = firstline.split(",")[1]
    return (tid, gid)

def create_mapFile_dict():
    reader = csv.reader(open(map_file, 'r'))
    for row in reader:
        k = row[0]
        v = row[1]
        map_dict[k] = v
    
    for tms_id in map_dict:
        google_id = map_dict[tms_id]
#         print tms_id + ' => ' + google_id
#     print ''

def create_tms_dict():
    reader = csv.reader(open(tms_res, 'r'))
    for row in reader:
        k = row[0]
        v = row[1]
        tms_res_dict[k] = v
        
    for tms_id in tms_res_dict:
        tms_name = tms_res_dict[tms_id]
#         print tms_id + ' => ' + tms_name
#     print ''
    
def create_google_dict():
    reader = csv.reader(open(google_res, 'r'))
    for row in reader:
        k = row[0]
        v = row[2]
        google_res_dict[k] = v
        
    for google_id in google_res_dict:
        google_name = google_res_dict[google_id]
#         print google_id + ' => ' + google_name



# create_mapFile_dict()
# create_tms_dict()
# create_google_dict()