'''
Created on Jul 6, 2017

@author: qcadmin
'''
from shutil import copyfile
import os, re, datetime

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

def add_remove_resources_options(opt):
    list = []
    with open (tms_file, 'r') as f:
        for line in f:
            line = line.strip()
            list.append(line)
    if opt == 'remove':
        notes = 'removed from'
        if s_res_opt in list[1] and res_rmv in list[4] and res_add in list[7]:
            print "The following lines are to be removed from the file:\n"
            for x in list[1:10]:
                print x
            print ''
            del list[1:10]
            print "Resources options are removed"
        else:
            print "The contents to be removed are not found"
            return
    elif opt == 'add':
        notes = 'added to'
        if s_res_opt in list[1] and res_rmv in list[4] and res_add in list[7]:
            print "The contents to be added has existed"
            return
        else:
            list.insert(1, text_str_res)
            print "The following lines are to be added into the file:"
            print list[1]
    else:
        print "Given argument is wrong"
             
    with open (tms_file, 'w') as outfile:
        for item in list:
            outfile.write(item.strip() + '\n')
    print "Resources options are %s file" % notes
            
def add_remove_filter_options(opt):
    list = []
    with open (tms_file, 'r') as f:
        for line in f:
            line = line.strip()
            list.append(line)
    
    if opt == 'remove':
        notes = 'removed from'
        if fil_create in list[-7] and fil_update in list[-4]:
            print "The following lines are to be removed from file:\n"
            for item in list[-7:-1]:
                print item
            print ''
            del list[-7:-1]
            print "Filter options are removed"
        else:
            print "The contents to be removed are not found"
            return

    if opt == 'add':
        notes = 'added to'
        if fil_create in list[-7] and fil_update in list[-4]:
            print "The contents to be added has existed"
            return
        else:
            list.insert(-1, text_str_filter)
            print "The following lines are to be added into the file:"
            for x in list[-2:-1]:
                print x
            
    with open (tms_file, 'w') as outfile:
        for item in list:
            outfile.write(item.strip() + '\n')
    print "Resources options are %s file" % notes

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
        if list[index+1] == fil_valid_value:
            print "Filter by %s date has already set to %s" % (type, option)
        else:
            list[index+1] = fil_valid_value
            print "Filter by %s date is changed to tomorrow" % type
    elif option == 'notuse':
        if list[index+1] == fil_invalid_value:
            print "Filter by %s date has already set to %s" % (type, option)
        else:
            list[index+1] = fil_invalid_value
            print "Filter by %s date is changed to '2000-01-01" % type
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

# add_remove_filter_options('add')
# add_remove_filter_options('remove')

# filter_creat_update_value_change('create', 'use')
# filter_creat_update_value_change('create', 'notuse')
# filter_creat_update_value_change('update', 'use')
# filter_creat_update_value_change('update', 'notuse')


# add_remove_resources_options('add')
# add_remove_resources_options('remove')

# allow_resources_add_rmv('special', 'false')
# allow_resources_add_rmv('special', 'true')
# allow_resources_add_rmv('resrmv', 'false')
# allow_resources_add_rmv('resrmv', 'true')
# allow_resources_add_rmv('resadd', 'false')
# allow_resources_add_rmv('resadd', 'true')



        