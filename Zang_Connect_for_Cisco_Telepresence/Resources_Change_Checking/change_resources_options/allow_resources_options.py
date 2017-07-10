'''
Created on Jul 6, 2017

@author: qcadmin
'''
from shutil import copyfile
import os, re

os.chdir("C:\UC\UCTMS")
tms_file = "tms.config"
tms_back_file = 'tms_backup.config'
opt_true = "<value>True</value>"
opt_false = "<value>False</value>"
s_res_opt = "AllowSpecialResourcesRemoval"
res_rmv = "AllowResourcesRemoval"
res_add = "AllowResourcesCreation"
index = ''
text_str = """
<setting name="AllowSpecialResourcesRemoval" serializeAs="String">
<value>True</value>
</setting>
<setting name="AllowResourcesRemoval" serializeAs="String">
<value>True</value>
</setting>
<setting name="AllowResourcesCreation" serializeAs="String">
<value>True</value>
</setting>
"""
search = "<setting name"
indent_tag = "  <setting name"

def backup_tmsconfig_file():
    copyfile(tms_file, tms_back_file)
    print "tms.config is copied to backup file"

def add_remove_resources_options(opt):
    list = []
    with open (tms_file, 'r') as f:
        for line in f:
            line = line.strip()
            list.append(line)
    
    if opt == 'remove':
        if s_res_opt in list[1] and res_rmv in list[4] and res_add in list[7]:
            del list[1:10]
            print "Resources options are removed"
        else:
            print "The contents to be removed are not found"
            return

    if opt == 'add':
        if s_res_opt in list[1] and res_rmv in list[4] and res_add in list[7]:
            print "The contents to be added has existed"
            return
        else:
            list.insert(1, text_str)
            print "Resources options are added"
     
    with open (tms_file, 'w') as outfile:
        for item in list:
            outfile.write(item.strip() + '\n')

def allow_resources_add_rmv(type, option):
    """Write the tms.config to a list"""
    list = []
    with open (tms_file, 'r') as f:
        for line in f:
            line = line.strip()
            list.append(line)
            
    """Find out required line and change option"""
    for line in list:
        if type == 'special':
            if s_res_opt in line:
                index = list.index(line)
        elif type == 'resrmv':
            if res_rmv in line:
                index = list.index(line)
        elif type == 'resadd':
            if res_add in line:
                index = list.index(line)
        else:
            print "Wrong argument given"
    if option == 'true':
        list[index+1] = opt_true
        print "Option for allow special resources removal is changed to 'Ture'"
    elif option == 'false':
        list[index+1] = opt_false
        print "Option for allow special resources removal is changed to 'False'"
    else:
        print "Wrong argument given"
    print ''
    print "The option in tms.config is displayed as:"
    print list[index]
    print list[index+1]
    print list[index+2]
    print ''
    """Write the list back to file"""
    with open (tms_file, 'w') as outfile:
        for item in list:
            outfile.write(item + '\n')


# add_remove_resources_options('add')

# allow_resources_add_rmv('special', 'false')
# allow_resources_add_rmv('resrmv', 'false')
# allow_resources_add_rmv('resadd', 'false')

# add_remove_resources_options('remove')
        