"""
NOTE:- BEFORE USING (render_templet)

from flask import Flask
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask course.This should be an amazing course"

@app.route("/index") 
def index():
    return "Welcome to the index  page"


if __name__=="__main__":
    app.run(debug=True)
"""
# render_templet html and py files ko separately  handle karega toh (Frontend and backend) dono alag rahenge 
# AFTER USING (render_templet)

from flask import Flask,render_template
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/") 
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True)


    """ URL IS :- http://127.0.0.1:5000/   JUST ADD THE name of the html in any case """