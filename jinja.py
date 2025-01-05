### Building Url Dynamically
## Variable Rule
### Jinja 2 Template Engine

### Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''

from flask import Flask,render_template,request,redirect,url_for
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])                    
def index():
    return render_template('index.html') #http://127.0.0.1:5000/index

@app.route('/about')
def about():
    return render_template('about.html') #http://127.0.0.1:5000/about

## YAHA TAK HUMNE 2 PARAMTER DEKHE ROUTE KAI ANDAR 1) ("/") OR ("/FUNCTION_NAME") 2) HTTP METHODS:- FOR WHICH OPRATION YOU HAVE TO PERFORM  
# NOW WE ARE GOING TO SEE 3 PARAMETER BY USING WHICH WE CAN TAKE INPUT DYNAMICALLY (MEANS AT RUN TIME ) AND ALSO APPLY CONDITIONS DYNAMICALLY i.e "Varaible rule " 

## Variable Rule
# EXAMPLES:- 
# 1) With Single Parameter 
@app.route('/user/<username>')
def user(username):
    return f"Hello, {username}!"        #http://127.0.0.1:5000/user/Adarsh#


# 2) With Single Parameter but with Typecaste...You need to specify which Datatype you want to take as input 
@app.route('/age/<int:age>')
def age(age):
    return f"You are {age} years old!"      #http://127.0.0.1:5000/age/20

#Visiting /age/25 will display:
#"You are 25 years old!

# 3) With Multiple Variables:

@app.route('/product/<string:name>/<int:price>')
def info(name, price):
    return f"The product {name} costs {price} units."
#/product/phone/999 will display:                       #http://127.0.0.1:5000/product/Phone/9999
#"The product phone costs 999 units."


## HERE I AM USING MY VARAIBLE RULE WITH "render_templet"..so it will integreat with "html" files and jinja2 is responsible for retriving Data source in that html file 
@app.route('/succex/<int:marks>')  # The <int:score> ensures score is already an integer when passed
def succex(marks):  
    
    if (marks >= 50):  # Perform the condition based on the integer score
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template('result.html', results=res)  #http://127.0.0.1:5000/succex/49
# This will integrate with "html" files and print the output on web page 

## Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    exp={'score':score,"res":res}  ## Here I am Storing my Expression as in the form of Key and Value pAir 

    return render_template('result2.html',results=exp)  ## From here "Exp" will pass and that will accepted by the jinja-2 and that will be "integretd" with htmi file "
    #http://127.0.0.1:5000/successres/75


## if confition
@app.route('/successif/<int:score>')
def successif(score):

    return render_template('result3.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result3.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))
            
# IN THIS (getresult.html and @app.route(/submit)) I AM DYNAMICALLY CONNECTING 2 ROUTES TOGHETHER HERE TWO ROUTES ARE 1) SUBMIT 2) successres  HERE I AM COLLLECTING DATA FROM SUBMIT ROUTE  
# BY USING THAT (getresult.html)form and after collecting the data I am Performing operation and finding result in "(successres)" it this route... Basically I am Giving Data of Marks here In (submit) route and 
# finding result in "successres" in this result...so Data reteiving in (submit) and result based on that Data in (successres)...This how we can Connect two routes 



if __name__=="__main__":
    app.run(debug=True)

