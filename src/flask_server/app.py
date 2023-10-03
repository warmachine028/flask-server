import jwt
from flask import Flask, Blueprint, request, Response, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import NotFound, MethodNotAllowed
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth


health_bp = Blueprint("health", __name__)
users_bp = Blueprint("users", __name__, url_prefix="/users")
auth_bp = Blueprint("auth", __name__)
error_bp = Blueprint("errors", __name__)

allowed_users = {
    "alice": generate_password_hash("my-pass"),
    "bob": generate_password_hash("his-pass"),
}
allowed_tokens = {
    "token-alice": "alice",
    "token-bob": "bob",
}
all_users = [
    {"id": 1, "name": "Alice Hussain"},
    {"id": 2, "name": "Bob Khan"},
]
basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme="Bearer")

## auth.py
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


## health.py
@health_bp.route("/health", methods=["GET"])
def health_check():
    return "ok"


## users.py
@users_bp.route("", methods=["GET"])
@basic_auth.login_required
def get_users():
    return jsonify(all_users)


@users_bp.route("", methods=["POST"])
@token_auth.login_required
def create_user():
    body = request.json
    print(body)
    return Response(status=204)


## error.py
@error_bp.app_errorhandler(NotFound)
def handle_not_found(err):
    return (
        jsonify({"message": "Resource not Found."}),
        err.code,
    )


@error_bp.app_errorhandler(MethodNotAllowed)
def handle_method_not_allowed(err):
    return (jsonify({"message": "Method not allowed."}), err.code)


@error_bp.app_errorhandler(Exception)
def handle_generic_exception(err):
    message = jsonify({"message": str(err)})
    try:
        print(type(err), err.code)
        return (message, err.code)
    except AttributeError:
        return (message, 500)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(error_bp)
    return app

app = create_app()

def main():
    app.run(host="localhost", debug=True)

@app.route("/")
def hello_world():
    return "<h1>Hello from flask Server</h1>"

if __name__ == "__main__":
    main()