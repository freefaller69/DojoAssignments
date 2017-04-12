from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def landingPage():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    session['first'] = request.form['first']
    session['last'] = request.form['last']
    session['email'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('user.html')
    # return render_template('user.html', first=session['first'], last=session['last'], email=session['email'])


# @app.route('/ninjas')
# def ninjas():
#     return render_template('ninjas.html')
#
# @app.route('/dojos/new')
# def new():
#     return render_template('dojos.html')


app.run(debug=True, port=8888)
