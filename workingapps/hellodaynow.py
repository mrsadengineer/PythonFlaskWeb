print("Hello Day UI")
print("Now UI")
print("#############################################################")
from flask import Flask
from datetime import datetime
from flask import render_template
#import re

app = Flask(__name__)


#@app.route("/todaystime")
#def homeoftimehome():
#    return "Hello, Time!"





@app.route("/todaystime/")
@app.route("/todaystime/<name>")
def hello_there(name = None):

    if name == "simple":
        return printoutnow()

    else:
        return render_template(
        "hello_threeReturn.html",
        name=name,
        date=datetime.now()
     

    )

def printoutnow():
    now = datetime.now()
    print(now)
    somethingnew = now.__str__()
    return somethingnew


print("http://127.0.0.1:5000/todaystime/simple")
print("http://127.0.0.1:5000/todaystime/sammy")
print("http://127.0.0.1:5000/todaystime/raw")
print("http://127.0.0.1:5000/todaystime")


#@app.route("/api/data")
#def get_data():
#    return app.send_static_file("data.json")
app.run()