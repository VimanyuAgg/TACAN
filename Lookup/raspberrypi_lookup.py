import lookup_server
import redis

class RaspberryPi:

	def __init__(self):
		print "isnide rasp init"
		redis_db = redis.StrictRedis(host="localhost", port=6379)
		print "redis connection created"
		lookup_server.serve(self)
		print "look up started"

	def retrieve(key):
		return redis_db.get(key)

	def register(key, val):
		if key and val is not None:
			redis_db.set(key, val)
			return "Okay"
		else:
			return "Not registered"
