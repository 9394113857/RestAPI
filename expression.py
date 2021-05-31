# 1.This framework is for throwing Errors of Fields:-
# 2.Flask framework and Mysql Database:-
import re

from flask import request, jsonify, Flask, logging
from flask_mysqldb import MySQL

# 3.validation framework:-

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'raghu'
app.config['MYSQL_DB'] = 'clinicalfirst'

mysql = MySQL(app)


# User_Signup:-
# create in postman by using jsonify:-
@app.route('/users/create', methods=['POST'])
def register():
    if 'username' in request.json and 'password' in request.json \
            and 'email' in request.json and 'phone' in request.json and 'ip' in request.json and 'date' in request.json:
        username = request.json['username']
        email = request.json['email']
        phone = request.json['phone']
        password = request.json['password']
        userip = request.json['ip']
        date = request.json['date']
        # Cursor:-
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_signup WHERE USER_NAME = % s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not re.match(r'^[A-Za-z0-9@#$%^&+=]{8,32}',
                          password):
            msg = 'Password must contain alphanumber with specialcharacters !'
        elif not re.match(r'^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$', phone):
            msg = 'Invalid phone number and starts with +91 !'
        elif not re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
                          userip):
            msg = 'Invalid ip address format !'
        elif not re.match(r'^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$', date):
            msg = 'Invalid date format !'
        elif not username or not password or not email or not phone or not userip or not date:
            msg = 'Please fill out the fields !'

        else:
            cursor = mysql.connection.cursor()
            # UserId Pattern:-
            cursor.execute("SELECT USER_SIGNUP_ID FROM user_signup")
            lastid = cursor.rowcount
            print('----------------------')
            print("Last Id is: " + str(lastid))
            lastid += 1
            pattern = 'US000'
            # add_value = 00
            # pattern += 1 # pattern incremnting always by 1:-
            id_value = pattern + str(lastid)
            cursor.execute(
                "insert into user_signup(user_signup_id,USER_NAME,USER_MAIL_ID,USER_PHONE_NUMBER,USER_PASSWORD,USER_IP,"
                "USER_DATE_CREATED) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                (id_value, username, email, phone, password, userip, date))
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
@app.route('/users/create', methods=['POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.json and 'password' in request.json and 'email' in request.json:
        username = request.json['username']
        password = request.json['password']
        email = request.json['email']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_signup WHERE USER_NAME = % s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the fields !'
        else:
            
            # UserId Pattern:-
            lastid = cursor.execute("SELECT USER_SIGNUP_ID FROM user_signup")
            # lastid = cur.rowcount
            print('----------------------')
            print("Last Id is: " + str(lastid))
            lastid += 1
            pattern = 'US000'
            # add_value = 00
            # pattern += 1 # pattern incremnting always by 1:-
            id_value = pattern + str(lastid)
            
            cursor.execute("insert into user_signup(USER_NAME,USER_PASSWORD,USER_MAIL_ID) VALUES(%s,%s,%s)", (username, password, email))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    # Post man response:-
    details = cursor.fetchall()
    return jsonify({"details": details}), 200
"""

"""
# A class definition defines a 'class object':-
class UserSchema(Schema):
    user_name = fields.String(required=True)
    user_mail_id = fields.String(required=True)
    user_phone_number = fields.Integer(required=True)
    user_password = fields.String(required=True)
    user_ip = fields.String(required=True)
    user_date_created = fields.Date(required=True)
"""

"""
def function(self):
    validate_text(self.user_name, min_length=8, max_length=20, required=True,
                  pattern='^(?=[a-zA-Z0-9._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$')
    validate_text(self.user_password, min_length=4, max_length=8, required=True, pattern='A-Za-z0-9@#$%^&+=')
    validate_text(self.user_mail_id, min_length=4, max_length=8, required=True,
                  pattern='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    validate_int(self.user_phone_number, min_length=4, max_length=8, required=True,
                 pattern='^(?:(?:\+|00)91|0)\s*[\d](?:[\s.-]*\d{2}){4}$')
    validate_int(self.user_ip, min_length=4, max_length=8, required=True,
                 pattern='^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    validate_date(self.user_date_created, min_length=4, max_length=8, required=True,
                  pattern='^[0-2]\d|3[01])/(0\d|1[0-2])/([12]\d{3}')
"""

"""
    # A function definition defines a user-defined 'function object':-
    def validate_username(self, user_name):
        excluded_chars = "*?!'^+%&/()=}][{$#"
        for char in self.user_name.data:
            if char in excluded_chars:
                raise ValidationError(f"Character {char} is not allowed in username.")
"""

"""
# Common Error for all parameters:-
# updated decorator:-
def required_params(schema):
    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                schema.load(request.get_json())
            except ValidationError as err:
                error = {
                    "status": "error",
                    "messages": err.messages
                }
                return jsonify(error), 400
            return fn(*args, **kwargs)

        return wrapper

    return decorator
"""

"""
# User_Signup:-
# create in postman by using jsonify:-
@app.route('/users/create', methods=['POST'])
def register():
    if 'username' in request.json and 'password' in request.json and 'email' in request.json:
        username = request.json['username']
        email = request.json['email']
       # phone = request.json['phone']
        password  = request.json['password']
       # userip = request.json['ip']
       # date = request.json['date']
    # Cursor:-
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM user_signup WHERE USER_NAME = % s', (username,))
    account = cursor.fetchone()
    if account:
        msg = 'Account already exists !'
#   elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
    elif not re.match(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email):
        msg = 'Invalid email address !'
#   elif not re.match(r'[A-Za-z0-9]+', username):
    elif not re.match(r'[A-z][a-z0-9_-]{3,19}$', username):
        msg = 'Username must contain only characters and numbers !'
#   elif not re.match(r'[^(?=.*[a-z](?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$]+', password):
    elif not re.match(r'R@m@_f0rtu9e$', password):
        msg = 'Password must contain alphanumber with specialcharacters !'

    else:
        cursor.execute("insert into user_signup(USER_NAME,USER_MAIL_ID,USER_PASSWORD) VALUES(%s,%s,%s)",
                       (username, email, password,))
        mysql.connection.commit()

        details = cursor.fetchall()
        return jsonify({"details":details}), 200
    return 'Invalid Input !!!'
"""

"""
    elif not re.match(r'(\+91)?(-)?\s*?(91)?\s*?(\d{3})-?\s*?(\d{3})-?\s*?(\d{4})+', phone):
        msg = 'Invalid phone number and starts with +91 !'
    elif not re.match(
            r'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])+', userip):
        msg = 'Invalid ip address format !'
    elif not re.match(r'(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d+', date):
        msg = 'Invalid date format !'
    elif not username or not password or not email or not phone or not userip or not date:
        msg = 'Please fill out the form !'
    """

# if request.method == 'POST' and 'username' in request.json and 'password' in request.json \
#        and 'email' in request.json and 'phone' in request.json and 'ip' in request.json and 'date' in request.json:


#


""" 
# Old Route:-
# User_Signup:-
# create in postman by using jsonify:-
@app.route('/users/create', methods=['POST'])
# @required_params(UserSchema())
def create_usersignup():
    # user_signup_id = request.json['user_signup_id']

    user_name = request.json['user_name']
    user_mail_id = request.json['user_mail_id']
    user_phone_number = request.json['user_phone_number']
    user_password = request.json['user_password']
    user_ip = request.json['user_ip']
    user_date_created = request.json['user_date_created']
    # print(user_name, user_mail_id, user_phone_number, user_password, user_ip, user_date_created)
    cur = mysql.connection.cursor()  # Control.1

    # UserId Pattern:-
    lastid = cur.execute("SELECT USER_SIGNUP_ID FROM user_signup")
    # lastid = cur.rowcount
    print('----------------------')
    print("Last Id is: " + str(lastid))
    lastid += 1
    pattern = 'US000'
    # add_value = 00
    # pattern += 1 # pattern incremnting always by 1:-
    id_value = pattern + str(lastid)
    print("Current Id is: " + str(id_value) + str(" Inserted Successfully"))
    print('----------------------')

    # Insert and commit the changes:-
    cur.execute("insert into user_signup(USER_SIGNUP_ID,USER_NAME,USER_MAIL_ID,USER_PHONE_NUMBER,USER_PASSWORD,USER_IP,"
                "USER_DATE_CREATED) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                (id_value, user_name, user_mail_id, user_phone_number, user_password, user_ip, user_date_created))
    mysql.connection.commit()

    # Getting user details and showing response in postman:-
    details = cur.fetchall()
    return jsonify({'user_details': details}, {'Last Id': lastid}), 200
"""
