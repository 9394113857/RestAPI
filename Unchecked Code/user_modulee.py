# Insert Operation with hashlib library:-
@app.route('/user/create', methods=['POST'])
def register_user():
    if 'user_name' in request.json and 'mailid' in request.json \
            and 'user_phone_num' in request.json and 'user_password' in request.json:
        user_name = request.json['user_name']
        mailid = request.json['mailid']
        user_phone_num = request.json['user_phone_num']
        user_password = request.json['user_password']

        # hash_user = hashlib.md5(user_name.encode())
        hash_pass = hashlib.md5(user_password.encode())

        # Cursor Initialization:-
        cursor = mysql.connection.cursor()

        # UserId Pattern for Insert Operation:-
        cursor.execute("SELECT USER_ID FROM user_signup")
        last_user_id = cursor.rowcount
        print('----------------------------------')
        print("Last Inserted ID is: " + str(last_user_id))
        pattern = 'US000'  # pattern = ooo
        last_user_id += 1
        # add_value = 00
        # pattern += 1 # pattern incremnting always by 1:-
        user_id = pattern + str(last_user_id)  # pass 'user_id' value in place holder exactly
        # User Id pattern Code End #

        # Execute Operation:-
        cursor.execute(
            "insert into user_signup(USER_ID, USER_NAME, USER_MAIL_ID, USER_PHONE_NUMBER, USER_PASSWORD) VALUES(%s, %s, %s, %s, %s)",
            (user_id, user_name, mailid, user_phone_num, hash_pass))
        mysql.connection.commit()

        return "Your account has been created successfully !!!"

"""
POST
http://127.0.0.1:5000/userssss/insert
{
     "user_name"          :  "Raghu3",
     "mailid"           :  "raghunadh28@gmail.com",
     "user_phone_num" :  "9394113857",
     "user_password"     :  "Raghunadh@1234"
}
"""


# Login Functionality:-
@app.route('/')
@app.route('/user/login', methods=['GET', 'POST'])
def login_user():
    msg = ''
    if request.method == 'POST' and 'username' in request.json and 'password' in request.json:

        username = request.json['username']
        password = request.json['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_signup WHERE USER_NAME = % s AND USER_PASSWORD = % s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !!!'
            return jsonify('User Logged In Successfully')
        else:
            return jsonify('Incorrect Username/password check it it !!!')


# GET Method:-
@app.route('/user/logout')
def logout_user():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return jsonify('User Logged Out Successfully')

##############################################################################
# Insert Operation with bcrypt library:-
@app.route("/userss/insert", methods=['GET', 'POST'])
def register_user1():
    if 'user_name' in request.json and 'mailid' in request.json \
            and 'user_phone_num' in request.json and 'user_password' in request.json:
        # parameters:-
        user_name = request.json['user_name']
        mailid = request.json['mailid']
        user_phone_num = request.json['user_phone_num']
        user_password = request.json['user_password']

        # Hashed password with bcrypt library:-
        hashed_password = bcrypt.generate_password_hash(user_password).decode('utf-8')

        # Cursor Initialization:-
        cursor = mysql.connection.cursor()

        # UserId Pattern for Insert Operation:-
        cursor.execute("SELECT USER_ID FROM user_signup")
        last_user_id = cursor.rowcount
        print('----------------------------------')
        print("Last Inserted ID is: " + str(last_user_id))
        pattern = 'US000'  # pattern = ooo
        last_user_id += 1
        # add_value = 00
        # pattern += 1 # pattern incremnting always by 1:-
        user_id = pattern + str(last_user_id)  # pass 'user_id' value in place holder exactly
        # User Id pattern Code End #

        # Execute Operation:-
        cursor.execute(
            "insert into user_signup(USER_ID, USER_NAME, USER_MAIL_ID, USER_PHONE_NUMBER, USER_PASSWORD) VALUES(%s, %s, %s, %s, %s)",
            (user_id, user_name, mailid, user_phone_num, hashed_password))
        mysql.connection.commit()

        return "Your account has been created successfully!"

# Checking login user with password using bcrypt functionality:-
@app.route("/userss/login", methods=['GET', 'POST'])
def login_user1():
    if 'mail_id' in request.json and 'password' in request.json:
        mail_id = request.json['mail_id']
        password = request.json["password"]
        cur = mysql.connection.cursor()
        cur.execute("select * from user_signup WHERE (USER_MAIL_ID = %s)", (mail_id,))
        details = cur.fetchone()
        if details is None:
            return ({"Error": "No details"}), 401
        # here 2 is the index num
        hashed_password = details[4]
        password_match = check_password_hash(hashed_password, password)
        if password_match:
            # # generate the JWT Token
            # token = jwt.encode({
            #     'user_mail': mail_id,
            #     'exp': datetime.utcnow() + timedelta(minutes=2)},
            #     app.config['SECRET_KEY'], algorithm='HS256')

            # return token
            return jsonify('User Logged-In Successfully !!!')
        else:
            return ({"Error": "invalid credentials"}), 401
    return "Insufficient parameters", 400

# Logout the user:-
@app.route("/userss/logout")
def logout_user1():
    logout_user()
    # return redirect(url_for('home'))
    return jsonify('User Logged-Out Successfully !!!!')

