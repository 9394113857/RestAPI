import hashlib
# importing module:-
import logging
import random
import re
import smtplib
# 3. Get ip and device name from socket library:-
import socket
# 1.This framework is for throwing Errors of Fields:-
# 2.Flask framework and Mysql Database:-
from pipes import quote

import MySQLdb
import jwt
import mysql
from flask import request, Blueprint, app
from werkzeug.security import generate_password_hash

# Checking Valid Phone Number:-
# import phonenumbers
# from phonenumbers import carrier, timezone, geocoder, data

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

""" 
All logger Messages:-
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
"""

# Flask App Initialization:-
user = Blueprint("user", __name__)

# User_Signup:-
# create in postman by using jsonify:-
@user.route('/insert', methods=['POST'])
@user.route('/', methods=['POST'])
def register():
    if 'username' in request.json and 'mail_id' in request.json \
            and 'user_phone_number' in request.json and 'user_password' and 'date' in request.json:

        # signup_id = request.json['signup_id']
        username = request.json['username']
        mail_id = request.json['mail_id']
        user_phone_number = request.json['user_phone_number']
        user_password = request.json['user_password']
        hashed_password = generate_password_hash(user_password)
        date = request.json['date']

        # Cursor Initialization:-
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
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
        elif not re.match(r'^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$', date):
            msg = 'Invalid date format !'
        elif not username or not mail_id or not user_phone_number or not user_password or not date:
            msg = 'Please fill out the fields !'
        else:
            cursor = mysql.connection.cursor()
            """
            # Check Phone Number Service:-
            INDIA_CODE = "+91"
            Phone_Number = user_phone_number  # 5394112233 It's False, Try this
            my_number = phonenumbers.parse(INDIA_CODE + str(Phone_Number), "IN")
            # Getting Values from the Service:-
            print("===============================================")
            num = phonenumbers.is_valid_number(my_number)
            print("1.Checking Given Number is Active or Not:", num)

            if(num!=False):
                return 'Not in Service !!!'
            else:
            """
            # UserId Pattern for Insert Operation:-
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
                "insert into user_signup(USER_ID, USER_NAME, USER_MAIL_ID, USER_PHONE_NUMBER, USER_PASSWORD, USER_IP, USER_DEVICE, USER_DATE_CREATED) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                (user_id, username, mail_id, user_phone_number, hashed_password, IPAddr, hostname, date))
            mysql.connection.commit()

            # Current Inserted USER_ID:-
            cursor.execute("SELECT USER_ID FROM user_signup")
            current_user_id = cursor.rowcount
            print('----------------------------------')
            print("Current Inserted ID is: " + str(current_user_id))
            print('----------------------------------')
            """
            current_user_name = ("SELECT USER_NAME FROM user_signup")
            print('----------------------------------')
            print("Current Inserted User Name is: " + str(current_user_name))
            print('----------------------------------')
            """
            # cursor.close()
            # details = cur.fetchall()
            logger.info("Successfully Registred with Id: %s", current_user_id)
            # logger.info("Successfully Registred with User Name: %s", current_user_name)
            return "successfully inserted", 200
        return msg
    return "invalid parameters"


# Login:-
# @app.route('/login', methods=["POST"])
# def login():
#     if 'mail_id' in request.json and 'password' in request.json:
#         mail_id = request.json['mail_id']
#         password = request.json["password"]
#         cur = mysql.connection.cursor()
#         cur.execute("select * from user_signup WHERE (USER_MAIL_ID = %s)", (mail_id,))
#         details = cur.fetchone()
#         if details is None:
#             return ({"Error": "No details"}), 401
#         # here 2 is the index num
#         hashed_password = details[4]
#         password_match = check_password_hash(hashed_password, password)
#         if password_match:
#             # generate the JWT Token
#             token = jwt.encode({
#                 'user_mail': mail_id,
#                 'exp': datetime.utcnow() + timedelta(minutes=2)},
#                 app.config['SECRET_KEY'], algorithm='HS256')
#
#             return token
#         else:
#             return ({"Error": "invalid credentials"}), 401
#     return "Insufficient parameters", 400
#
#
# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None
#         if "x-access-token" in request.headers:
#             token = request.headers["x-access-token"]
#         if not token:
#             return jsonify({"message": "Token is missing !!"}), 401
#         try:
#             data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
#             current_user = data['user_mail']
#
#         except:
#             return jsonify({"message": "Token is invalid"})
#
#         return f(current_user, *args, **kwargs)
#
#     return decorated
#
#
# @app.route('/user/validate', methods=["GET"])
# @token_required
# def tokenTesting(user):
#     return user


##############################################################################
# Forgot Password Token Genaration:-
@user.route('/forgot_pass', methods=['POST'])
def reset():
    if request.method == 'POST' and (request.json or request.form):
        user_mail_id = None
        user_mail_id = request.json['user_mail_id']
        cur = mysql.connection.cursor()
        cur.execute("select * from user_signup where USER_MAIL_ID=%s", (user_mail_id,))
        account = cur.fetchone()
        if account is None:
            return "invalid details"
        else:
            token = jwt.encode({'email': user_mail_id}, app.config["SECRET_KEY"], algorithm='HS256')
            lin = quote(token)
            otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
            print(otp)
            body = '\n\n' + '\n your reset password link: ' + (
                'http://127.0.0.1:5000/forgot_pass') + '\n' + "http://127.0.0.1:5000/reset_pass"
            try:
                smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            except Exception as e:
                print(e)
                smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)

            smtpObj.receiver = user_mail_id

            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login('ur mail', "ur password from web")
            smtpObj.sendmail('ur mail', smtpObj.receiver, body)

            smtpObj.quit()
            pass
            return "reset link sent to your mail"

    return "invalid"


# Confirm Password with Generated Token:-
@user.route('/reset_pass', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and (request.json or request.form):
        user_mail_id = request.json['user_mail_id']
        user_password = request.json['user_password']
        user_confirm_password = request.json['user_confirm_password']
        if user_password == user_confirm_password:
            updated_pass = user_confirm_password
            h = hashlib.md5(updated_pass.encode())
            cur = mysql.connection.cursor()
            cur.execute("update user_signup set USER_PASSWORD=%s where USER_MAIL_ID=%s", (h.hexdigest(), user_mail_id))
            mysql.connection.commit()
            cur.close()
            return "success"


################################################ END CODE ##############################################################

# Post Man:-
"""
Working URL Now:-
POST:- Inserting Values change username, mail_id and user_phone_number every time.
http://127.0.0.1:5000/user/insert 
Body---> Raw----> json
{     
    "username"          :  "Raghu1",
    "mail_id"           :  "raghunadh1@gmail.com",
    "user_phone_number" :  "9394113851",
    "user_password"     :  "raghu@123",
    "date"              :  "2021-06-08"
}
"""
