from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')

def index():
  return render_template('index.html')

@app.route('/users')

def users():
  return render_template('users.html')

@app.route('/users', methods=['POST'])

def your_name():
   print "Got Post Info"
   name = request.form['name']
   # redirects back to the '/' route
   print request.form
   return render_template('users.html', name=name)
   return redirect('/users')

app.run(debug=True) # run our server
