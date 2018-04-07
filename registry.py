from flask import Flask, jsonify, request, Response, json, Request
import redis

app = Flask(__name__)
redis_db = redis.StrictRedis(host="localhost", port=6379)


@app.route('/v1/retrieve/<string:key>', methods=['GET'])
def retrieve(key):
  return redis_db.get(key)


@app.route('/v1/register', methods=['POST'])
def register():
  r = request.get_json()
  if r is not None:
    key = r["nodeId"]
    val = r["IP"]
    redis_db.set(key, val)
    return "OK"
  else:
    return "failed"


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
