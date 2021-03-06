#!/usr/bin/python
import MySQLdb
import xml.etree.ElementTree as ET
import subprocess
import os

# connect to the database
db = MySQLdb.connect(host="localhost",
                     user="sympatest",
                     passwd="sympatest",
                     db='test')

# create the cursor
cur = db.cursor()

# iterate through the list of courses
cur.execute("SELECT id,instructor,listCreated FROM courseList")
# numRows = int(cur.rowcount)
# for i in range(0,numRows):
rows = cur.fetchall()
for row in rows:
	# row = cur.fetchone()
	courseID = row[0]
	instructorID = row[1]
	listCreated = row[2]
	# check if list has been created already
	if(not listCreated):
		# open the XML template 
		tree = ET.parse('course_list_a_template.xml')
		root = tree.getroot()

		# fill in the form
		listname = root.find('listname')
		listname.text = courseID
		subject = root.find('subject')
		subject.text = courseID + " Course Announcement List"
		# editor email (select)
		inclTemplate = open('inclTemplate.incl','r')
		inclFile = open("/usr/local/sympa/etc/data_sources/"+courseID+".incl",'w')
		inclFile.write(inclTemplate.read())
		# inclFile.write("sql_query SELECT instructor.email FROM instructor,courseList WHERE instructor.id = %s"%instructorID)
		inclFile.write("sql_query SELECT instructor.email FROM instructor,courseList WHERE instructor.id = courseList.instructor AND courseList.id = '%s'"%courseID)
		inclTemplate.close();
		inclFile.close();
		owner_include = root.find('owner_include')
		owner_source = owner_include.find('source')
		owner_source.text = courseID
		# create that owner_include incl file
		sql = root.find('sql')
		query = sql.find('query')
		query.text = "SELECT student.email FROM `%s`,student WHERE `%s`.sid = student.sid"%(courseID,courseID)
		
		# write the XML file
                tree.write('current.xml')
		# tree.write(courseID+'.xml')

		# create list
		# subprocess.call("/usr/local/sympa/bin/sympa.pl --create_list --input_file /usr/local/sympa/script/current.xml")
		os.system("/usr/local/sympa/bin/sympa.pl --create_list --input_file /usr/local/sympa/script/current.xml")

		# indicate as created
		cur.execute("UPDATE courseList SET listCreated = 1 WHERE id = '%s'"%courseID)
		db.commit()

db.close()
