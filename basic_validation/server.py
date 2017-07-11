from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'Secret'
@app.route('/')
def index():
  return render_template('index.html')
@app.route('/process', methods=['Post'])
def process():
  if len(request.form['name'])< 1:
    flash("Name cannot be empty!")    #display validation errors
  else:
    flash("Success! Your name is {}".format(request.form['name']))# display success message
  return redirect('/')
app.run(debug=True)