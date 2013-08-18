#!/usr/bin/python
import MySQLdb
import xml.etree.ElementTree as ET

# connect to the database
db = MySQLdb.connect(host="localhost",
                     user="sympatest",
                     passwd="sympatest",
                     db='test')

# create the cursor
cur = db.cursor()
cur

# iterate through the list of courses
cur.execute("SELECT id,teacher,listCreated FROM courseList")
# numRows = int(cur.rowcount)
# for i in range(0,numRows):
rows = cur.fetchall()
for row in rows
	# row = cur.fetchone()
	courseID = row[0]
	teacherID = row[1]
	listCreated = row[2]
	# check if list has been created already
	if(not listCreated)
		# open the XML template 
		tree = ET.parse('courseListTemplate.xml')
		root = tree.getroot()

		# fill in the form
		listname = root.find('listname')
		listname.text = courseID
		# editor_include = root.find('editor_include')
		# editor_source = editor_include.find('source')
		# editor_source = "/home/sympa/incl/%s"%(courseID)
		# editor email (select)
		# listOwner
		# listModerator - teacher
		sql = root.find('sql')
		query = sql.find('query')
		query.text = "SELECT student.email FROM `%s`,student WHERE `%s`.sid = student.sid"%(courseID,courseID)
		
		# write the XML file
                tree.write('current.xml')

		# create list
		# subprocess.call("/usr/local/sympa/bin/sympa.pl --create_list --input_file /home/sympa/current.xml")

		# indicate as created
		cur.execute("UPDATE courseList SET listCreated = 'true' WHERE id = %s",(courseID))

