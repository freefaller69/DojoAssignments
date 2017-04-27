from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re, datetime
NAME_REGEX = re.compile(r'^[_A-Za-z\'-]{2,}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriendsdb')
app.secret_key = 'AHighlySecureSecret'

@app.route('/')
def index():
    query_all = ('SELECT * FROM friends')
    all_friends = mysql.query_db(query_all)
    return render_template('index.html', all_friends=all_friends)

@app.route('/friends', methods=['POST'])
def friends():
    if not NAME_REGEX.match(request.form['fName']):
        flash("First name entry has non-alphabet characters.", 'registration_error')
    if not NAME_REGEX.match(request.form['lName']):
        flash("Last name entry has non-alphabet characters.", 'registration_error')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address.", 'registration_error')
    if "_flashes" in session:
        return redirect ('/')
    add_friend_query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data = {
        'first_name': request.form['fName'],
        'last_name': request.form['lName'],
        'email': request.form['email'],
    }
    flash ("User successfully added", 'success')
    mysql.query_db(add_friend_query, data)
    return redirect('/')

@app.route('/friend/<id>')
def showFriend(id):
    friend_query = "SELECT * FROM friends WHERE id = :id"
    friend_data = {
        "id": id
    }
    friend = mysql.query_db(friend_query, friend_data)
    return render_template('edit.html', friend=friend[0])

@app.route('/friend/edit/<id>', methods=['POST'])
def update(id):
    if not NAME_REGEX.match(request.form['fName']):
        flash("Please review your first name entry for non-alphabet characters.", 'registration_error')
    if not NAME_REGEX.match(request.form['lName']):
        flash("Please review your last name entry for non-alphabet characters.", 'registration_error')
    if len(request.form['email']) < 5:
        flash("Email cannot be empty.", 'registration_error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address.", 'error')

    if "_flashes" in session:
        return redirect('/friend/'+id)


    update_query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = now() WHERE id = :id"
    update_data = {
        'first_name': request.form['fName'],
        'last_name': request.form['lName'],
        'email': request.form['email'],
        'id': id
    }
    mysql.query_db(update_query, update_data)
    flash ("User successfully updated", 'success')
    return redirect('/')

@app.route('/friend/delete/<id>', methods=['POST'])
def delete(id):
    delete_query = "DELETE FROM friends WHERE id = :id"
    delete_data = {
        'id': id
    }
    mysql.query_db(delete_query, delete_data)
    return redirect('/')

app.run(debug=True, port=8888)
