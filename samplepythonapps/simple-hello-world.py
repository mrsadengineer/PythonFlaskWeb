print("Hello Simple World")
print("first")

from flask import Flask
from datetime import datetime
#import re
from flask import render_template


app = Flask(__name__)




#return a static data.json, programmable strings and, 

@app.route("/sayhellopsimppython")
def homeoftimehome():
    return "Hello Simple Python Input, Time!"


@app.route("/calccharthree/<name>")
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
print("http://127.0.0.1:5000/sayhellopsimppython")
print("http://127.0.0.1:5000/calccharthree/012345")
print("http://127.0.0.1:5000/itemoftime/now")
print("##############ENDOF_NO-UI###############")




# with ui

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






#working with varaible cross code and rendering template
@app.route("/todaystime/")
@app.route("/todaystime/<name>")
def hello_there_advance(name = None):

    if name == "simple":
        return printoutnow()

    else:
        return render_template(
        "hello_threeReturn.html",
        name=name,
        date=datetime.now()
    )

print("http://127.0.0.1:5000/todaystime/simple")
print("http://127.0.0.1:5000/todaystime/sammy")
print("http://127.0.0.1:5000/todaystime/raw")
print("http://127.0.0.1:5000/todaystime")
app.run()
