from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')

def index():
  return render_template('index.html')

@app.route('/user')

def user():
  return render_template('user.html')

@app.route('/user', methods=['POST'])

def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   email = request.form['email']
   # redirects back to the '/' route
   print request.form
   return render_template(name)
   return redirect('/user')

app.run(debug=True) # run our server
