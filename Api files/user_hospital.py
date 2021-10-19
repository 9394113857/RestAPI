# 1.This framework is for throwing Errors of Fields:-
# 2.Flask framework and Mysql Database:-
# importing module
import logging
import re
# 3. Get ip and device name from socket library:-
import socket

from flask import request, Flask
from flask_mysqldb import MySQL

# Create and configure logger
logging.basicConfig(filename="F:\Restful-API's\RestAPI\log files\Hospital.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages
logger.info('-----------------------------')
logger.info("User_Hospital script started Now:-")
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


# User_Hospital:-
# create in postman by using jsonify:-
@app.route('/hospitals/create', methods=['POST'])
def hospital():
    if 'hospital_id' in request.json and 'hospital_name' in request.json and 'hospital_city' \
            and 'hospiatal_country' in request.json and 'hospital_zip_code' in request.json:

        hospital_id = request.json['hospital_id']
        hospital_name = request.json['hospital_name']
        hospital_city = request.json['hospital_city']
        hospiatal_country = request.json['hospiatal_country']
        hospital_zip_code = request.json['hospital_zip_code']

        # Cursor:-
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_hospital WHERE USER_HOSPITAL_ID = % s', (hospital_id,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[A-Za-z0-9]+', hospital_name):
            msg = 'Hospital Name must contain only characters and numbers !'
        elif not re.match(r'[A-Za-z0-9]+', hospital_city):
            msg = 'Hospital City must contain only characters and numbers !'
        elif not re.match(r'[A-Za-z0-9]+', hospiatal_country):
            msg = 'Hospital Country must contain only characters and numbers !'
        elif not hospital_id or not hospital_name or not hospital_city or not hospiatal_country or not hospital_zip_code:
            msg = 'Please fill out the fields !'

        else:
            cursor = mysql.connection.cursor()

            # UserId Pattern:-
            cursor.execute("SELECT USER_ID FROM user_hospital")
            lastid = cursor.rowcount
            print('----------------------')
            print("Last Id is: " + str(lastid))
            lastid += 1
            pattern = 'US000'  # pattern = ooo
            # add_value = 00
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
                "insert into user_hospital(USER_HOSPITAL_ID, USER_ID, HOSPITAL_NAME, HOSPITAL_CITY, HOSPPITAL_COUNTRY, HOSPITAL_ZIP_CODE, USER_IP, USER_DEVICE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                (hospital_id, user_id, hospital_name, hospital_city, hospiatal_country, hospital_zip_code, IPAddress,
                 hostname))
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
POST:- // Inserting Values change hospital_id every time.
http://127.0.0.1:5000/hospitals/create 
Body---> Raw----> json
{
    "hospital_id"        : 1,
    "hospital_name"      : "Apollo",
    "hospital_city"      : "Hyd",
    "hospiatal_country"  : "Ind",
    "hospital_zip_code"  :  500072
}
"""
