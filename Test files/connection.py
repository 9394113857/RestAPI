from flask import Blueprint, jsonify

from database import mysql

# Blueprint Setup:-
read = Blueprint('read', __name__)


@read.route('/read')
def defaut():
    # creating the cursor object
    cur_obj = mysql.cursor()

    try:
        # creating a new databasee using query
        cur_obj.execute("create databasee New_PythonDB")

        # getting the list of all the databases which will now include the new databasee New_PythonDB
        dbms = cur_obj.execute("show databases")

    except:
        cur_obj.rollback()  # it is used if the operation is failed then it will not reflect in your databasee

    for x in cur_obj:
        # print(x)
        return jsonify(x)

    cur_obj.close()
