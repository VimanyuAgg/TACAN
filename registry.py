from flask import Flask, jsonify, request, Response, json, Request
import redis


app = Flask(__name__)
redis_db = redis.StrictRedis(host="localhost", port=6379)


@app.route('/v1/retrieve', methods =['GET'])
def retrieve():
	return "hi"



@app.route('/v1/register', methods =['POST'])	
def register():
	return "hi"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')