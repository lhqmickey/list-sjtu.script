#!/usr/bin/python
# open the XML template 
import xml.etree.ElementTree as ET

courseID = "123"
tree = ET.parse('courseListTemplate.xml')
root = tree.getroot()
# fill in the form
listname = root.find('listname')
listname.text = courseID
sql = root.find('sql')
query = sql.find('query')
query.text = "SELECT email FROM %s"%(courseID)

# write the XML file
tree.write('current.xml')
