from functools import wraps

from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from marshmallow import Schema, fields
from marshmallow import ValidationError
# from msilib import schema
from marshmallow.validate import Length

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'raghu'
app.config['MYSQL_DB'] = 'clinicalfirst'

mysql = MySQL(app)


# Defining Schema for validations for json:-
class User_SignupSchema(Schema):
    """
    # Actual Code:-
    # user_name = fields.String(required=True)
    user_name = fields.String(required=True, validators=[Length(min=5, max=64, message='User Name length must be between %(min)d and %(max)dcharacters')])
    user_mail_id = fields.String(required=True, validators=[Email(), Length(max=120)])
    user_phone_number = fields.Integer(required=True, validators=[Length(max=10, message='Phone Number must be at least %(max)d characters long')])
    user_password = fields.String(required=True, validators=[Length(min=8, message='Password should be at least %(min)d characters long')])
    user_ip = fields.String(required=True, validators=[Length(max=120, message='IP Address must be at least %(max)d characters long')])
    user_date_created = fields.Date(required=True, validators=[DateField(), Length(max=120, message='Date Field must be at least %(max)d characters long')]) # Length method and parameters:-
    """

    # Testing the code:-
    user_name = fields.String(required=True, Validators=[Length(min=5)])
    user_mail_id = fields.String(required=True)
    user_phone_number = fields.Integer(required=True)
    user_password = fields.String(required=True)
    user_ip = fields.String(required=True)
    user_date_created = fields.Date(required=True)


# Common Error for all parameters:-
# updated decorator:-
def required_params(Schema):
    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                Schema.load(request.get_json())
            except ValidationError as err:
                error = {
                    "status": "error",
                    "messages": err.messages
                }
                return jsonify(error), 400
            return fn(*args, **kwargs)

        return wrapper

    return decorator


# User_Signup:-
# create in postman by using jsonify
@app.route('/users/create', methods=['POST'])
@required_params(User_SignupSchema())
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

    # Getting details and showing response in postman :-
    details = cur.fetchall()
    return jsonify({'user_details': details}, {'Last Id': lastid}), 200


if __name__ == "__main__":
    app.run(debug=True)
