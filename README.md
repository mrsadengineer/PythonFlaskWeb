# Python Flask Web App  



## Introduction - the project's aim  

App to explore the programming language of Python and to create resources for understanding Flask. Introductory investigation in using python and Flask together with VSCODE and git.   

## Technologies
Project is created with:  

Python  3.8.6
Flask  



### Placement for Future README Sub sections  
Launch/ To Setup  
Table of contents  
Illustrations  
Scope of functionalities  
Examples of use  
Other information 

## Project status
The project is in the beginning.   

## Sources
https://code.visualstudio.com/docs/python/tutorial-flask

https://flask.palletsprojects.com/en/1.0.x/cli/

https://github.com/microsoft/python-sample-vscode-flask-tutorial



### Dev Installation Steps
Install Python  
Install pip  
install virtual environment  
Create Project App root folder  
Create virutal enviromenet   
    python -m venv <env>  
Set Up Editor (VSCODE)  
Add Code  
-Python  
-Flask  
--Templates folder 
--Static Content folder  


#### For Windows
##### To create virtual environment
python -m venv env



#### to run app
There are bascially two ways to start a flask app. Within the code using app.run() or through the flask cmd line lagnauge `flask run`  
Depending on your intentions, you would want use the best approche when you ask yourself, "should I use app.run() or flask run?"  

But before running the flask app, make scure the virtual enviroment is running. You can do it manuely or by seting up the python interperter. To manuely activate virtual enviroment by typing in the command line:
  
'env\scripts\activate'  
#### Selecting Python Interperter in VSCODE
For Development in VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command:

Activate virtual enviroment by:
use Terminal: Create New Integrated Terminal     

#### Running by Command Line 
When in the virtual virtual enviroment

python -m flask run

#### Command time commans
To quit session  

`ctrl + c` to exit





Set up debugger configuration