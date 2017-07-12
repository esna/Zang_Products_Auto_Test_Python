'''
Created on Jul 5, 2017

@author: qcadmin
'''
gcal_file = "C:/TMS_Resources/resources_google.csv"
res_1 = "TMSUCREID - Test ABC5"
res_2 = "TMSUCREID - Test ABC6"
res_3 = "TMSUCREID - WebEx meeting"
res_4 = "TMSUCREID - WebEx CMR"

with open (gcal_file, 'r') as f:
    for line in f:
        for res in (res_1, res_2, res_3, res_4):
            if res in line:
                print "%s is found" % res
    print "Test ends"
