import jwt
from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash
from flask_server.routes import allowed_users

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    if not data:
        raise Exception("No data found")
    if "username" not in data or "password" not in data:
        raise Exception("Unable to authenticate")

    if not check_password_hash(allowed_users[data["username"]], data["username"]):
        raise Exception("Invalid Credentials")

    encoded_jwt = jwt.encode(
        {"sub": 1, "name": "sergio"}, "mysecret", algorithm="HS256"
    )
    return jsonify({"token": encoded_jwt})