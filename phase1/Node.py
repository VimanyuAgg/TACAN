import weightMatrix
from spanning_tree import SPANNING_INFO
import raspberryPi_id_list
import main_server
import client

import logging
import os
import logging.handlers
import datetime
import thread

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

class Node:
	'''
	Node class representing each node in the network
	'''
	def __init__(self,myId):
		logger.info("Initializing Node: "+str(myId))
		self.id = myId
		#self.parentId = parentId
		#self.childListId = childListId
		my_info = SPANNING_INFO[myId]
		self.ipAddress= raspberryPi_id_list.ID_IP_MAPPING[myId]
		print self.ipAddress
		self.parentId = my_info['parentId']
		self.childListId = my_info['childListId']
		self.dist = my_info['dist']
		self.clusterheadId = my_info['clusterheadId']
		self.subtreeList = my_info['subtreeList']
		self.neighbourList = my_info['neighbourList']
		print "Calling weightMatrix for id: "+str(self.id)
		logger.info("Calling weightMatrix for id: "+str(self.id))
		self.weight = weightMatrix.getWeight(self.id)
		self.size = self.weight
		self.childRequestCounter = 0
		# self.childWeight = self.getChildWeight()
		self.isClusterhead = my_info['isClusterhead']
		self.state = my_info['state']
		logger.info("Calling phaseOneClustering")
		self.startPhaseOneClustering()
		logger.info("Starting Server on Node: "+str(myId))
		# thread.start_new_thread(main_server.serve,(self,))
		main_server.serve(self)
		logger.info("Server successfully started on node: "+str(myId))



	def getChildWeight(self):
		childWeight = 0
		if self.childListId is not None:
			for c in self.childListId:
				childWeight += weightMatrix.getWeight(c)
		return childWeight

	# As a leaf node, send size to parent
	def startPhaseOneClustering(self):
		logger.info("Starting Phase One Clustering on Node: " + str(self.id))
		if (self.childListId== None or len(self.childListId) == 0):
			logger.info("Calling phaseOneClusterStart on client.py from Node.py with parentId: %s"%(self.parentId))
			client.phaseOneClusterStart(self,raspberryPi_id_list.ID_IP_MAPPING[self.parentId])
			print "Node: %s sent size() message to parent: %s" % (self.id, self.parentId)
			logger.info("Node: %s sent size() message to parent: %s" % (self.id, self.parentId))
		else:
			logger.info("I don't have any parent: Node: %s"%(self.id))


	# As a parent, send size to YOUR parent
	# Must be called ONLY after childRequestCounter == len(childListId)
	def sendSizeToParent(self):
		if (raspberryPi_id_list.ID_IP_MAPPING[self.parentId] != None):
			client.phaseOneClusterStart(self,raspberryPi_id_list.ID_IP_MAPPING[self.parentId])
		else:
			client.sendCluster(self)




		

	# Connects to Raspberry Pi and registers its IP address on the central lookup
	# Can merge getIP and registerOnPi
	def registerOnPi():
		pass

	# Connects to Raspberry Pi (Central Service) and gets its IP address
	# Can merge getIP and registerOnPi
	def getIP():
		pass

	def getIpFromId(Id):
		return raspberryPi_id_list[Id]

	def getIPfromId(self,Id):
		return raspberryPi_id_list.ID_IP_MAPPING[Id]


#
# def testNode():
# 	n0 = Node
# 	n1 = Node(1)
# 	# print n1.parentId
# 	assert n1.parentId == 0
# 	print "Test 1 Passed"
#
# 	assert n1.weight > 0
# 	print "Test 2 Passed"
#
#
# testNode()


