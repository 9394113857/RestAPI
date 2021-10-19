# import MySQLdb
#
# serv = MySQLdb.connect(host = "localhost", user = "root", passwd = "raghu")
#
# c = serv.cursor()
#
# print (c.execute("SHOW DATABASES"))

# !/usr/bin/python

import MySQLdb

# Open databasee connection
db = MySQLdb.connect("localhost", "root", "raghu", "password")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print()
print("Database version : %s " % data)

# disconnect from server
db.close()
