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
                    return redirect(url_for('dashboard'))
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

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        return redirect(url_for('gqr'))
        gqr()
    return render_template("dashboard.html")
    

@app.route('/gqr', methods=['GET', 'POST'])
def gqr():
    return render_template("gqr.html")



def randomString(stringLength=20):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

qrcode =''
def generateqrcode(qrcode):
    student = mydb.cursor()
    qrcode = randomString(20)
    today = date.today()
    sql = "INSERT INTO Session (date, ID_Code) VALUES (%s, %s)"
    val = (today, qrcode)
    execute(sql, val)
    mydb.commit()

@app.route('/api/student', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json()
    qrcoderecived = req_data['qrcodesent']
    if qrcoderecived == qrcode :
        return 'Present'
    else :
        return 'Error'
