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
		print 'Hi'
		# indicate as created
		cur.execute("UPDATE courseList SET listCreated = 1 WHERE id = 'ee101-1'")
		db.commit();

db.close()
