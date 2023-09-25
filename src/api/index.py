# from importlib import metadata
# from api import create_app

# __version__ = metadata.version("flask_server")

# app = create_app()

# def main():
#     # app.run(host="localhost", debug=True)
#     app.run(host="0.0.0.0")

# @app.route("/")
# def hello_world():
#     return "<h1>Hello from flask Server</h1>"

# if __name__ == "__main__":
#     main()

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'