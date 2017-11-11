from flask import Flask, jsonify, request, Response, json, Request
import redis


app = Flask(__name__)
redis_db = redis.StrictRedis(host="localhost", port=6379)
redis_db.set('ip','bhushan')


@app.route('/v1/retrieve/<string:key>', methods =['GET'])
def retrieve(key):
	return redis_db.get(key)



# @app.route('/v1/register', methods =['POST'])	
# def register():
# 	r = request['data']
# 	return "hi"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')