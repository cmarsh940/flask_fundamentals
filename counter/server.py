from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')

def index():
    try:
        session['count'] += 1
    except:
        session['count'] = 0
    return render_template('index.html', count = session['count'])

@app.route('/plustwo')
def addTwo():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)