# import os

# app = create_app()

# def main():
#     # app.run(port=os.environ.get('PORT', 3000))
#     app.run(port="localhost:5000")

# @app.route("/")
# def hello_world():
#     return "<h1>Hello from flask Server</h1>"

# if __name__ == "__main__":
#     main()

from flask import Flask
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask_server.__init__ import create_app

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello from flask Server</h1>" + str(create_app)

