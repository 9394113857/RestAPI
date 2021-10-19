from flask import Flask

from user_signup import logger

app = Flask(__name__)

print(logger.info("Successfully Registred"))

if __name__ == "__main__":
    app.run(debug=True)