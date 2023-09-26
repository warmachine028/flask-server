from importlib import metadata
# from api import create_app
from api.file import SPAM

from flask import Flask

app = Flask(__name__)
__version__ = metadata.version("flask_server")


def main():
    app.run(host="localhost", debug=True)


@app.route("/")
def hello_world():
    return f"<h1>Hello from flask Server {SPAM}</h1>"


if __name__ == "__main__":
    main()
