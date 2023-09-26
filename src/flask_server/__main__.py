from flask_server import create_app
import os

app = create_app()

def main():
    app.run(port=os.environ.get('PORT', 5000))

@app.route("/")
def hello_world():
    return "<h1>Hello from flask Server</h1>"

if __name__ == "__main__":
    main()
