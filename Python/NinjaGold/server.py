from flask import Flask, render_template, request, redirect, session, flash
import random, datetime, time

app = Flask(__name__)
app.secret_key="wang0tang0zoopadoop"

@app.route('/')
def home():
    if 'gold' not in session:
        session['gold'] = 0
    if 'actions' not in session:
        session['actions'] = []
    else:
        print session['actions']
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    choice = request.form['action']
    if choice == 'farm':
        start = 10
        stop = 21
    if choice == 'cave':
        start = 5
        stop = 11
    if choice == 'house':
        start = 2
        stop = 6
    if choice == 'casino':
        start = -50
        stop = 51
    goldThisRound = random.randrange(start, stop)
    session['gold'] += goldThisRound
    session['place'] = choice
    place = choice

    today = datetime.datetime.today()

    action = {
        "goldThisRound": goldThisRound,
        "place": choice,
        "stamp": today
    }
    session['actions'].append(action)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True, port=8888)
