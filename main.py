from flask import Flask
from flask_mysqldb import MySQL

from user_module.user_signup import user

app = Flask(__name__)
app.register_blueprint(user, url_prefix="/user")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'raghu'
app.config['MYSQL_DB'] = 'clinicalfirst'

mysql = MySQL(app)


# default root:-
@app.route("/")
def test():
    return "<h1>Test Message from Empty root Raghu !!!</h1>"


# MAIN app To Run the Flask Script:-
if __name__ == "__main__":
    app.run(debug=True)

# When you deploy before to the server:-
# Note:-     app.run(debug=False)
# Make debug value False and deploy the code.
