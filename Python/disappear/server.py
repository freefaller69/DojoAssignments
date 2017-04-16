from flask import Flask, render_template

app = Flask(__name__)
app.secret_key="wang0tang0zoopadoop"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja/')
@app.route('/ninja/<turtle>')
def show_ninja(turtle=None):
    if turtle == None:
        return render_template('/ninja.html', turtle=turtle)
    if turtle.lower() == 'leonardo' or turtle == 'michelangelo' or turtle == 'raphael' or turtle == 'donatello':
        return render_template('/ninja.html', turtle=turtle)
    return render_template('/ninja.html', turtle='notapril')




app.run(debug=True, port=8888)
