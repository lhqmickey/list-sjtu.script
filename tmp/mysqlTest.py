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

# iterate through the list of courses
cur.execute("SELECT id,instructor,listCreated FROM courseList")
# for i in range(0,numRows):
rows = cur.fetchall()
for row in rows:
	print row
db.close()
