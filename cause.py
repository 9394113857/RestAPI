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


# Cause:-
# create in postman by using jsonify:-
@app.route('/cause/create', methods=['POST'])
def cause():
    if 'session_id' in request.json and 'cause_id' in request.json \
            and 'cause_name' in request.json and 'input' in request.json:

        session_id = request.json['session_id']
        cause_id = request.json['cause_id']
        cause_name = request.json['cause_name']
        input = request.json['input']

        # Cursor:-
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM cause WHERE SESSION_ID = % s', (session_id,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        # Checking conditions:-
        elif not session_id or not cause_id or not cause_name or not input:
            msg = 'Please fill out the fields !'

        else:
            cursor = mysql.connection.cursor()

            # UserId Pattern:-
            cursor.execute("SELECT USER_ID FROM cause")
            lastid = cursor.rowcount
            print('----------------------')
            print("Last Id is: " + str(lastid))
            lastid += 1
            pattern = 'US000' # pattern = ooo
            # pattern += 1 # pattern incremnting always by 1:-
            id_value = pattern + str(lastid)
            # User Id pattern Code End #

            # Python Program to Get IP Address and Device Name:-
            hostname = socket.gethostname()
            IPAddress = socket.gethostbyname(hostname)
            #print("Your Computer Name is:" + hostname)
            #print("Your Computer IP Address is:" + IPAddr)

            # Insert Code:-
            cursor.execute(
                "insert into cause(SESSION_ID, USER_ID, CAUSE_ID, CAUSE_NAME, INPUT, USER_IP, USER_DEVICE) "
                "VALUES(%s,%s,%s,%s,%s,%s,%s)", (session_id, id_value, cause_id, cause_name, input, IPAddress, hostname))
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

"""
Commented Code:-
'''
        # These are the conditions:-
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', regid):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', userid):
            msg = 'Username must contain only characters and numbers !'
        elif not re.match(r'^(?:1[01][0-9]|120|1[7-9]|[2-9][0-9])$', userage):   # userage code saved
            # "^(?:1[01][0-9]|120|1[7-9]|[2-9][0-9])$"gm
            msg = 'Age must contain number between 17 to 120 !'
        '''
"""