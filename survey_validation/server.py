from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'Secret'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/success')
def success():
  return render_template("success.html")

@app.route('/submit', methods=['POST'])
def createuser():
    invalid = False
    if len(request.form['name']) < 1:
        flash("name must be entered!")
        invalid = True

    if request.form['name'].isalpha() == False:
        flash("name must not contain any numbers.")
        invalid = True

    if len(request.form['comment']) < 1 and len(request.form['comment']) < 120:
        flash("Comment must be entered!")
        invalid = True

    if invalid:
        return redirect('/')

    else:
        flash("Thank you for submitting")
        return redirect('/')

app.run(debug=True)