from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    expression = ""
    if request.method == "POST":
        expression = request.form["expression"]
        try:
            result = eval(expression, {
                "sqrt": math.sqrt,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "log": math.log10,
                "ln": math.log,
                "pi": math.pi,
                "e": math.e
            })
        except:
            result = "Error"

    return render_template("index.html", result=result, expression=expression)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
