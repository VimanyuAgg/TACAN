from flask import Flask, render_template
import json
# import pandas as pd


app = Flask(__name__)

@app.route("/")
def index():
	tree = {"name": "a_root_node", "children": ["B", "C"]}
	obj = json.dumps(tree)
	return render_template("index.html", data = obj)

@app.route("/view")
def dashboard():
	return render_template("dashboard.html")


@app.route("/view/2")
def dashboard2():
	return render_template("dashboard2.html")

@app.route("/view/3")
def dashboard3():
	return render_template("dashboard3.html")


if __name__ == "__main__":
	app.run(debug=True)