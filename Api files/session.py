# 1.This framework is for throwing Errors of Fields:-
# 2.Flask framework and Mysql Database:-
# 3. Get ip and device name from socket library:-
# importing module
import logging
import socket

from flask import request, Flask
from flask_mysqldb import MySQL

# Create and configure logger
logging.basicConfig(filename="F:\Restful-API's\RestAPI\log files\session.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages
logger.info('-----------------------------')
logger.info("Session script started Now:-")
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


# Session:-
# create in postman by using jsonify:-
@app.route('/session/create', methods=['POST'])
def session():
    if 'id' in request.json and 'session_id' in request.json \
            and 'patient_id' in request.json:

        id = request.json['id']
        session_id = request.json['session_id']
        patient_id = request.json['patient_id']

        # Cursor:-
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM session WHERE ID = % s', (id,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        # Checking conditions:-
        elif not id or not session_id or not patient_id:
            msg = 'Please fill out the fields !'

        else:
            cursor = mysql.connection.cursor()

            # UserId Pattern:-
            cursor.execute("SELECT USER_ID FROM session")
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
                "insert into session(ID, USER_ID, SESSION_ID, PATIENT_ID, USER_IP, USER_DEVICE) "
                "VALUES(%s,%s,%s,%s,%s,%s)", (id, user_id, session_id, patient_id, IPAddress, hostname))
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
POST:- Inserting Values change id every time.
http://127.0.0.1:5000/session/create 
Body---> Raw----> json
{
    "id"         : 1,
    "session_id" : "1",
    "patient_id" : 1
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
