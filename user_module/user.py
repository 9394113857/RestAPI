import MySQLdb
from flask import Blueprint, jsonify, request

# blueprint setup
from flask_mysqldb import MySQL

db = Blueprint("db", __name__)

db.config['MYSQL_HOST'] = 'localhost'
db.config['MYSQL_USER'] = 'root'
db.config['MYSQL_PASSWORD'] = ''
db.config['MYSQL_DB'] = 'clinicalfirst'

mysql = MySQL(db)


@db.route("/home")
@db.route("/hom")
def home():
    return jsonify('Home page from home of /db/home url of database.py blueprint instance !!!')


@db.route("/test")
def test():
    return "<h1>Test</h1>"


@db.route("/version")
def mysql():
    # Open databasee connection
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


@db.route("/databases")
def databases():
    # Open databasee connection:-
    mysql = MySQLdb.connect("localhost", "root", "", "clinicalfirst")
    # mysql = MySQLdb.connections.cursors()

    # prepare a cursor object using cursor() method:-
    cursor = mysql.cursor()

    # execute SQL query using execute() method:-
    cursor.execute("SHOW DATABASES")

    # Response:-
    for x in cursor:
        return jsonify(x[0])


@db.route("/select")
def select_method():
    # Open databasee connection:-
    mysql = MySQLdb.connect("localhost", "root", "", "clinicalfirst")
    # mysql = MySQLdb.connections.cursors()

    # prepare a cursor object using cursor() method:-
    cursor = mysql.cursor()

    # execute SQL query using execute() method:-
    cursor.execute("SELECT * FROM user_signup")

    myresult = cursor.fetchone()

    return jsonify(myresult)


# @db.route("/insert")
# def insert_method():
#     # Open databasee connection:-
#     mysql = MySQLdb.connect("localhost", "root", "", "clinicalfirst")
#     # mysql = MySQLdb.connections.cursors()
#
#     # prepare a cursor object using cursor() method:-
#     cursor = mysql.cursor()
#
#     # execute SQL query using execute() method:-
#     cursor.execute("SELECT * FROM user_signup")
#
#     sql = "INSERT INTO user_signup (USER_ID, USER_NAME) VALUES (%s, %s)"
#     val = [
#         ('001', 'Raghu 2'),
#         ('002', 'Raghu 3')
#     ]
#
#     cursor.executemany(sql, val)
#
#     mysql.commit()
#
#     # print(cursor.rowcount, "record was inserted.")
#
#     # json response:-
#     return jsonify(cursor.rowcount, "record was inserted.")


@db.route("/id")
def id():
    # Open databasee connection:-
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


@db.route("/insert", methods=['POST'])
def insert():
    # Open databasee connection:-
    mysql = MySQLdb.connect("localhost", "root", "", "clinicalfirst")
    # mysql = MySQLdb.connections.cursors()

    userid = request.json
    user_id = userid['userid']

    username = request.json
    user_name = username['username']

    # prepare a cursor object using cursor() method:-
    cursor = mysql.cursor()

    # execute SQL query using execute() method:-
    cursor.execute("INSERT INTO user_signup (USER_ID, USER_NAME) VALUES (%s, %s)", (user_id, user_name))
    mysql.commit()

    return jsonify('Successfully Inserted'), 200

"""
Post man:-
POST:-
http://127.0.0.1:5000/db/insert
{
    "userid": "Us100",
    "username": "raghunadh"
}
"""