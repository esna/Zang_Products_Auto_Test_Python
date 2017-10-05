'''
Created on Jul 6, 2017

@author: qcadmin
'''
from shutil import copyfile
import os, re
import datetime

os.chdir("C:\UC\UCTMS")
tms_file = "tms.config"
tms_back_file = 'tms_backup.config'
opt_true = "<value>True</value>"
opt_false = "<value>False</value>"
s_res_opt = "AllowSpecialResourcesRemoval"
res_rmv = "AllowResourcesRemoval"
res_add = "AllowResourcesCreation"
fil_create = "FilterByCreateDate"
fil_update = "FilterByUpdateDate"
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
fil_valid_value = "<value>%s</value>" % tomorrow
fil_invalid_value = "<value>2000-01-01</value>"
index = ''

text_str_res = """
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
text_str_filter = """
<setting name="FilterByCreateDate" serializeAs="String">
<value>2000-01-01</value>
</setting>
<setting name="FilterByUpdateDate" serializeAs="String">
<value>2000-01-01</value>
</setting>
"""
search = "<setting name"
indent_tag = "  <setting name"

def backup_tmsconfig_file():
    copyfile(tms_file, tms_back_file)
    print "tms.config is copied to backup file"

def filter_creat_update_value_change(type, option):
    """Write the tms.config to a list"""
    list = []
    with open (tms_file, 'r') as f:
        for line in f:
            line = line.strip()
            list.append(line)
    """Find out required line and change option"""
    for line in list:
        if type == 'create':
            if fil_create in line:
                index = list.index(line)
        elif type == 'update':
            if fil_update in line:
                index = list.index(line)
        else:
            print "Wrong argument given"
    if option == 'use':
        list[index+1] = fil_valid_value
        print "Option for filter by create date is changed to tomorrow"
    elif option == 'notuse':
        list[index+1] = fil_invalid_value
        print "Option for filter by create date is changed to '2000-01-01"
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

# filter_creat_update_value_change('create', 'use')
# filter_creat_update_value_change('create', 'notuse')
# filter_creat_update_value_change('update', 'use')
# filter_creat_update_value_change('update', 'notuse')
        