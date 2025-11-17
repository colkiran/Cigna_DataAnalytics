from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return("<h1> Hello World </h1>")

@app.route("/<usrname>")
def user(usrname):
    return f"<h2> Greetings {usrname.upper()}, Welcome to Flask Programming..."


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)


