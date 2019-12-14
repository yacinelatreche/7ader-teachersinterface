from app import app
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

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
                    return render_template("dashboard.html")
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