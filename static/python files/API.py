from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL # Type this when you install this package flask-mysqldb
import MySQLdb.cursors

import hashlib
import logging

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'raghu'
app.config['MYSQL_DB'] = 'clinicalfirst'

# Intialize MySQL
mysql = MySQL(app)

logging.basicConfig(filename='log.txt', level=logging.warning(), filemode='a')

# http://localhost:5000/ - 1.This will be the index page, when the app starts:-
@app.route('/signup', methods=['POST'])
def USER_SIGNUP():
    if request.method == 'POST':
        try:
            USER_SIGNUP_ID = request.json['USER_SIGNUP_ID']
            USER_ID = request.json['USER_ID']
            USER_NAME = request.json['USER_NAME']
            USER_MAIL_ID = request.json['USER_MAIL_ID']
            USER_PHONE_NUMBER = request.json['USER_PHONE_NUMBER']
            USER_PASSWORD = request.json['USER_PASSWORD']
            USER_IP = request.json['USER_IP']

            j = hashlib.md5(USER_PASSWORD.encode())
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO USER_SIGNUP(USER_SIGNUP_ID,USER_ID,USER_NAME,USER_MAIL_ID,USER_PHONE_NUMBER,USER_PASSWORD,USER_IP) VALUES(%s,%s,%s,%s,%s,%s,%s)',
                        (USER_SIGNUP_ID,USER_ID,USER_NAME,USER_MAIL_ID,USER_PHONE_NUMBER,j.hexdigest(),USER_IP))
            mysql.connection.commit()
            cur.close()
            return jsonify('Signup Successful')
            logging.warning('warning information') #30
        except:
            return jsonify('user already exists try to login or signup with different credentials')


# Main function for our application to run the app instance on top given:-
if __name__ == "__main__":
    app.run(debug=True)



# filename='D:\\log.txt'


