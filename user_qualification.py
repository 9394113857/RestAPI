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


# User_Qualification:-
# create in postman by using jsonify:-
@app.route('/qualifications/create', methods=['POST'])
def qualification():
    if 'qualid' in request.json and 'qualname' in request.json and 'instname' in request.json\
            and 'procurement_year' in request.json:

        qualid = request.json['qualid']
        qualname = request.json['qualname']
        instname = request.json['instname']
        procurement_year = request.json['procurement_year']

        # Cursor:-
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_qualifiaction WHERE USER_QUAL_ID = % s', (qualid,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[A-Za-z0-9]+', qualname): # perfect
            msg = 'Qualification Name name must contain only characters and numbers !'
        elif not re.match(r'[A-Za-z0-9]+', instname): # perfect
            msg = 'Institution Name must contain only characters and numbers !'
        elif not qualid or not qualname or not instname or not procurement_year:
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
                "VALUES(%s,%s,%s,%s,%s,%s,%s)",(qualid, user_id, qualname, instname, procurement_year, IPAddress, hostname))
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

