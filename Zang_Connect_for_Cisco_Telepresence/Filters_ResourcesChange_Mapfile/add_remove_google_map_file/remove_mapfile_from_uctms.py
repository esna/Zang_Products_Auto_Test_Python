'''
Created on Jul 10, 2017

@author: qcadmin
'''
import os, sys
dir_name = "C:\UC\UCTMS"
os.chdir(dir_name)

map_file = "resources_map_google.csv"
if os.path.isfile(map_file):
    os.remove(map_file)
    print "%s is removed from %s" % (map_file, dir_name)
else:
    print "Map file is not found in folder %s" % dir_name
    sys.exit()