from flask import Flask
from flask import render_template

app = Flask(__name__)

student = ["Anna", "Sajil"]


@app.route("/")
def hello_world():
    return render_template("home.html", person=student)
