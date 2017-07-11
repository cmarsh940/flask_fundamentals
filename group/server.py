from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')

def index():
  return render_template('index.html')

@app.route('/haha')

def haha():
  return render_template('haha.html')

@app.route('/success')

def success():
  return render_template('success.html')

@app.route('/next')

def next():
  return render_template('next.html')

@app.route('/end')

def end():
  return render_template('end.html')

app.run(debug=True) # run our server
