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

user_id = ""

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # Form Validations
    # First name and last name validations
    if not NAME_REGEX.match(request.form['fName']):
        flash("First name entry has non-alphabet characters.", 'registration_error')
    if not NAME_REGEX.match(request.form['lName']):
        flash("Last name entry has non-alphabet characters.", 'registration_error')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address.", 'registration_error')
    # Password validation
    if not PASSWORD_REGEX.match(request.form['new_pwd']):
        flash("Password must be between 8 and 20 characters in length and  include at least 1 uppercase letter, 1 lowercase letter, and 1 number.", 'registration_error')
    elif (request.form['new_pwd']) != (request.form['pwdConfirm']):
        flash("Password confirmation does not match.  Please reenter.", 'registration_error')
    # If errors, flash message(s) and return to registration
    if "_flashes" in session:
        return redirect ('/')
        # check if email already in database
    check_user_query = "SELECT email FROM users WHERE email = :email"
    check_user_data = {
        "email": request.form['email']
        }
    isUser = mysql.query_db(check_user_query, check_user_data)
    if not isUser:
        data = {
            'first_name': request.form['fName'],
            'last_name': request.form['lName'],
            'email': request.form['email'],
            'pw_hash': bcrypt.generate_password_hash(request.form['new_pwd'])
        }
        # submit data to database
        add_user_query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        newUserID = mysql.query_db(add_user_query, data)
        session['user'] = {
            "LoggedIn": True,
            "id": str(newUserID),
            'first_name': request.form['fName'],
            'last_name': request.form['lName'],
            'email': request.form['email'],
        }
        global user_id
        user_id = session['user']['id']
        flash("Registration successful", 'success')
        return redirect('/wall')
    else:
        flash("Registration information error.  Please verify and resubmit.", 'registration_error')
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
    if user and bcrypt.check_password_hash(user[0]['pw_hash'], password):
        session['user'] = {
            "LoggedIn": True,
            "id": unicode(user[0]['id']),
            "first_name": user[0]['first_name'],
            "last_name": user[0]['last_name'],
            "email": user[0]['email'],
        }
        global user_id
        user_id = session['user']['id']
        return redirect('/wall')
    else:
        flash("You shall not pass!!!", 'login_error')
    return redirect('/')

@app.route('/user/<id>')
def showUser(id):
    # if user not logged in, redirect to login/registration
    if not session:
        return redirect('/')
    # if user in session, url user edits return user to their own user page
    if unicode(session['user']['id']) != id:
        return redirect('/user/'+user_id)
    return render_template('user.html', user=user_id)

@app.route('/edit/<id>')
def edit(id):
    # if user not logged in, redirect to login/registration
    if not session:
        return redirect('/')
    # if user in session, url user edits return user to their own user page
    if unicode(session['user']['id']) != id:
        return redirect('/edit/'+user_id)
    return render_template('edit.html', user=user_id)

@app.route('/update', methods=['POST'])
def update():
    user_update_data = {
        'first_name': request.form['fName'],
        'last_name': request.form['lName'],
        'email': request.form['email'],
        'id': user_id
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
        return redirect('/edit/'+user_id)

    user_update_query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
    mysql.query_db(user_update_query, user_update_data)
    session['user'] = {
        "first_name": request.form['fName'],
        "last_name": request.form['lName'],
        "email": request.form['email'],
        "id": session['user']['id']
    }
    flash ("User successfully updated", 'success')
    return render_template('user.html', user=user_id)


@app.route('/confirm_delete')
def confirm_delete():
    flash("Confirm deletion", 'confirm_delete')
    if "_flashes" in session:
        return redirect('/user/'+user_id)

@app.route('/user/delete/<id>', methods=['POST'])
def delete(id):
    delete_query = "DELETE FROM users WHERE id = :id"
    delete_data = {
        'id': id
    }
    mysql.query_db(delete_query, delete_data)
    flash("User deleted.")
    return redirect('/')

@app.route('/wall')
def theWall():
    message_query = "SELECT messages.id as msg_id, message, messages.created_at, message_id, users.first_name, users.last_name FROM messages JOIN users on users.id = user_id LEFT JOIN comments ON messages.id = message_id GROUP BY message_id ORDER BY messages.created_at DESC"

    user_messages = mysql.query_db(message_query)

    user_comment_query = "SELECT user_comment, comments.created_at, users.first_name, users.last_name, message_id FROM comments JOIN users ON users.id = user_id ORDER BY comments.created_at"
    user_comments = mysql.query_db(user_comment_query)
    if len(user_messages) == 0:
        return render_template('/wall.html')
    else:
        return render_template('/wall.html', user_messages=user_messages, user_comments=user_comments)

@app.route('/wall/message', methods=['POST'])
def post_message():
    new_message_data = {
        'message': request.form['message'],
        'user_id': user_id
    }
    if len(new_message_data['message']) < 2:
        flash("Minimum message length is 2 characters.  Hi!  Please resubmit.", 'message_error')
    else:
        new_message_query = "INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW())"
        mysql.query_db(new_message_query, new_message_data)
    return redirect('/wall')

@app.route('/wall/message/comment/<msg_id>', methods=['POST'])
def post_comment(msg_id):
    new_comment_data = {
        'comment': request.form['comment'],
        'user_id': user_id,
        'message_id': msg_id
    }
    if len(new_comment_data['comment']) > 1:
        new_comment_query = "INSERT INTO comments (user_comment, user_id, message_id, created_at, updated_at) VALUES (:comment, :user_id, :message_id, NOW(), NOW())"
        mysql.query_db(new_comment_query, new_comment_data)
    return redirect('/wall')

# @app.route('/confirm_msg_delete/<msg_id>')
# def confirm_msg_delete(msg_id):
#     flash("Confirm deletion", 'confirm_delete/<msg_id>')
#     if "_flashes" in session:
#         return redirect('/wall')

@app.route('/allusers')
def allusers():
    query_all = ('SELECT * FROM users')
    all_users = mysql.query_db(query_all)
    return render_template('allusers.html', all_users=all_users)

@app.route('/logout')
def logout():
    session.clear()
    print "User ID:",user_id
    return redirect('/')

app.run(debug=True, port=8888)
