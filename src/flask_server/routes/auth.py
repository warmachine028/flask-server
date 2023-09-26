import jwt
from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

auth_bp = Blueprint("auth", __name__)

allowed_users = {
    "alice": generate_password_hash("my-pass"),
    "bob": generate_password_hash("his-pass"),
}
allowed_tokens = {
    "token-alice": "alice",
    "token-bob": "bob",
}

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme="Bearer")


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    if not data:
        raise Exception("No data found")

    if "username" not in data or "password" not in data:
        raise Exception("Unable to authenticate")
    name, password = data["username"], data["password"]

    if name not in allowed_users:
        raise Exception("User not Found")

    if not check_password_hash(allowed_users[name], password):
        raise Exception("Invalid Credentials")
    
    encoded_jwt = jwt.encode(
        {"sub": 1, "name": "sergio"}, "mysecret", algorithm="HS256"
    )
    return jsonify({"token": encoded_jwt})


@basic_auth.verify_password
def verify_basic_password(username, password):
    if username not in allowed_users:
        return

    if check_password_hash(allowed_users[username], password):
        return username


@token_auth.verify_token
def verify_token(token):
    try:
        decoded_jwt = jwt.decode(token, "mysecret", algorithm=["HS256"])
    except Exception as e:
        return None
    if decoded_jwt["name"] in allowed_users:
        return decoded_jwt["name"]
    return None
