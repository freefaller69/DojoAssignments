from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['POST'])
def dojo_survey():
    print "Got Post Info"
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/show')

    # return render_template('response.html', name=name, location=location, language=language, comments=comments)


@app.route('/show')
def show_response():
    return render_template('response.html')
#
    # return render_template('response.html', name=session['name'], location=session['location'], language=session['language'], comments=session['comments'])


app.run(debug=True, port=8888)
