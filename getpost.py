from flask import Flask,render_template,request
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
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST']) # Here we are using both " HTTP methods " 
                    # GET:- TO READ THE WEB-PAGE AND TO SEE THE CONTENT
                    # POST:- TO ADD / SUBMIT THE FORM  , TO UPDATE THE WEB-PAGE 
                    # request.method:- This is imp to send request / retrive Data  to the server about any particular Data   

def form():
    if request.method=='POST':     # When "request.method==POST" is successful then IT WILL UPDATE THE "DATA" INTO THE WEB-PAGE 
        name=request.form['name']   # AND HERE THE DATA IS GOING TO UPDATE IS "name"...The name is going to update in" html file"..name will go and update the print the statemnt 
        return f'Hello {name}!'     # After updating ,... Suppose this   "request.method==POST" is get failed it will print the      return render_template('form.html') this staemnt ...and call the html page 
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST']) ## This will submit the form 
def submit():                       # Whenever you are click on submit button then this , will go and excute the "submit.html" form and then it will excute and print the stament  
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!' # print this statement with whatever the name you have given 
    return render_template('form.html')


if __name__=="__main__":
    app.run(debug=True)

"""
NOTE:- WHAT WE ARE DOING HERE IS WE ARE WRITING ONE STAEMENT AND WE ARE CALLING THAT FUNCTION THROUGH HTML PAGE AND REDIRECTING IT TO THE WEB-PAGE WITH THE HELP PF
(render_templet) BUT , WHATEVER THE STATEMENT I AM PASSING , IT IS WRITTEN IN CODE ONLY MAI CODE SAI HI BHEJ RAHA HU , I WANTED TO SEND THE 
STRING AND INPUT VARAILE DYNAMICALLY .... FOR EG :- JASAI HUM PRINT STATEMNT KAI ANDAR JASAI STRING KO PASS KARTE HAU WOH JAKE PRINT HOTA HAI IT IS NOT DYNAMIC 
BUT, MAI JAB INPUT FUNCTION USE KARKE DYNAMICALLY INPUT LETA HU TAB MAI AT RUN TIME INPUT LERA HOT HU... THAT IS AT RUN TIME.... SO , THAT IS CALLED AS DYNAMIC..
VASAI HI AGAR MUJHE ALL STRINGS, STATEMENT , VARIABLES DYNAMICALLY INPUT/OUTPUT KARNE HAI TOH MUJHE :- BUILD URL DYNAMICALLY YAI USE KARNA
 APDEGA 
FOR THAT WE ARE USING "JINJA.PY" THIS FILE
"""