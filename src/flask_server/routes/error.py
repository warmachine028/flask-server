from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound, MethodNotAllowed

error_bp = Blueprint("errors", __name__)


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
    message = jsonify(
        {"message": str(err)}
    )
    try:
        print(type(err), err.code)
        return (message, err.code)
    except AttributeError:
        return (message, 500)
