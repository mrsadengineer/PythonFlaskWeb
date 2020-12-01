from flask import Flask
from datetime import datetime
from flask import render_template

app = Flask(__name__)



@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/python/")
def pythonfRef():
    return render_template("learnpython.html")

@app.route("/flask/")
def flaskRef():
    return render_template("learnflask.html")

@app.route("/api/")
def api():
    return render_template("now.html")

@app.route("/")
def home():
    return render_template("home.html")
    

print("#######Quick Links for Testing")

print("http://127.0.0.1:5000/")
print("http://127.0.0.1:5000/home")
print("http://127.0.0.1:5000/about")
print("http://127.0.0.1:5000/contact")
print("http://127.0.0.1:5000/now")
print("http://127.0.0.1:5000/api")
print("http://127.0.0.1:5000/python")
print("http://127.0.0.1:5000/flask")



print("#######################################")

def main():
    print("Python and Flask Reference Web App ")
    print("put on your seatbelts")
  
    print("#############################################################")
    app.run()

if __name__ == "__main__":
    main()




    #import re

#@app.route("/todaystime")
#def homeoftimehome():
#    return "Hello, Time!"


#@app.route("/todaystime/")
#@app.route("/todaystime/<name>")
#def hello_there(name = None):
#
#    if name == "simple":
#        return printoutnow()
#
#    else:
#        return render_template(
#        "hello_threeReturn.html",
#        name=name,
#        date=datetime.now()
#     
#
#    )
# main app routes
#@app.route("/api/data")
#def get_data():
#    return app.send_static_file("data.json")

#def printoutnow():
#    now = datetime.now()
#    print(now)
#    somethingnew = now.__str__()
#    return somethingnew
#



#print("http://127.0.0.1:5000/todaystime/simple")
#print("http://127.0.0.1:5000/todaystime/sammy")
#print("http://127.0.0.1:5000/todaystime/raw")
#print("http://127.0.0.1:5000/todaystime")
#