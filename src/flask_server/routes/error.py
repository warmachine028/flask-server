from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound

error_bp = Blueprint("errors", __name__)


@error_bp.app_errorhandler(NotFound)
def handle_not_found(err):
    return (
        jsonify({"message": "Resource not Found."}),
        err.code,
    )


# @error_bp.errorhandler(500)
@error_bp.app_errorhandler(Exception)
def handle_generic_exception(err):
    print(err.code, type(err))
    return (
        jsonify(
            {"message": "Internal Server Error. Please check the logs for more details"}
        ),
        err.code,
    )
