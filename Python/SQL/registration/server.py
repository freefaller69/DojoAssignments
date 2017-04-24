from flask import Flask, render_template, request, redirect, session, flash
from MySQLConnection import MySQLConnector
import re, datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*[^a-zA-Z])(?=.*[a-z])(?=.*[A-Z])\S{8,20}$')


app = Flask(__name__)
mysql = MySQLConnector(app,'usersdb')
app.secret_key = 'ThisIsSecret'

print mysql.query_db('SELECT * FROM users')

app.route()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def registration():
    today = datetime.date.today()
    birthdate = datetime.datetime.strptime(request.form['birthdate'], '%Y-%m-%d').date()
    print "Got Post Info"
    if len(request.form['fName']) < 1:
        flash("First name cannot be empty.", 'error')
    elif not (request.form['fName'].isalpha()):
        flash("First name must be letters only.", 'error')
    if len(request.form['lName']) < 1:
        flash("Last name cannot be empty.", 'error')
    elif not (request.form['lName'].isalpha()):
        flash("Last name must be letters only.", 'error')

    if birthdate > today:
        flash("Surely you can't be serious!")

    if len(request.form['email']) < 1:
        flash("Email is a required field.", 'error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address.", 'error')
    if not PASSWORD_REGEX.match(request.form['pwd']):
        flash("Password must be between 8 and 20 characters in length and  include at least 1 uppercase letter, 1 lowercase letter, and 1 number.")
    elif (request.form['pwd']) != (request.form['pwdConfirm']):
        flash("Password confirmation does not match.  Please reenter.")


    if "_flashes" in session:
        return redirect ('/')
    session['fName'] = request.form['fName']
    session['lName'] = request.form['lName']
    session['birthdate'] = request.form['birthdate']
    session['email'] = request.form['email']
    session['pwd'] = request.form['pwd']
    flash("Thanks for submitting your information.")
    return redirect('/')



app.run(debug=True, port=8888)
