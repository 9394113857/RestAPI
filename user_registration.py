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


# User_Registration:-
# create in postman by using jsonify:-
@app.route('/registrations/create', methods=['POST'])
def registration():
    if 'regid' in request.json and 'age' in request.json \
            and 'date' in request.json:

        regid = request.json['regid']
        age = request.json['age']
        date = request.json['date']

        # Cursor:-
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_registration WHERE USER_REG_ID = % s', (regid,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        # Checking conditions:-
        elif not re.match(r'^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$', date): # perfect
            msg = 'Invalid date format !'
        elif not regid or not age or not date:
            msg = 'Please fill out the fields !'

        else:
            cursor = mysql.connection.cursor()

            # UserId Pattern:-
            cursor.execute("SELECT USER_ID FROM user_registration")
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
                "insert into user_registration(USER_REG_ID, USER_ID, USER_AGE, USER_IP, USER_DEVICE, USER_DATE_REGISTERED) "
                "VALUES(%s,%s,%s,%s,%s,%s)", (regid, id_value, age, IPAddress, hostname, date))
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