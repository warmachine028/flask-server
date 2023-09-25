from importlib import metadata
from flask import Flask
from flask_server import create_app

__version__ = metadata.version("flask_server")
app = create_app()


def main():
    # app.run(host="localhost", debug=True)
    app.run(host="0.0.0.0")

@app.route("/")
def hello_world():
    return "<h1>Hello from flask Server</h1>"

if __name__ == "__main__":
    main()
