import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "myLittleSecret"

def sessionNumberInit():
    if 'number' not in session:
        session["number"] = random.randrange(0, 101)


@app.route("/")
def init():
    sessionNumberInit()
    return render_template("index.html")



@app.route("/submitted", methods = ["POST"])
def submitted():
    try:
        if int(request.form["num"]) < session["number"]:
            return render_template("index.html", output = "Too low! Session number: " + str(session["number"]) + " Your answer: " + request.form["num"])
        elif int(request.form["num"]) > session["number"]:
            return render_template("index.html", output = "Too high! Session number: " + str(session["number"]) + " Your answer: " + request.form["num"])
        else:
            return render_template("index.html", output = str(session["number"]) + " was the number!")
    except:
        return render_template("index.html", output = "Not a number! Try again!")

@app.route("/reset")
def reset():
    session["number"] = random.randrange(0, 101)
    return redirect("/")

app.run(debug=True)