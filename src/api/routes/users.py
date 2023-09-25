from flask import Blueprint, jsonify, Response, request
from api.routes import basic_auth, token_auth

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("", methods=["GET"])
@basic_auth.login_required
def get_users():
    all_users = [
        {"id": 1, "name": "Alice Hussain"},
        {"id": 2, "name": "Bob Khan"},
    ]
    return jsonify(all_users)


@users_bp.route("", methods=["POST"])
@token_auth.login_required
def create_user():
    body = request.json
    print(body)
    return Response(status=204)
