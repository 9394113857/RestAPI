# 1.This framework is for throwing Errors of Fields:-
# 2.Flask framework and Mysql Database:-
# importing module
import logging
import re
# 3. Get ip and device name from socket library:-
import socket

from flask import request, Blueprint

from database import mysql

# Create and configure logger
logging.basicConfig(filename="F:\Restful-API's\RestAPI\log files\Registration.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

# Creating an object:-
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG:-
logger.setLevel(logging.DEBUG)

# Test messages
logger.info('-----------------------------')
logger.info("User_Registration script started Now:-")
logger.info('-----------------------------')
"""
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
"""

# Blueprint Setup:-
registration = Blueprint('registration', __name__)


# User_Registration:-
# create in postman by using jsonify:-
@registration.route('/registration/create', methods=['POST'])
def registration():
    if 'reg_id' in request.json and 'user_age' in request.json \
            and 'user_experience' in request.json and 'user_gender' in request.json \
            and 'user_license_number' in request.json and 'flat_no' in request.json \
            and 'street_name' in request.json and 'city_name' in request.json \
            and 'state_name' in request.json and 'country_name' in request.json \
            and 'zip_code' in request.json and 'user_approved' in request.json \
            and 'date' in request.json:

        reg_id = request.json['reg_id']
        user_age = request.json['user_age']
        user_experience = request.json['user_experience']
        user_gender = request.json['user_gender']
        user_license_number = request.json['user_license_number']
        flat_no = request.json['flat_no']
        street_name = request.json['street_name']
        city_name = request.json['city_name']
        state_name = request.json['state_name']
        country_name = request.json['country_name']
        zip_code = request.json['zip_code']
        user_approved = request.json['user_approved']
        date = request.json['date']

        # Cursor:-
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_registration WHERE USER_REG_ID = % s', (reg_id,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        # Checking conditions:-
        elif not re.match(r'^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$', date):  # perfect
            msg = 'Invalid date format !'
        elif not reg_id or not user_age or not user_experience or not user_gender \
                or not user_license_number or not flat_no or not street_name or not city_name \
                or not state_name or not country_name or not zip_code or not user_approved or not date:
            msg = 'Please fill out the fields !'

        else:
            cursor = mysql.connection.cursor()

            # UserId Pattern:-
            cursor.execute("SELECT USER_ID FROM user_registration")
            lastid = cursor.rowcount
            print('----------------------')
            print("Last Id is: " + str(lastid))
            lastid += 1
            pattern = 'US000'  # pattern = ooo
            # pattern += 1 # pattern incremnting always by 1:-
            user_id = pattern + str(lastid)
            # User Id pattern Code End #

            # Python Program to Get IP Address and Device Name:-
            hostname = socket.gethostname()
            IPAddress = socket.gethostbyname(hostname)
            # print("Your Computer Name is:" + hostname)
            # print("Your Computer IP Address is:" + IPAddr)

            # Insert Code:-
            cursor.execute(
                "insert into user_registration(USER_REG_ID, USER_ID, USER_AGE, USER_EXPERIANCE, USER_GENDER, USER_LICENSE_NUMBER, FLAT_NO, STREET_NAME, CITY_NAME, STATE_NAME, COUNTRY_NAME, ZIP_CODE, USER_APPROVED, USER_IP, USER_DATE_REGISTERED) "
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    reg_id, user_id, user_age, user_experience, user_gender, user_license_number, flat_no, street_name,
                    city_name, state_name, country_name, zip_code, user_approved, IPAddress, date))
            mysql.connection.commit()
            # details = cur.fetchall()
            logger.info("successfully registred")
            return "successfully inserted", 200
        return msg
    return "invalid parameters"


################################################ END CODE ##############################################################

# Post Man:-
"""
Working URL Now:-
POST:- // Inserting Values change reg_id every time.
http://127.0.0.1:5000/registrations/create 
Body---> Raw----> json
{
    "reg_id"                :  1,
    "user_age"              :  29,
    "user_experience"       :  3.10,
    "user_gender"           :  "MALE",
    "user_license_number"   :  "INS-1992",
    "flat_no"               :  "5-7-33",
    "street_name"           :  "Sangeeth Nagar",
    "city_name"             :  "HYD",
    "state_name"            :  "TS",
    "country_name"          :  "IND",
    "zip_code"              :  500072,
    "user_approved"         :  "2021-06-06",
    "date"                  :  "2021-06-06"
}
"""

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
