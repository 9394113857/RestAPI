# 1.This framework is for throwing Errors of Fields:-
# 2.Flask framework and Mysql Database:-
import re
# 3. Get ip and device name from socket library:-
import socket

from flask import request, jsonify, Flask, logging
from flask_mysqldb import MySQL

# 3.validation framework:-

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'raghu'
app.config['MYSQL_DB'] = 'clinicalfirst'

mysql = MySQL(app)


# User_Department:-
# create in postman by using jsonify:-
@app.route('/departments/create', methods=['POST'])
def departments():
    if 'id' in request.json and 'userid' in request.json \
            and 'deptid' in request.json and 'deptname' in request.json:

        id = request.json['id']
        userid = request.json['userid']
        deptid = request.json['deptid']
        deptname = request.json['deptname']

        # Cursor:-
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_department WHERE USER_ID = % s', (userid,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[A-Za-z0-9]+', deptname):
            msg = 'Department Name must contain only characters and numbers !'
        elif not id or not userid or not deptid or deptname:
            msg = 'Please fill out the fields !'

        else:
            cursor = mysql.connection.cursor()
            '''
            # UserId Pattern:-
            cursor.execute("SELECT USER_ID FROM user_department")
            lastid = cursor.rowcount
            print('----------------------')
            print("Last Id is: " + str(lastid))
            lastid += 1
            pattern = 'US000' # pattern = ooo
            # pattern += 1 # pattern incrementing always by 1:-
            id_value = pattern + str(lastid)
            # User Id pattern Code End #
            '''
            # Python Program to Get IP Address and Device Name:-
            hostname = socket.gethostname()
            IPAddress = socket.gethostbyname(hostname)

            #print("Your Computer Name is:" + hostname)
            #print("Your Computer IP Address is:" + IPAddr)

            # Insert Code:-
            cursor.execute(
                "insert into user_department(ID, USER_ID, DEPT_ID, DEPT_NAME, USER_IP, USER_DEVICE,) "
                "VALUES(%s, %s, %s, %s, %s, %s)", (id, userid, deptid, deptname, IPAddress, hostname))
            mysql.connection.commit()
            # details = cur.fetchall()
           # logging.info("successfully registred")
            return "successfully inserted", 200
        return msg
    return "invalid parameters"


# MAIN app:-
if __name__ == "__main__":
    app.run(debug=True)

################################################ END CODE ##############################################################

