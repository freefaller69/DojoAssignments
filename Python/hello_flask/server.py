from flask import Flask, render_template, redirect, redirect, session, flash

app = Flask(__name__)
app.secret_key = "yabbadabbadoo"

@app.route('/')
def hello():
    if "users" not in session:
        session['users'] = []
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def addUser():
    user = {
    "first_name": request.form['fname'],
    "last_name": request.form['lname'],
    "email": request.form['email'],
    "id": request.form['count']
    }

    if len(user['first_name']) < 2:
        flash("First name must be longer than two characters")
    if len(user['last_name']) < 2:
        flash("Last name must be longer than two characters")

    if "_flashes" in session:
        return redirect ('/')

    session['user'] = user
    session['counter'] += 1
    print session['user']['first_name']
    session['users'].append(user)
    print session['users']
    return redirect('/')

@app.route('/user/<id>')
def showUser(id):
    for user in session['users']:
        if user['id'] == id:
            one_user = user
    return render_template('user.html', user=one_user)

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True, port=8888)
