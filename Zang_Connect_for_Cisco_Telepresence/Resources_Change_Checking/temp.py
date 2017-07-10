'''
Created on Jul 7, 2017

@author: qcadmin
'''


filename = 'test'
list = []

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

list = []
    with open (tms_file, 'r') as f:
        for line in f:
            line = line.strip()
            list.append(line)

for item in list:
    print item