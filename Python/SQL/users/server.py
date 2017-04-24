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
    add_user_query = "INSERT INTO users (first_name, last_name, email, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :email, :occupation, NOW(), NOW())"
    data = {
        'first_name': request.form['fName'],
        'last_name': request.form['lName'],
        'email': request.form['email'],
        'occupation': request.form['occupation'],
    }
    mysql.query_db(add_user_query, data)
    return redirect('/')

@app.route('/remove_user/<id>', methods=['POST'])
def delete(id):
    delete_query = "DELETE FROM users WHERE id = :id"
    data = {
        'id': id
    }
    mysql.query_db(delete_query, data)
    return redirect('/')


app.run(debug=True, port=8888)
