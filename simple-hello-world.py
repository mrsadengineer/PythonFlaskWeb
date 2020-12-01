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
    #string something = 
    #timetoremember = datetime.combine()

    
    print(name)
    content = name[3]
    return content



print("http://127.0.0.1:5000/itemoftime")
app.run()