from app import app
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import random
import string
from datetime import date

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="y@cine2012",
  database="esisba_login"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT username FROM teachers")

usernames = mycursor.fetchone()
loggedin = False
@app.route('/', methods=['GET', 'POST'])
def login_view():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        username = request.form.get('username')
        password = request.form['password']
        for x in usernames:
            if username == x :
                mycursor.execute("SELECT Password FROM teachers WHERE username ='{}'".format(x))
                passwords = mycursor.fetchone()[0]
                if password == passwords:
                    loggedin = True
                    return dashboard()
                else:
                    return '''<h1>username is: {}</h1>
                            <h1>password is: {}</h1>
                            <h6>from database</h6>
                            <h2>username: {}</h2>
                            <h2>password: {}</h2>'''.format(username, password,x,passwords)
            else:
                return '''<h1>username is: {}</h1>
                            <h1>password is: {}</h1>
                            <h6>from database</h6>
                            <h2>username: {}</h2>'''.format(username, password,x)
    return render_template("index.html") 

@app.route('/dashboard/', methods=['GET', 'POST'])
def dashboard():
    if loggedin == True:
        return render_template("dashboard.html")
    else:
        login_view()

    if request.method == 'POST':
        generateqrcode()
        gqr()

@app.route('/gqr/', methods=['GET', 'POST'])
def gqr():
    if loggedin == True:
        return render_template("gqr.html")
    else:
        login_view()



def randomString(stringLength=20):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
def generateqrcode()
    student = mydb.cursor()
    qrcode = randomString(20)
    today = date.today()
    sql = "INSERT INTO Session (date, ID_Code) VALUES (%s, %s)"
    val = (today, qrcode)
    execute(sql, val)
    mydb.commit()