from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re, datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*[^a-zA-Z])(?=.*[a-z])(?=.*[A-Z])\S{8,20}$')


app = Flask(__name__)
mysql = MySQLConnector(app,'users')
app.secret_key = 'ThisIsSecret'

print mysql.query_db('SELECT * FROM users.users')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/friends', methods=['POST'])
def create():
    return redirect('/')

@app.route('/users')
def users():
    query_all = 'SELECT * FROM users.users'
    all_users = mysql.query_db(query_all)
    return render_template('users.html', all_users = all_users)

@app.route('/user/<id>')
def showUser(id):
    one_user_query = "SELECT * FROM users.users WHERE id = :id"
    one_user_data = {
        "id": id
    }
    one_user = mysql.query_db(one_user_query, one_user_data)
    return render_template('user.html', user=one_user[0])

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

    # if birthdate > today:
    #     flash("Surely you can't be serious!")
    #
    # if len(request.form['email']) < 1:
    #     flash("Email is a required field.", 'error')
    # elif not EMAIL_REGEX.match(request.form['email']):
    #     flash("Invalid email address.", 'error')
    # if not PASSWORD_REGEX.match(request.form['pwd']):
    #     flash("Password must be between 8 and 20 characters in length and  include at least 1 uppercase letter, 1 lowercase letter, and 1 number.")
    # elif (request.form['pwd']) != (request.form['pwdConfirm']):
    #     flash("Password confirmation does not match.  Please reenter.")


    if "_flashes" in session:
        return redirect ('/')
    print request.form['fName']
    print request.form['lName']
    print request.form['email']
    print request.form['occupation']
    return redirect('/')



app.run(debug=True, port=8888)
