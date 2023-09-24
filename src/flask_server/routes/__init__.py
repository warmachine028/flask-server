import importlib.metadata
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash

__version__ = importlib.metadata.version("flask_server")

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme="Bearer")

allowed_users = {
    "alice": generate_password_hash("my-pass"),
    "bob": generate_password_hash("his-pass"),
}
allowed_tokens = {"token-alice": "alice", "token-bob": "bob"}


@basic_auth.verify_password
def verify_basic_password(username, password):
    if username not in allowed_users:
        return

    if check_password_hash(allowed_users[username], password):
        return username


@token_auth.verify_token
def verify_token(token):
    if token not in allowed_tokens:
        return
    return allowed_tokens[token]
