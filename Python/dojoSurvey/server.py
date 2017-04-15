from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['POST'])
def dojo_survey():
    print "Got Post Info"
    if len(request.form['name']) < 1:
        flash("Name cannot be empty.")
    if len(request.form['location']) < 1:
        flash("Select a location.")
    if len(request.form['language']) < 1:
        flash("Select a favorite language. It's ok if it's something other than Python.")
    if len(request.form['comments']) > 120:
        flash("Comments are limited to 120 characters.")

    if "_flashes" in session:
        return redirect ('/')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/show')

@app.route('/show')
def show_response():
    return render_template('response.html')




app.run(debug=True, port=8888)
