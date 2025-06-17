from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1>Welcome to DSA Flask Tutorial</h1><br>See batch details <a href="http://127.0.0.1:5000/about">here'


@app.route("/about")
def hello():
    return "<h1>From DSA SMP Feb Online Batch</h1>"
