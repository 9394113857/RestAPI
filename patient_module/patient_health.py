# 1.This framework is for throwing Errors of Fields:-
# 2.Flask framework and Mysql Database:-
# 3. Get ip and device name from socket library:-
# importing module
import logging
import socket

from flask import request, Flask, Blueprint
from flask_mysqldb import MySQL

# Create and configure logger
logging.basicConfig(filename="F:\Restful-API's\RestAPI\log files\patient_health.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages
logger.info('-----------------------------')
logger.info("Patient_Health script started Now:-")
"""
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
"""

# blueprint setup
patient_health = Blueprint("patient_health", __name__)

app = Flask(__name__)
mysql = MySQL(app)


# patient_health:-
# create in postman by using jsonify:-
@app.route('/patient_health/create', methods=['POST'])
def patient_health():
    if 'health_id' in request.json and 'patient_id' in request.json \
            and 'blood_group' in request.json and 'patient_age' in request.json and 'patient_weight' in request.json \
            and 'patient_height' in request.json and 'systolic_bp' in request.json and 'dyastolic_bp' in request.json \
            and 'patient_temperature' in request.json and 'created_by' in request.json \
            and 'date' in request.json:

        health_id = request.json['health_id']
        patient_id = request.json['patient_id']
        blood_group = request.json['blood_group']
        patient_age = request.json['patient_age']
        patient_weight = request.json['patient_weight']
        patient_height = request.json['patient_height']
        systolic_bp = request.json['systolic_bp']
        dyastolic_bp = request.json['dyastolic_bp']
        patient_temperature = request.json['patient_temperature']
        created_by = request.json['created_by']
        date = request.json['date']

        # Cursor:-
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM patient_health WHERE PATIENT_HEALTH_ID = % s', (health_id,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        # Checking conditions:-
        elif not health_id or not patient_id or not blood_group or not patient_age or not patient_weight \
                or not patient_height or not systolic_bp or not dyastolic_bp or not patient_temperature \
                or not created_by:
            msg = 'Please fill out the fields !'

        else:
            cursor = mysql.connection.cursor()

            # UserId Pattern:-
            cursor.execute("SELECT USER_ID FROM patient_health")
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
                "insert into patient_health(PATIENT_HEALTH_ID, USER_ID, PATIENT_ID, BLOOD_GROUP, PATIENT_AGE, PATIENT_WEIGHT, PATIENT_HEIGHT, PATIENT_SYSTOLIC_BP, PATIENT_DYASTOLIC_BP, PATIENT_TEMPARATURE, CREATED_BY, IP_ADDRESS, USER_DEVICE, CREATED_DATE) "
                "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    patient_id, user_id, patient_id, blood_group, patient_age, patient_weight, patient_height,
                    systolic_bp,
                    dyastolic_bp, patient_temperature, created_by, IPAddress, hostname, date))
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
POST:- Inserting Values change health_id and patient_id every time.
http://127.0.0.1:5000/patient_health/create 
Body---> Raw----> json
{
    "health_id"             :   1,
    "patient_id"            :   1,
    "blood_group"           :   "B+",
    "patient_age"           :   "29",
    "patient_weight"        :   "80",
    "patient_height"        :   5,
    "systolic_bp"           :   10,
    "dyastolic_bp"          :   20,
    "patient_temperature"   :   "98.6",
    "created_by"            :   "Raghu"
    "date"                  :   "2021-06-06"    
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
