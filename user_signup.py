# 1.This framework is for throwing Errors of Fields:-
# 2.Flask framework and Mysql Database:-
import re
# 3. Get ip and device name from socket library:-
import socket

from flask import request, jsonify, Flask, logging
from flask_mysqldb import MySQL

#importing module
import logging

#Create and configure logger
logging.basicConfig(filename="F:\Restful-API's\RestAPI\log files\Signup.log",
					format='%(asctime)s %(message)s',
					filemode='a')

#Creating an object
logger=logging.getLogger()

#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

#Test messages
logger.info('-----------------------------')
logger.info("User_Signup script started Now:-")
"""
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
"""



# Flask App Initialization:-
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'raghu'
app.config['MYSQL_DB'] = 'clinicalfirst'

mysql = MySQL(app)

# User_Signup:-
# create in postman by using jsonify:-
@app.route('/users/create', methods=['POST'])
def register():
    if 'signup_id' in request.json and 'username' in request.json and 'mail_id' in request.json\
            and 'user_phone_number' in request.json and 'user_password' and 'date' in request.json:

        signup_id = request.json['signup_id']
        username = request.json['username']
        mail_id = request.json['mail_id']
        user_phone_number = request.json['user_phone_number']
        user_password = request.json['user_password']
        date = request.json['date']

        # Cursor:-
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_signup WHERE USER_SIGNUP_ID = % s', (signup_id,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', mail_id):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not re.match(r'^[A-Za-z0-9@#$%^&+=]{8,32}', user_password):
            msg = 'Password must contain alphanumber with specialcharacters !'
        elif not re.match(r'^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$', user_phone_number):
            msg = 'Invalid phone number and starts with +91 !'
        elif not re.match(r'^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$', date):
            msg = 'Invalid date format !'
        elif not signup_id or not username or not mail_id or not user_phone_number or not user_password or not date:
            msg = 'Please fill out the fields !'

        else:
            cursor = mysql.connection.cursor()

            # UserId Pattern for Insert Operation:-
            cursor.execute("SELECT USER_ID FROM user_signup")
            last_user_id = cursor.rowcount
            print('----------------------------------')
            print("Last Inserted ID is: " + str(last_user_id))
            pattern = 'US000' # pattern = ooo
            last_user_id += 1
            # add_value = 00
            # pattern += 1 # pattern incremnting always by 1:-
            user_id = pattern + str(last_user_id) # pass 'user_id' value in place holder exactly
            # User Id pattern Code End #

            # Python Program to Get IP Address and Device Name:-
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            #print("Your Computer Name is:" + hostname)
            #print("Your Computer IP Address is:" + IPAddr)

            # Inserting Values via placeholders like '%s' using exceute() of cursor object:-
            cursor.execute(
                "insert into user_signup(USER_SIGNUP_ID, USER_ID, USER_NAME, USER_MAIL_ID, USER_PHONE_NUMBER, USER_PASSWORD, USER_IP, USER_DEVICE, USER_DATE_CREATED) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (signup_id, user_id, username, mail_id, user_phone_number, user_password, IPAddr, hostname, date))
            mysql.connection.commit()
            # Current Inserted USER_ID:-
            cursor.execute("SELECT USER_ID FROM user_signup")
            current_user_id = cursor.rowcount
            print('----------------------------------')
            print("Current Inserted ID is: " + str(current_user_id))
            print('----------------------------------')
            # details = cur.fetchall()
            logger.info("successfully registred")
            return "successfully inserted", 200
        return msg
    return "invalid parameters"


# MAIN app:-
if __name__ == "__main__":
    app.run(debug=True)

# When you deploy before to the server:-
# Note:-     app.run(debug=False)
# Make debug value False and deploy the code.

################################################ END CODE ##############################################################


# Post Man:-
"""
Working URL Now:-
POST:-
http://127.0.0.1:5000/users/create 
Body---> Raw----> json
{
    "signup_id" :          2 ,
    "username" :           "Raghu",
    "mail_id" :            "raghunadh2@gmail.com",
    "user_phone_number" :  "9394113852",
    "user_password" :      "raghu123",
    "date" :               "2021-06-06"
}
"""