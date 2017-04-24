from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re, datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*[^a-zA-Z])(?=.*[a-z])(?=.*[A-Z])\S{8,20}$')


app = Flask(__name__)
mysql = MySQLConnector(app,'emaildb')
app.secret_key = 'ThisIsSecret'

print mysql.query_db('SELECT * FROM addresses')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def users():
    query_all = 'SELECT * FROM addresses'
    addresses = mysql.query_db(query_all)
    return render_template('success.html', addresses = addresses)

@app.route('/register', methods=['POST'])
def registration():
    if len(request.form['email']) < 1:
        flash("Email is a required field.", 'error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address.", 'error')

    if "_flashes" in session:
            return redirect ('/')

    email_query = "INSERT INTO addresses (email_address, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    data = {
        'email': request.form['email'],
    }
    mysql.query_db(email_query, data)
    flash("The email address you entered, " + str(data['email']) + ", is a VALID email address!  Thank you!")
    return redirect('/success')

@app.route('/remove_address/<id>', methods=['POST'])
def delete(id):
    delete_query = "DELETE FROM addresses WHERE id = :id"
    data = {
        'id': id
    }
    mysql.query_db(delete_query, data)
    return redirect('/success')


app.run(debug=True, port=8888)
