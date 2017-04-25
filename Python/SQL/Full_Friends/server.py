from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re, datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*[^a-zA-Z])(?=.*[a-z])(?=.*[A-Z])\S{8,20}$')

app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriendsdb')
app.secret_key = 'AHighlySecureSecret'

print mysql.query_db('SELECT * FROM friends')

@app.route('/')
def index():
    query_all = ('SELECT * FROM friends')
    all_friends = mysql.query_db(query_all)
    return render_template('index.html', all_friends=all_friends)

@app.route('/friends', methods=['POST'])
def friends():
    if len(request.form['fName']) < 1:
        flash("First name cannot be empty.", 'error')
    elif not (request.form['fName'].isalpha()):
        flash("First name must be letters only.", 'error')
    if len(request.form['lName']) < 1:
        flash("Last name cannot be empty.", 'error')
    elif not (request.form['lName'].isalpha()):
        flash("Last name must be letters only.", 'error')
    if len(request.form['email']) < 1:
        flash("Email is a required field.", 'error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address.", 'error')
    if "_flashes" in session:
        return redirect ('/')
    add_friend_query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data = {
        'first_name': request.form['fName'],
        'last_name': request.form['lName'],
        'email': request.form['email'],
    }
    flash ("User added")
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
    # if len(request.form['fName']) < 1:
    #     flash("First name cannot be empty.", 'error')
    # elif not (request.form['fName'].isalpha()):
    #     flash("First name must be letters only.", 'error')
    # if len(request.form['lName']) < 1:
    #     flash("Last name cannot be empty.", 'error')
    # elif not (request.form['lName'].isalpha()):
    #     flash("Last name must be letters only.", 'error')
    # if len(request.form['email']) < 1:
    #     flash("Email is a required field.", 'error')
    # elif not EMAIL_REGEX.match(request.form['email']):
    #     flash("Invalid email address.", 'error')
    # if "_flashes" in session:
    #     return render_template('/friend/edit/<id>.html', id=id)

    update_query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = now() WHERE id = :id"
    update_data = {
        'first_name': request.form['fName'],
        'last_name': request.form['lName'],
        'email': request.form['email'],
        'id': id
    }
    print "update query: ", update_query
    print "update data: ", update_data
    mysql.query_db(update_query, update_data)
    flash ("User updated")
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
