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


# User_Specialization:-
# create in postman by using jsonify:-
@app.route('/specializations/create', methods=['POST'])
def specialization():
    if 'spl_id' in request.json and 'spl_name' in request.json:

        spl_id = request.json['spl_id']
        spl_name = request.json['spl_name']

        # Cursor:-
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_specialization WHERE USER_SPECIALIZATION_ID = % s', (spl_id,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[A-Za-z0-9]+', spl_name): # Perfect
            msg = 'Specialization Name must contain only characters and numbers !'
        elif not spl_id or not  spl_name:
            msg = 'Please fill out the fields !'

        else:
            cursor = mysql.connection.cursor()

            # UserId Pattern:-
            cursor.execute("SELECT USER_ID FROM user_specialization")
            lastid = cursor.rowcount
            print('----------------------')
            print("Last Id is: " + str(lastid))
            lastid += 1
            pattern = 'US000' # pattern = ooo
            # add_value = 00
            # pattern += 1 # pattern incremnting always by 1:-
            user_id = pattern + str(lastid)
            # User Id pattern Code End #

            # Python Program to Get IP Address and Device Name:-
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            #print("Your Computer Name is:" + hostname)
            #print("Your Computer IP Address is:" + IPAddr)

            # Insert Code:-
            cursor.execute(
                "insert into user_specialization(USER_SPECIALIZATION_ID, USER_ID, SPECIALIZATION_NAME, USER_IP, USER_DEVICE) VALUES(%s,%s,%s,%s,%s)",
                (spl_id, user_id, spl_name, IPAddr, hostname))
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

        # Conditions:-
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', splid):
            msg = 'Invalid email address !'


"""