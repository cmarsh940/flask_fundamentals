from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')

def index():
  return render_template('index.html')

@app.route('/success')

def success():
  return render_template('success.html')

@app.route('/success', methods=['POST'])

def submit():
   print "Got Post Info"
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
   # redirects back to the '/' route
   print request.form
   return render_template('success.html', name=name, location=location, language=language, comment=comment)
   return redirect('/success')

app.run(debug=True) # run our server
