from flask import Blueprint, jsonify, Response, request
from flask_server.routes.auth import basic_auth, token_auth

users_bp = Blueprint("users", __name__, url_prefix="/users")
all_users = [
    {"id": 1, "name": "Alice Hussain"},
    {"id": 2, "name": "Bob Khan"},
]


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



