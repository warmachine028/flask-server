from flask import Blueprint, request
from werkzeug.security import check_password_hash

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    if "username" not in data or "password" not in data:
        raise Exception("Unable to authenticate")

    if not check_password_hash(allowed_users)
