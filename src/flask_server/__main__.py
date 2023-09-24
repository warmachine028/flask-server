from flask_server import create_app

app = create_app()

def main():
    # app.run(host="localhost", debug=True)
    app.run(host="0.0.0.0")

@app.route("/")
def hello_world():
    return "<h1>Hello from flask Server</h1>"

if __name__ == "__main__":
    main()
