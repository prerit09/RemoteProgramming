import common
import requests
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if(request.method == "POST"):
        code = request.form['cpp_code']
        input = request.form['in']
        expected="Hello World!"

        out = common.result(code, input, expected)

        return render_template("index.html", usr=out)
    else:
        return render_template("index.html")

@app.route("/exercise-1", methods=["POST", "GET"])
def exercise_1():
    if(request.method == "POST"):
        code = request.form['cpp_code']
        input = request.form['in']
        expected="* \n* * \n* * * \n"

        out = common.result(code, input, expected)

        return render_template("exercises/exercise-1.html", usr=out)
    else:
        return render_template("exercises/exercise-1.html")
    
@app.route("/admin", methods=["POST", "GET"])
def admin():
    if(request.method == "POST"):
        code = request.form['cpp_code']
        input = request.form['in']
        expected = request.form['exp']   
        
        out = common.result(code, input, expected)

        return render_template("admin.html", usr=out)

    else:
        return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)