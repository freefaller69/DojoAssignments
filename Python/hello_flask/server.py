from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Michael"
    age = 48
    return render_template('index.html', name=name, age=age)

@app.route('/numbers')
def numbers():
    for number in range(3):
        print "We're in number"
    return redirect('/')

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True, port=8888)
