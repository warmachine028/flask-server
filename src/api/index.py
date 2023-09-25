# from importlib import metadata
# from api import create_app

# __version__ = metadata.version("flask_server")

from flask import Flask

app = Flask(__name__)


def main():
    app.run(host="localhost", debug=True)


@app.route("/")
def hello_world():
    return "<h1>Hello from flask Server</h1>"


if __name__ == "__main__":
    main()
