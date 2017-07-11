from flask import Flask, render_template, request, redirect, flash
from datetime import datetime
import re
app = Flask(__name__)
app.secret_key = 'This is secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/submit', methods=['POST'])
def createuser():
    invalid = False
    if len(request.form['firstname']) < 1:
        flash("First name must be entered!")
        invalid = True

    if len(request.form['lastname']) < 1:
        flash("Last name must be entered!")
        invalid = True

    if request.form['firstname'].isalpha() == False or request.form['lastname'].isalpha() == False:
        flash("First and Last name must not contain any numbers.")
        invalid = True

    if len(request.form['email']) < 1:
        flash("Email must be entered!")
        invalid = True

    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address!')
        invalid = True

    if len(request.form['password']) < 1:
        flash("Password must be entered!")
        invalid = True

    if len(request.form['password']) < 8:
        flash("Password should be at least 8 characters")
        invalid = True

    countint = 0
    for i in request.form['password']:
        if i.isnumeric() == True:
            countint += 1

    if countint == 0:
        flash("Your password must have at least 1 number!")
        invalid = True

    countupper = 0
    for i in request.form['password']:
        if i.isupper() == True:
            countupper += 1

    if countupper == 0:
        flash("Your password must have at least 1 uppercase character!")
        invalid = True

    if len(request.form['pwconfirm']) < 1:
        flash("You must confirm your password!")
        invalid = True

    if request.form['password'] != request.form['pwconfirm']:
        flash("Password and password confirm should match!")
        invalid = True

    birthdate = datetime.strptime(request.form['bday'],'%Y-%m-%d')
    if birthdate >= datetime(2017,06,18):
        flash("Birthdate must be in the past!")
        invalid = True

    if invalid:
        return redirect('/')

    else:
        flash("Thanks for submitting your information.")
        return redirect('/')

app.run(debug=True)