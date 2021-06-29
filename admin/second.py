from flask import Blueprint, jsonify

second = Blueprint("second", __name__)


@second.route("/home")
@second.route("/")
def home():
    return jsonify('Home page from home of /admin/home url')


@second.route("/test")
def test():
    return "<h1>Test</h1>"
