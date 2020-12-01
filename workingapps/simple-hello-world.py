print("Hello Simple World")
print("Time Date")

from flask import Flask
from datetime import datetime
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




print("http://127.0.0.1:5000/api/data")
print("http://127.0.0.1:5000/itemoftime")
print("http://127.0.0.1:5000/itemoftime/now")
app.run()
