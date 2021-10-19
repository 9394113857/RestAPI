from functools import wraps

from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

users = []


# 2nd Method:-
class UserSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    age = fields.Integer(required=True)
    married = fields.Boolean(required=True)


"""
1st Method:-
def required_params(required):
    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):
            _json = request.get_json()
            missing = [r for r in required.keys()
                       if r not in _json]
            if missing:
                response = {
                    "status": "error",
                    "message": "Request JSON is missing some required params",
                    "missing": missing
                }
                return jsonify(response), 400
            wrong_types = [r for r in required.keys()
                           if not isinstance(_json[r], required[r])]
            if wrong_types:
                response = {
                    "status": "error",
                    "message": "Data types in the request JSON doesn't match the required format",
                    "param_types": {k: str(v) for k, v in required.items()}
                }
                return jsonify(response), 400
            return fn(*args, **kwargs)
        return wrapper
    return decorator
"""


# 2nd Method:-
# updated decorator:-
def required_params(schema):
    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                schema.load(request.get_json())
            except ValidationError as err:
                error = {
                    "status": "error",
                    "messages": err.messages
                }
                return jsonify(error), 400
            return fn(*args, **kwargs)

        return wrapper

    return decorator


@app.route('/')
def hello_world():
    return 'Hello World!'


"""
1st Method:-
@app.route("/user/", methods=["POST"])
@required_params({"first_name": str, "last_name": str, "age": int, "married": bool})
def add_user():
    # here a simple list is used in place of a DB
    users.append(request.get_json())
    return "OK", 201
"""


# 2nd Method previous without @required_params
# Updated Route:-
@app.route("/user/", methods=["POST"])
@required_params(UserSchema())
def add_user():
    # here a simple list is used in place of a DB
    users.append(request.get_json())
    return "OK", 201


if __name__ == '__main__':
    app.run(debug=True)
