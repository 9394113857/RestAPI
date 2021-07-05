from flask import Flask
from flask_mysqldb import MySQL

from admin.second import second
from databasee.database import db

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'clinicalfirst'
mysql = MySQL(app)

# mysql.init_app(app)

app.register_blueprint(second, url_prefix="/second")
app.register_blueprint(db, url_prefix="/db")


# default root:-
@app.route("/")
def default():
    return "<h1>Test Message from Empty root !!!</h1>"


# MAIN app To Run the Flask Script:-
if __name__ == "__main__":
    app.run(debug=True)

# When you deploy before to the server:-
# Note:-     app.run(debug=False)
# Make debug value False and deploy the code.
