import socket

import MySQLdb

db = MySQLdb.connect("localhost","root","","clinicalfirst")
cursor = db.cursor()

file = open("F:\Restful-API's\RestAPI\log files\Signup.log", 'r')
line1 = file.readlines(1)
print(line1)

file.close()

# Python Program to Get IP Address and Device Name:-
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

cursor.execute("SELECT USER_ID FROM user_signup")
current_user_id = cursor.rowcount


query = "INSERT INTO api_logs(TRIGGERED_TIME, IP_ADDRESS, USER_DEVICE, USER_ID) VALUES (%s, %s, %s, %s)"

cursor.execute(query, (line1, IPAddr, hostname, current_user_id))

db.commit()
db.close()