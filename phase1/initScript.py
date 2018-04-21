from Node import Node
from threading import Thread
import time
import traceback

from pymongo import MongoClient
import os
import datetime
import logging.handlers
import spanningtreepopulate

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

today_date = str(datetime.datetime.now()).split(" ")[0]
current_path = os.path.dirname(os.path.realpath(__file__))


debug_handler = logging.handlers.RotatingFileHandler(os.path.join(current_path+"/logs/", today_date+'-debug.log'),maxBytes=30000000,backupCount=40)
debug_handler.setLevel(logging.DEBUG)

info_handler = logging.handlers.RotatingFileHandler(os.path.join(current_path+"/logs/", today_date+'-info.log'),maxBytes=30000000,backupCount=40)
info_handler.setLevel(logging.INFO)

error_handler = logging.handlers.RotatingFileHandler(os.path.join(current_path+"/logs/", today_date+'-error.log'),maxBytes=300000,backupCount=40)
error_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)
debug_handler.setFormatter(formatter)

logger.addHandler(info_handler)
logger.addHandler(error_handler)
logger.addHandler(debug_handler)

con = MongoClient("mongodb://localhost:27017/spanningtreemap")
db = con.spanningtreemap

def cleanDB():
	try:
		db.spanningtree.remove({})
		logger.info("Cleaning DB if it exists")
	except Exception as e:
		logger.error(e)
		logger.error(traceback.format_exc())

def buildDB():
	logger.info("Creating New DB")
	spanningtreepopulate.populateTree()

def spawnNode(id):
	return Node(id)

if __name__ == '__main__':
	threadPool= []
	logger.info("Cleaning DB if it exists")
	for i in range(0,12):
		thread = Thread(target=spawnNode, args=(str(i),))
		threadPool.append(thread)

	for thread in threadPool:
		thread.start()
		time.sleep(2)



