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


# patient_health:-
# create in postman by using jsonify:-
@app.route('/patient_health/create', methods=['POST'])
def patient_health():
    if 'health_id' in request.json and 'patient_id' in request.json \
    and 'blood_group' in request.json and 'patient_age' in request.json and 'patient_weight' in request.json \
    and 'patient_height' in request.json and 'systolic_bp' in request.json and 'dyastolic_bp' in request.json \
    and 'patient_temperature' in request.json and 'created_by' in request.json\
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
        elif not health_id or not patient_id or not blood_group or not patient_age or not patient_weight\
               or not patient_height or not systolic_bp or not dyastolic_bp or not patient_temperature\
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
                "insert into patient_health(PATIENT_HEALTH_ID, USER_ID, PATIENT_ID, BLOOD_GROUP, PATIENT_AGE, PATIENT_WEIGHT, PATIENT_HEIGHT, PATIENT_SYSTOLIC_BP, PATIENT_DYASTOLIC_BP, PATIENT_TEMPARATURE, CREATED_BY, IP_ADDRESS, USER_DEVICE, CREATED_DATE) "
                "VALUES(%s,%s,%s,%s,%s,%s)", (patient_id, id_value, patient_id, blood_group, patient_age, patient_weight, patient_height, systolic_bp, dyastolic_bp, patient_temperature, created_by, IPAddress, hostname, date))
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