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
logging.basicConfig(filename="F:\Restful-API's\RestAPI\log files\Qualification.log",
					format='%(asctime)s %(message)s',
					filemode='a')

#Creating an object
logger=logging.getLogger()

#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

#Test messages
logger.info('-----------------------------')
logger.info("User_Qualification script started Now:-")
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


# User_Qualification:-
# create in postman by using jsonify:-
@app.route('/qualifications/create', methods=['POST'])
def qualification():
    if 'qual_id' in request.json and 'qual_name' in request.json and 'inst_name' in request.json\
            and 'procurement_year' in request.json:

        qual_id = request.json['qual_id']
        qual_name = request.json['qual_name']
        inst_name = request.json['inst_name']
        procurement_year = request.json['procurement_year']

        # Cursor:-
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_qualifiaction WHERE USER_QUAL_ID = % s', (qual_id,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[A-Za-z0-9]+', qual_name): # perfect
            msg = 'Qualification Name name must contain only characters and numbers !'
        elif not re.match(r'[A-Za-z0-9]+', inst_name): # perfect
            msg = 'Institution Name must contain only characters and numbers !'
        elif not qual_id or not qual_name or not inst_name or not procurement_year:
            msg = 'Please fill out the fields !'

        else:
            cursor = mysql.connection.cursor()

            # UserId Pattern:-
            cursor.execute("SELECT USER_ID FROM user_qualifiaction")
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
                "insert into user_qualifiaction(USER_QUAL_ID, USER_ID, USER_QUALIFICATION_NAME, INSTITUTE_NAME, PROCUREMENT_YEAR, USER_IP, USER_DEVICE) "
                "VALUES(%s,%s,%s,%s,%s,%s,%s)",(qual_id, user_id, qual_name, inst_name, procurement_year, IPAddress, hostname))
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
POST:- // Inserting Values change qual_id every time.
http://127.0.0.1:5000/qualifications/create 
Body---> Raw----> json
{
    "qual_id"           : 1,
    "qual_name"         : "MBBS",
    "inst_name"         : "APOLLO HEALTH CARE CITY",
    "procurement_year"  : "2021-06-07"
}
"""