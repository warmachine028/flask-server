# from importlib import metadata
# from flask import Flask
# # from flask_server.routes.health import health_bp
# # from flask_server.routes.users import users_bp
# # from flask_server.routes.error import error_bp
# # from flask_server.routes.auth import auth_bp

# __version__ = metadata.version("flask_server")


# # def create_app():
# app = Flask(__name__)
# # app.register_blueprint(health_bp)
# # app.register_blueprint(users_bp)
# # app.register_blueprint(error_bp)
# # app.register_blueprint(auth_bp)
#     # return app


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