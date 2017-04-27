from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re, datetime
NAME_REGEX = re.compile(r'^[_A-Za-z\'-]{2,}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]{5,}$')
PASSWORD_REGEX = re.compile(r'^(?=.*[^a-zA-Z])(?=.*[a-z])(?=.*[A-Z])\S{8,20}$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'userssecuredb')
app.secret_key = 'AHighlySecureSecret'

print mysql.query_db('SELECT * FROM users')

@app.route('/', methods=['GET'])
def index():
    # query_all = ('SELECT * FROM users')
    # all_users = mysql.query_db(query_all)
    # return render_template('index.html', all_users=all_users)
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # Form Validations
    # First name and last name validations
    if not NAME_REGEX.match(request.form['fName']):
        flash("Please review your first name entry for non-alphabet characters.", 'registration_error')
    if not NAME_REGEX.match(request.form['lName']):
        flash("Please review your last name entry for non-alphabet characters.", 'registration_error')
    # email validation
    if len(request.form['email']) < 5:
        flash("Email cannot be empty.", 'registration_error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address.", 'error')
    # Password validation
    if not PASSWORD_REGEX.match(request.form['new_pwd']):
        flash("Password must be between 8 and 20 characters in length and  include at least 1 uppercase letter, 1 lowercase letter, and 1 number.", 'registration_error')
    elif (request.form['new_pwd']) != (request.form['pwdConfirm']):
        flash("Password confirmation does not match.  Please reenter.", 'registration_error')
    # If errors, flash message(s) and return to registration
    if "_flashes" in session:
        return redirect ('/')

    check_user_query = "SELECT email FROM users WHERE email = :email"
    check_user_data = {
        "email" : user['email']
        }
    isUser = mysql.query_db(check_user_query, check_user_data)
    if not  isUser[0]:
        add_user_query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        data = {
            'first_name': request.form['fName'],
            'last_name': request.form['lName'],
            'email': request.form['email'],
            'password': request.form['new_pwd'],
            'pw_hash': bcrypt.generate_password_hash(password)
        }
        print data['pw_hash']
        mysql.query_db(add_user_query, data)
        return redirect('/user/'+str(user[0]['id']))
    # return redirect('/')
    else:
        flash("Error with email, please select another email.")
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['pwd']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = {
        'email': email
    }
    user = mysql.query_db(user_query, query_data)
    if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        # redirect goes here
        flash("Password is GOOD!")
        return redirect('/user/'+str(user[0]['id']))
    else:
        flash("You shall not pass!!!")
        return redirect('/')

@app.route('/user/<id>')
def showUser(id):
    user_query = "SELECT * FROM users WHERE id = :id"
    user_data = {
        "id": id
    }
    user = mysql.query_db(user_query, user_data)
    return render_template('user.html', user=user[0])

@app.route('/user/edit/<id>', methods=['POST'])
def update(id):
    user_update_query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, WHERE id = :id"
    user_update_data = {
        'first_name': request.form['fName'],
        'last_name': request.form['lName'],
        'email': request.form['email'],
        'id': id
    }
    print "update query: ", user_update_query
    print "update data: ", user_update_data
    mysql.query_db(user_update_query, user_update_data)
    return redirect('/')

@app.route('/user/delete/<id>', methods=['POST'])
def delete(id):
    delete_query = "DELETE FROM users WHERE id = :id"
    delete_data = {
        'id': id
    }
    mysql.query_db(delete_query, delete_data)
    return redirect('/')

app.run(debug=True, port=8888)
