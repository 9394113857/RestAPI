from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'raghu'
app.config['MYSQL_DB'] = 'clinicalfirst'

mysql = MySQL(app)


@app.route("/users")
def health():
    cur = mysql.connection.cursor()
    cur.execute("select * from user_signup")
    user_details = cur.fetchall()
    print(user_details, "User Details")
    return jsonify(user_details), 200


@app.route("/users/<USER_SIGNUP_ID>", methods=['GET'])
def get_single_user(USER_SIGNUP_ID):
    cur = mysql.connection.cursor()
    cur.execute("select * from user_signup where user_signup_id =" + USER_SIGNUP_ID)
    # cur.lastrowid
    user_details = cur.fetchall()
    return jsonify({"user_details": user_details}), 200


# User_Signup:-
# create in postman by using jsonify
@app.route('/users/create', methods=['POST'])
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

    # Next Logic:-
    cur.execute("SELECT USER_SIGNUP_ID FROM user_signup")
    lastid = cur.rowcount
    print('----------------------')
    print("Last Id is: " + str(lastid))
    lastid += 1
    pattern = 'US000'
    # add_value = 00
    # pattern += 1 # pattern incremnting always by 1:-
    id_value = pattern + str(lastid)
    print("Next Id is: " + str(id_value))
    print('----------------------')

    cur.execute("insert into user_signup(USER_SIGNUP_ID,USER_NAME,USER_MAIL_ID,USER_PHONE_NUMBER,USER_PASSWORD,USER_IP,"
                "USER_DATE_CREATED) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                (id_value, user_name, user_mail_id, user_phone_number, user_password, user_ip, user_date_created))
    mysql.connection.commit()  # Control.2

    details = cur.fetchall()
    return jsonify({'user_details': details}, {'Last Id': lastid}), 200


@app.route('/login', methods=["POST"])
def login():
    if 'email' in request.json and 'password' in request.json:
        email = request.json["email"]
        pw = request.json["password"]
        cur = mysql.connection.cursor()
        cur.execute("select * from user_signup WHERE (USER_MAIL_ID = %s AND USER_PASSWORD = %s)", (email, pw))
        details = cur.fetchone()
        if details is not None:
            return ({"message": "successfully loged"})
        else:
            return ({"Error": "invalid credentials"}, 401)

    return "Insufficient parameters", 400


# Delete operation:-
# delete in postman by using josnify
@app.route("/users/delete/<USER_SIGNUP_ID>", methods=['DELETE'])
def delete_user_signup(USER_SIGNUP_ID):
    cur = mysql.connection.cursor()
    cur.execute("delete from user_signup where USER_SIGNUP_ID =" + USER_SIGNUP_ID)
    mysql.connection.commit()
    """
    cur.execute("SELECT USER_SIGNUP_ID FROM user_signup")
    lastid = cur.lastrowid
    print()
    #print("Last Updated Id: " + lastid)
    print(lastid)
    """
    user_details = cur.fetchall()
    return jsonify({'user_details': user_details}), 200


# Update method:-
# update in postman by using josnify
@app.route("/users/update", methods=['PUT'])
def update_user_signup():
    user_signup_id = request.json['signupId']
    user_name = request.json['userName']
    user_mail_id = request.json['emailId']
    user_phnum = request.json['phoneNumber']
    cur = mysql.connection.cursor()
    cur.execute("""
         UPDATE user_signup set USER_NAME = %s, USER_MAIL_ID = %s, USER_PHONE_NUMBER = %s WHERE USER_SIGNUP_ID =%s
         """, (user_name, user_mail_id, user_phnum, user_signup_id))
    mysql.connection.commit()
    user_details = cur.fetchall()
    return jsonify({'userdetails': user_details})


# User_Registration Code:-
# create in postman by using jsonify
@app.route('/users_registration/register', methods=['POST'])
def user_registration():
    # user_reg_id = request.json['user_reg_id']
    # user_id = request.json['user_id']
    """
    user_age = request.json['user_age']
    user_experience = request.json['user_experience']
    user_gender = request.json['user_gender']
    user_lic_num = request.json['user_lic_num']
    flat_no = request.json['flat_no']
    street_name = request.json['street_name']
    city_name = request.json['city_name']
    state_name = request.json['state_name']
    country_name = request.json['country_name']
    zip_code = request.json['zip_code']
    user_approved = request.json['user_approved']
    user_ip = request.json['user_ip']
    """

    # New Code:-
    user_reg_id = request.json['user_reg_id']
    user_date_registered = request.json['user_date_registered']
    ip_address = request.get_json()

    cur = mysql.connection.cursor()
    # Next Logic:-

    """ Main Code:-
    cur.execute("insert into user_registration(USER_REG_ID,USER_ID,USER_AGE,USER_Experience,USER_GENDER,USER_LICENSE_NUMBER, FLAT_NO,STREET_NAME,CITY_NAME,STATE_NAME,COUNTRY_NAME,ZIP_CODE,USER_APPROVED,USER_IP,"
                "USER_DATE_CREATED) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(usersignupid,user_id, user_age, user_lic_num, flat_no, street_name, city_name, state_name, country_name, zip_code, user_approved, user_ip, user_datge_registered))
    """

    # The last() function is used to return the last value of the specified column:-
    cur.execute("SELECT USER_SIGNUP_ID FROM user_signup ORDER BY USER_SIGNUP_ID DESC LIMIT 1")
    usersignupid = cur.fetchone()

    cur.execute("insert into user_registration(USER_REG_ID,USER_ID,"
                "USER_DATE_REGISTERED) VALUES(%s,%s,%s)", (user_reg_id, usersignupid, user_date_registered))
    mysql.connection.commit()

    details = cur.fetchone()
    return jsonify({'user_details': details}, {'Last Id': usersignupid}), 200


if __name__ == "__main__":
    app.run(debug=True)
