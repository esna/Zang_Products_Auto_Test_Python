'''
Created on Jul 7, 2017

@author: qcadmin
'''
import allow_resources_options
import os
tms_backup_file = 'tms_backup.config'

os.chdir("C:\UC\UCTMS")
if os.path.isfile(tms_backup_file):
    print "tms.config file has been backuped"
else:
    allow_resources_options.backup_tmsconfig_file()
allow_resources_options.add_remove_resources_options('add')
print "Test ends"