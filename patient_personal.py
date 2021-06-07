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
logging.basicConfig(filename="F:\Restful-API's\RestAPI\log files\patient_personal.log",
					format='%(asctime)s %(message)s',
					filemode='a')

#Creating an object
logger=logging.getLogger()

#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

#Test messages
logger.info('-----------------------------')
logger.info("Patient_Personal script started Now:-")
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


# patient_personal:-
# create in postman by using jsonify:-
@app.route('/patient_personal/create', methods=['POST'])
def patient_personal():
    if 'patient_id' in request.json and 'patient_name' in request.json \
            and 'phone' in request.json and 'mail_id' in request.json\
            and 'flat_no' in request.json and 'street_name' in request.json\
            and 'city_name' in request.json and 'state_name' in request.json\
            and 'country_name' in request.json and 'zip_code' in request.json\
            and 'date_of_birth' in request.json and 'created_by' in request.json\
            and 'date':

        patient_id = request.json['patient_id']
        patient_name = request.json['patient_name']
        phone = request.json['phone']
        mail_id = request.json['mail_id']
        flat_no = request.json['flat_no']
        street_name = request.json['street_name']
        city_name = request.json['city_name']
        state_name = request.json['state_name']
        country_name = request.json['country_name']
        zip_code = request.json['zip_code']
        date_of_birth = request.json['date_of_birth']
        created_by = request.json['created_by']
        date = request.json['date']

        # Cursor:-
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM patient_personal WHERE PATIENT_ID = % s', (patient_id,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        # Checking conditions:-
        elif not patient_id or not patient_name or not phone or not mail_id\
                or not flat_no or not street_name or not city_name or not state_name\
                or not country_name or not zip_code or not date_of_birth or not created_by\
                or not date:
            msg = 'Please fill out the fields !'

        else:
            cursor = mysql.connection.cursor()

            # UserId Pattern:-
            cursor.execute("SELECT USER_ID FROM patient_personal")
            lastid = cursor.rowcount
            print('----------------------')
            print("Last Id is: " + str(lastid))
            lastid += 1
            pattern = 'US000' # pattern = ooo
            # pattern += 1 # pattern incremnting always by 1:-
            user_id = pattern + str(lastid)
            # User Id pattern Code End #

            # Python Program to Get IP Address and Device Name:-
            hostname = socket.gethostname()
            IPAddress = socket.gethostbyname(hostname)
            #print("Your Computer Name is:" + hostname)
            #print("Your Computer IP Address is:" + IPAddr)

            # Insert Code:-
            cursor.execute(
                "insert into patient_personal(PATIENT_ID, USER_ID, PATIENT_NAME, PHONE_NUMBER, MAIL_ID, FLAT_NO, STREET_NAME, CITY_NAME, STATE_NAME, COUNTRY_NAME, ZIP_CODE, DATE_OF_BIRTH, CREATED_BY, IP_ADDRESS, USER_DEVICE, CREATED_DATE) "
                "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (patient_id, user_id, patient_name, phone, mail_id, flat_no, street_name, city_name, state_name, country_name, zip_code, date_of_birth, created_by, IPAddress, hostname, date))
            mysql.connection.commit()
            # details = cur.fetchall()
            logger.info("successfully registred")
            return "successfully inserted", 200
        return msg
    return "invalid parameters"


# MAIN app:-
if __name__ == "__main__":
    app.run(debug=True)

################################################ END CODE ##############################################################

# Post Man:-
"""
Working URL Now:-
POST:- Inserting Values change patient_id and phone, mail_id every time they are unique.
http://127.0.0.1:5000/patient_personal/create 
Body---> Raw----> json
{
    "patient_id"        :  1,
    "patient_name"      :  "Raghu",
    "phone"             :  "9394113857",
    "mail_id"           :  "raghunadh2@gmail.com",
    "flat_no"           :  "5-7-33",
    "street_name"       :  "Sangeeth Nagar",    
    "city_name"         :  "HYD",
    "state_name"        :  "TS",
    "country_name"      :  "IND",
    "zip_code"          :  500072,
    "date_of_birth"     :  "1992-04-14",
    "created_by"        :  "Raghu",
    "date"              :  "2021-06-06"   
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