from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re, datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*[^a-zA-Z])(?=.*[a-z])(?=.*[A-Z])\S{8,20}$')

app = Flask(__name__)
mysql = MySQLConnector(app,'userssecuredb')
app.secret_key = 'AHighlySecureSecret'

print mysql.query_db('SELECT * FROM users')

@app.route('/')
def index():
    query_all = ('SELECT * FROM users')
    all_users = mysql.query_db(query_all)
    return render_template('index.html', all_users=all_users)

@app.route('/register', methods=['POST'])
def register():
    add_user_query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data = {
        'first_name': request.form['fName'],
        'last_name': request.form['lName'],
        'email': request.form['email'],
    }
    mysql.query_db(add_user_query, data)
    return redirect('/')

@app.route('/user/<id>')
def showUser(id):
    user_query = "SELECT * FROM users WHERE id = :id"
    user_data = {
        "id": id
    }
    user = mysql.query_db(user_query, user_data)
    return render_template('edit.html', user=user[0])

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
