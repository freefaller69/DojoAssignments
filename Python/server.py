from flask import flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key="wang0tang0zoopadoop"

@app.route('/')
def home():
    return render_template('index.html')





app.run(debug=True, port=8888)
