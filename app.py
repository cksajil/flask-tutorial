from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/result", methods=["POST"])
def result_page():
    user_name = request.form["user_name"]
    return render_template("result.html", name=user_name)
