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
logging.basicConfig(filename="F:\Restful-API's\RestAPI\log files\Hospital.log",
					format='%(asctime)s %(message)s',
					filemode='a')

#Creating an object
logger=logging.getLogger()

#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

#Test messages
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
    if 'hospitalid' in request.json and 'hospitalname' in request.json and 'hospital_city'\
            and 'hospital_country' in request.json and 'hospital_zip_code' in request.json:

        hospitalid = request.json['hospitalid']
        hospitalname = request.json['hospitalname']
        hospital_city = request.json['hospital_city']
        hospital_country = request.json['hospital_country']
        hospital_zip_code = request.json['hospital_zip_code']

        # Cursor:-
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_hospital WHERE USER_HOSPITAL_ID = % s', (hospitalid,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[A-Za-z0-9]+', hospitalname):
            msg = 'Hospital Name must contain only characters and numbers !'
        elif not hospitalid or not hospitalname or not hospital_city or not hospital_country or not hospital_zip_code:
            msg = 'Please fill out the fields !'

        else:
            cursor = mysql.connection.cursor()

            # UserId Pattern:-
            cursor.execute("SELECT USER_ID FROM user_hospital")
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
            IPAddress = socket.gethostbyname(hostname)
            #print("Your Computer Name is:" + hostname)
            #print("Your Computer IP Address is:" + IPAddr)

            # Insert Code:-
            cursor.execute(
                "insert into user_hospital(USER_HOSPITAL_ID, USER_ID, HOSPITAL_NAME, HOSPITAL_CITY, HOSPPITAL_COUNTRY, HOSPITAL_ZIP_CODE, USER_IP, USER_DEVICE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                (hospitalid, user_id, hospitalname, hospital_city, hospital_country, hospital_zip_code, IPAddress, hostname))
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
POST:-
http://127.0.0.1:5000/hospitals/create 
Body---> Raw----> json
{
    "hospitalid"        : 1,
    "hospitalname"      : "Apollo Hospitals",
    "hospital_city"     : "Hyderabad",
    "hospital_country"  : "India",
    "hospital_zip_code" : "500072"
}
"""