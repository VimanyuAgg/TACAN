from flask import Flask, render_template
import json
# import pandas as pd


app = Flask(__name__)

@app.route("/")
def index():
	tree = {"name": "a_root_node", "children": ["B", "C"]}
	obj = json.dumps(tree)
	return render_template("index.html", data = obj)


if __name__ == "__main__":
    app.run(debug=True)