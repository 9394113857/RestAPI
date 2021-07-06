import re
import socket
import logging
import MySQLdb
from faker import Faker
from flask import Blueprint, request, jsonify, Flask
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash

# Create and configure logger:-
logging.basicConfig(filename="F:\Restful-API's\RestAPI\log files\Signup.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

# Creating an object:-
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG:-
logger.setLevel(logging.DEBUG)

# Test messages:-
logger.info('-----------------------------')
logger.info("User_Signup script started Now:-")
logger.info('-----------------------------')


# blueprint setup
user = Blueprint("user", __name__)

app = Flask(__name__)
mysql = MySQL(app)

# User_Signup:-
# create in postman by using jsonify:-
@user.route('/insert', methods=['POST'])
def register():
    if 'username' in request.json and 'mail_id' in request.json \
            and 'user_phone_number' in request.json and 'user_password' in request.json:

        username = request.json['username']
        mail_id = request.json['mail_id']
        user_phone_number = request.json['user_phone_number']
        user_password = request.json['user_password']
        hashed_password = generate_password_hash(user_password)

        # Open databasee connection:-
        mysql = MySQLdb.connect("localhost", "root", "", "clinicalfirst")

        # Cursor Initialization:-
        cursor = mysql.cursor()
        cursor.execute('SELECT * FROM user_signup WHERE USER_NAME = % s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
            logger.info("User already exists: %s", username)

        elif not re.match(r'[^@]+@[^@]+\.[^@]+', mail_id):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not re.match(r'^[A-Za-z0-9@#$%^&+=]{8,32}', user_password):
            msg = 'Password must contain alphanumber with specialcharacters !'
        elif not re.match(r'^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[6789]\d{9}|(\d[ -]?){10}\d$',
                          user_phone_number):
            msg = 'Invalid phone number and starts with +91 !'
        # elif not re.match(r'^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$', date):
        #     msg = 'Invalid date format !'
        elif not username or not mail_id or not user_phone_number or not user_password:
            msg = 'Please fill out the fields !'
        else:
            # UserId Pattern for Insert Operation:-
            cursor = mysql.cursor()
            cursor.execute("SELECT USER_ID FROM user_signup")
            last_user_id = cursor.rowcount
            print('----------------------------------')
            print("Last Inserted ID is: " + str(last_user_id))
            pattern = 'US000'  # pattern = ooo
            last_user_id += 1
            # add_value = 00
            # pattern += 1 # pattern incremnting always by 1:-
            user_id = pattern + str(last_user_id)  # pass 'user_id' value in place holder exactly
            # User Id pattern Code End #

            # Python Program to Get IP Address and Device Name:-
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            # print("Your Computer Name is:" + hostname)
            # print("Your Computer IP Address is:" + IPAddr)

            # Execute cursor now:-
            cursor.execute(
                "insert into user_signup(USER_ID, USER_NAME, USER_MAIL_ID, USER_PHONE_NUMBER, USER_PASSWORD, USER_IP, USER_DEVICE) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                (user_id, username, mail_id, user_phone_number, hashed_password, IPAddr, hostname))
            mysql.commit()

            # Current Inserted USER_ID:-
            cursor.execute("SELECT USER_ID FROM user_signup")
            current_user_id = cursor.rowcount
            print('----------------------------------')
            print("Current Inserted ID is: " + str(current_user_id))
            print('----------------------------------')
            logger.info("Successfully Registred with Id: %s", current_user_id)
            return "successfully inserted", 200
        return msg
    return "invalid parameters"

# Post Man:-
"""

POST:- Inserting Values change username, mail_id and user_phone_number every time.
http://127.0.0.1:5000/user/insert 
Body---> Raw----> json
{     
    "username"          :  "Raghu1",
    "mail_id"           :  "raghunadh28@gmail.com",
    "user_phone_number" :  "9394113857",
    "user_password"     :  "raghu@123"        
}

# "date"              :  "2021-06-03"
"""
