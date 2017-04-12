from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key="wang0tang0zoopadoop"


@app.route('/')
def home():
    counter = 1
    if 'counter' in session:
        session['counter']=session['counter'] + 1
    else:
        session['counter'] = counter
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    session['counter']=session['counter'] + 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True, port=8888)
