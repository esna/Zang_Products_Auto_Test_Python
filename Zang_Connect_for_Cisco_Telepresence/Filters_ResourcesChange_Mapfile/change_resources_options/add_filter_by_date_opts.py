'''
Created on Jul 12, 2017

@author: qcadmin
'''
import os
import allow_resources_options
tms_backup_file = 'tms_backup.config'

os.chdir("C:\UC\UCTMS")
if os.path.isfile(tms_backup_file):
    print "tms.config file has been backuped"
else:
    allow_resources_options.backup_tmsconfig_file()
allow_resources_options.add_remove_filter_options('add')
print "Test ends"