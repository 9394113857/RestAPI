from flask import Flask
from flask_mysqldb import MySQL
from admin.user import user
# from databasee.database import db
# from user_module.user import user

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'clinicalfirst'
app.config['SECRET_KEY'] = 'secret_key'

mysql = MySQL(app)

app.register_blueprint(user, url_prefix="/user")
# app.register_blueprint(db, url_prefix="/db")
# app.register_blueprint(user, url_prefix="/user")



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
