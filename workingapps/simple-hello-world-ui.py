print("Hello Simple World UI")
print("User Interface")

from flask import Flask
from datetime import datetime
from flask import render_template
#import re

app = Flask(__name__)


@app.route("/itemoftime")
def homeoftimehome():
    return "Hello, Time!"


@app.route("/itemoftime/<name>")
def UnitOfTime(name):
    print(name)
    content = name[3]
    return content


@app.route("/itemoftime/now")
def printoutnow():
    now = datetime.now()
    print(now)
    somethingnew = now.__str__()
    return somethingnew


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

print("http://127.0.0.1:5000/hello/sammy")
print("http://127.0.0.1:5000/hello")

app.run()