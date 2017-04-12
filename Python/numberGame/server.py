from flask import Flask, render_template, request, redirect, session, flash
import random

app = Flask(__name__)
app.secret_key="wang0tang0zoopadoop"

@app.route('/')
def home():
    if 'number' in session:
        pass
    else:
        session['number']=random.randrange(0, 101)
        print session['number']
    return render_template('index.html')

@app.route('/', methods=['POST'])
def guess():
    if len(request.form['guess']) < 1:
        flash("Please enter a number between 1 and 100.", 'error')
        return redirect('/')
    session['guess'] = request.form['guess']
    guess = int(session['guess'])
    number = int(session['number'])
    if guess < 1 or guess > 100:
        flash("Please enter a number between 1 and 100.", 'error')
        return redirect('/')
    if guess == number:
        flash(str(number) + " was the number!", 'yep')
        return redirect('/')
    if guess < number:
        flash("Too low.", 'nope')
        return redirect('/')
    elif guess > number:
        flash("Too high.", 'nope')
        return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True, port=8888)
