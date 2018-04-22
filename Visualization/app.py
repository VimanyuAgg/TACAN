from flask import Flask, render_template, jsonify, request
import json
from threading import Thread
from time import sleep
# import pandas as pd

import sys, os
from os.path import dirname
_PARSE_LOGS_PATH = 'TACAN/Visualization/parse_logs'
project_home = dirname(dirname(sys.path[0]))
to_ins = os.path.join(project_home, _PARSE_LOGS_PATH)
# print to_ins
sys.path.insert(0, to_ins)
from parse_logs import parse


app = Flask(__name__)

globalCtr = 65

def createFile(tree):
	for _ in xrange(200):
		with open("./static/myflare.json", "w+") as fb:
			fb.write(json.dumps(tree))
			sleep(.2)
	return

@app.route("/")
def index():
	# parse()
	t = Thread(target=parse, args=())
	t.start()
	sleep(1)
	return render_template("index.html")

@app.route("/view")
def dashboard():
	return render_template("dashboard.html")


@app.route("/view/2")
def dashboard2():
	return render_template("dashboard2.html")

@app.route("/view/3")
def dashboard3():
	return render_template("dashboard3.html")

tree = 'foo'

@app.route("/update_data", methods=["POST"])
def updateTree():
	global tree
	content = request.data
	print ('content', type(content))
	print content
	tree = content
	print "updating"
	return 'OK'

@app.route("/data")
def data():
	global globalCtr

	## getMongoConnection and data as tree
	print "I am here"

	# tree = {"name": "a_root_node", "children": [{"name": "A", "children": []}, {"name": "C", "children": []}]}

	with open("./static/myflare.json", "w+") as fb:
		fb.write(tree)

	globalCtr += 1
	print globalCtr

	return jsonify({"result":"success"})



if __name__ == "__main__":
	app.run(debug=True)

	"""
	/Users/gurnoorsinghbhatia/Documents/code/cmpe295A/TACAN/Visualization/app.py
	"""