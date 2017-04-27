from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re, datetime
NAME_REGEX = re.compile(r'^[_A-Za-z\'-]{2,}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*[^a-zA-Z])(?=.*[a-z])(?=.*[A-Z])\S{8,20}$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'userssecuredb')
app.secret_key = 'AHighlySecureSecret'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if len(request.form['new_pwd']) < 1:
        flash("Please enter a password between 8 and 20 characters in length which includes at least 1 uppercase letter, 1 lowercase letter, and 1 number.", 'registration_error')
        return redirect('/')
    data = {
        'first_name': request.form['fName'],
        'last_name': request.form['lName'],
        'email': request.form['email'],
        'pw_hash': bcrypt.generate_password_hash(str(request.form['new_pwd']))
    }
    # Form Validations
    # First name and last name validations
    if not NAME_REGEX.match(data['first_name']):
        flash("First name entry has non-alphabet characters.", 'registration_error')
    if not NAME_REGEX.match(data['last_name']):
        flash("Last name entry has non-alphabet characters.", 'registration_error')
    if not EMAIL_REGEX.match(data['email']):
        flash("Invalid email address.", 'registration_error')
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
        "email": data['email']
        }
    print "isUser:",check_user_data
    isUser = mysql.query_db(check_user_query, check_user_data)
    if not isUser:
        add_user_query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        print data['pw_hash']
        mysql.query_db(add_user_query, data)
        flash("Registration successful", 'success')
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        query_data = {
            'email': data['email']
        }
        user = mysql.query_db(user_query, query_data)

        # session['id'] = user['id']

        return redirect('/user/'+str(user[0]['id']))
    # return redirect('/')
    else:
        flash("Error with email, please verify and reenter.", 'registration_error')
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    if len(request.form['email']) < 1:
        return redirect('/')
    email = request.form['email']
    password = request.form['pwd']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = {
        'email': email
    }
    user = mysql.query_db(user_query, query_data)
    if not user:
        flash("You shall not pass!!!", 'login_error')
        return redirect('/')
    if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        # redirect goes here
        session['id'] = str(user[0]['id'])
        return redirect('/user/'+str(user[0]['id']))
    else:
        flash("You shall not pass!!!", 'login_error')
    return redirect('/')

@app.route('/user/<id>')
def showUser(id):
    # if user not logged in, redirect to login/registration
    if not session:
        return redirect('/')
    # if user in session, url user edits return user to their own user page
    if session['id'] != id:
        return redirect('/user/'+(session['id']))
    user_query = "SELECT * FROM users WHERE id = :id"
    user_data = {
        "id": id
    }
    user = mysql.query_db(user_query, user_data)
    return render_template('user.html', user=user[0])

@app.route('/edit/<id>')
def edit(id):
    # if user not logged in, redirect to login/registration
    if not session:
        return redirect('/')
    # if user in session, url user edits return user to their own user page
    if session['id'] != id:
        return redirect('/edit/'+(session['id']))
    # user = session['id']
    user_query = "SELECT first_name, last_name, email FROM users WHERE id = :id"
    user_data = {
    "id": id
    }
    user = mysql.query_db(user_query, user_data)
    print user
    return render_template('edit.html', user=user[0])
    # return redirect('/edit/'+(session['id']))

@app.route('/update', methods=['POST'])
def update():
    user_update_data = {
        'first_name': request.form['fName'],
        'last_name': request.form['lName'],
        'email': request.form['email'],
        'id': session['id']
    }
    # Form Validations
    # First name and last name validations
    if not NAME_REGEX.match(user_update_data['first_name']):
        flash("First name entry has non-alphabet characters.", 'registration_error')
    if not NAME_REGEX.match(user_update_data['last_name']):
        flash("Last name entry has non-alphabet characters.", 'registration_error')
    if not EMAIL_REGEX.match(user_update_data['email']):
        flash("Invalid email address.", 'registration_error')
    # Password validation
    # If errors, flash message(s) and return to registration
    if "_flashes" in session:
        return redirect('/edit/'+(session['id']))

    user_update_query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
    mysql.query_db(user_update_query, user_update_data)
    flash ("User successfully updated", 'success')
    return redirect('/user/'+(session['id']))


@app.route('/confirm_delete')
def confirm_delete():
    flash("Confirm deletion", 'confirm_delete')
    if "_flashes" in session:
        return redirect('/user/'+(session['id']))

@app.route('/cancel')
def cancel():
    return redirect('/user/'+(session['id']))

@app.route('/user/delete/<id>', methods=['POST'])
def delete(id):
    delete_query = "DELETE FROM users WHERE id = :id"
    delete_data = {
        'id': id
    }
    mysql.query_db(delete_query, delete_data)
    flash("User deleted.")
    return redirect('/')

@app.route('/allusers')
def allusers():
    query_all = ('SELECT * FROM users')
    all_users = mysql.query_db(query_all)
    return render_template('allusers.html', all_users=all_users)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True, port=8888)
