import MySQLdb
from flask import Blueprint, jsonify

# blueprint setup
second = Blueprint("second", __name__)


@second.route("/home")
@second.route("/hom")
def home():
    return jsonify('Home page from home of /admin/home url of second blueprint instance !!!')


@second.route("/test")
def test():
    return "<h1>Test</h1>"


@second.route("/mysql")
def mysql():
    # Open database connection
    mysql = MySQLdb.connect("localhost", "root", "", "clinicalfirst")

    # prepare a cursor object using cursor() method
    cursor = mysql.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()

    # print()
    # print("Database version : %s " % data)

    return jsonify('Database version : %s ' % data)

    # disconnect from server
    db.close()


@second.route("/databases")
def databases():
    # Open database connection:-
    mysql = MySQLdb.connect("localhost", "root", "", "clinicalfirst")
    # mysql = MySQLdb.connections.cursors()

    # prepare a cursor object using cursor() method:-
    cursor = mysql.cursor()

    # execute SQL query using execute() method:-
    cursor.execute("SHOW DATABASES")

    # Response:-
    for x in cursor:
        return jsonify(x[0])


@second.route("/select")
def select_method():
    # Open database connection:-
    mysql = MySQLdb.connect("localhost", "root", "", "clinicalfirst")
    # mysql = MySQLdb.connections.cursors()

    # prepare a cursor object using cursor() method:-
    cursor = mysql.cursor()

    # execute SQL query using execute() method:-
    cursor.execute("SELECT * FROM user_signup")

    myresult = cursor.fetchone()

    return jsonify(myresult)


@second.route("/insert")
def insert_method():
    # Open database connection:-
    mysql = MySQLdb.connect("localhost", "root", "", "clinicalfirst")
    # mysql = MySQLdb.connections.cursors()

    # prepare a cursor object using cursor() method:-
    cursor = mysql.cursor()

    # execute SQL query using execute() method:-
    cursor.execute("SELECT * FROM user_signup")

    sql = "INSERT INTO user_signup (USER_ID, USER_NAME) VALUES (%s, %s)"
    val = [
        ('001', 'Raghu 2'),
        ('002', 'Raghu 3')
    ]

    cursor.executemany(sql, val)

    mysql.commit()

    # print(cursor.rowcount, "record was inserted.")

    # json response:-
    return jsonify(cursor.rowcount, "record was inserted.")


@second.route("/id")
def id():
    # Open database connection:-
    mysql = MySQLdb.connect("localhost", "root", "", "clinicalfirst")
    # mysql = MySQLdb.connections.cursors()

    # prepare a cursor object using cursor() method:-
    cursor = mysql.cursor()

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("Michelle", "Blue Village")
    cursor.execute(sql, val)

    mysql.commit()

    # print("1 record inserted, ID:", cursor.lastrowid)

    return jsonify("1 record inserted, ID:", cursor.lastrowid)
