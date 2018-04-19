import weightMatrix
from spanning_tree import SPANNING_INFO
import raspberryPi_id_list
import main_server
import client
import pymongo
from pymongo import MongoClient

import logging
import os, traceback
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

con = MongoClient("mongodb://localhost:27017/spanningtreemap")
db = con.spanningtreemap
class Node:
	'''
	Node class representing each node in the network
	'''
	def __init__(self,myId):
		logger.info("#######################")
		logger.info("Node: %s - Initializing"%(str(myId)))
		logger.info("#######################")
		self.id = str(myId)
		#self.parentId = parentId
		#self.childListId = childListId
		my_info = SPANNING_INFO[myId]
		self.ipAddress= raspberryPi_id_list.ID_IP_MAPPING[myId]
		self.parentId = my_info['parentId']
		self.childListId = my_info['childListId']
		self.dist = my_info['dist']
		self.clusterheadId = my_info['clusterheadId']
		self.hopcount = 0
		self.rackLocation = my_info['rackLocation']
		self.subtreeList = my_info['subtreeList']
		self.neighbourList = my_info['neighbourList']
		self.weight = weightMatrix.getWeight(self.id)
		self.size = self.weight
		self.childRequestCounter = 0
		self.initialNodeChildLength = 0
		self.bestNodeId = self.id
		self.bestNodeHopCount = self.hopcount
		self.bestNodeClusterHeadId = self.clusterheadId


		self.neighbourHelloArray = set()
		if self.childListId != None and len(self.childListId) != 0:
			self.initialNodeChildLength = len(self.childListId)

		#info to be saved for shiftNodeRequest
		self.shiftNodeId = None
		self.shiftNodeSum = None
		self.shiftNodeCluster = None

		# self.childWeight = self.getChildWeight()
		self.isClusterhead = my_info['isClusterhead']
		self.state = my_info['state']
		logger.info("Node: %s - Calling phaseOneClustering"%(myId))

		self.startPhaseOneClustering()
		logger.info("Node: %s - Starting Server"%(str(myId)))
		# thread.start_new_thread(main_server.serve,(self,))
		main_server.serve(self)



	def getChildWeight(self):
		childWeight = 0
		if self.childListId is not None:
			for c in self.childListId:
				childWeight += weightMatrix.getWeight(c)
		return childWeight

	# As a leaf node, send size to parent
	def startPhaseOneClustering(self):
		logger.info("Node: %s - Starting Phase One Clustering"%(str(self.id)))
		if (self.childListId== None or len(self.childListId) == 0):
			logger.info("Node: %s - Calling phaseOneClusterStart with parentId: %s"%(self.id,self.parentId))
			client.phaseOneClusterStart(self,raspberryPi_id_list.ID_IP_MAPPING[self.parentId])
			print "Node: %s - Sent size() message to parent: %s" % (self.id, self.parentId)
			logger.info("Node: %s - Sent size() message to parent: %s" % (self.id, self.parentId))
		else:
			logger.info("Node: %s - I am a parent not leaf"%(self.id))


	# As a parent, send size to YOUR parent
	# Must be called ONLY after childRequestCounter == len(childListId)
	def sendSizeToParent(self):
		if (self.parentId != None):
			client.phaseOneClusterStart(self,raspberryPi_id_list.ID_IP_MAPPING[self.parentId])
		else:
			logger.info("Node: %s - Setting myself as clusterhead as no parent found!"%(self.id))
			self.isClusterhead = 1
			self.clusterheadId = str(self.id)
			self.state = "free"
			# try:
			# 	db.spanningtree.update_one({'_id':ObjectId("")},{'$set':{'isClusterhead':self.isClusterhead,'clusterheadId':self.clusterheadId,'state':self.state}},upsert=False)
			# except Exception as e:
			# 	logger.error("Some Error occurred in sendSizeToParent()")
			client.sendCluster(self)

	def propogateClusterheadInfo(self,clusterName,hopCount):
		if (self.childListId != None and len(self.childListId) != 0):
			client.propogateClusterheadInfo(self,clusterName,hopCount+1)
		else:
			logger.info("Node: %s - I don't have any children"%(self.id))

	def sendShiftNodeRequest(self, bestNodeClusterHeadId):
		if self.isClusterhead != 1:

			client.sendShiftNodeRequest(self,bestNodeClusterHeadId,raspberryPi_id_list.ID_IP_MAPPING[self.clusterheadId])

	def propagateJamToChildren(self,jamId):
		logger.info("Node: %s - Adding childIps for propagating jam signal"%(self.id))
		if self.childListId == None or len(self.childListId) == 0:
			logger.info("Node: %s - Leaf node. NOT propagating Jam signal anymore"%(self.id))
			return

		childIPs = [raspberryPi_id_list.ID_IP_MAPPING[childId] for childId in self.childListId]
		logger.info(childIPs)
		client.propagateJamToChildren(childIPs,jamId,self.id)

	def propagateWakeUp(self):
		if self.childListId != None and len(self.childListId) != 0:
			logger.info("Node: %s - Propagating wakeup to children."%(self.id))
			childIPs = [raspberryPi_id_list.ID_IP_MAPPING[childId] for childId in self.childListId]
			client.propagateWakeUp(childIPs, self.id)
		else:
			logger.info("Node: %s - No children found! Stopping wakeup propagation."%(self.id))
			return

	def updateInternalVariablesAndSendJoin(self,bestNodeId,bestNodeClusterHeadId,newHopCount):
		logger.info("Node: {} - Updating parent,clusterhead and hopcount from {},{},{}, to {},{},{}".format(self.id,self.parentId,\
																											self.clusterheadId,self.hopcount,\
																											self.bestNodeId,bestNodeClusterHeadId,\
																											self.bestNodeHopCount))
		self.parentId = bestNodeId
		self.clusterheadId = bestNodeClusterHeadId
		self.hopcount = newHopCount
		# try:
		# 	db.spanningtree.update_one({'_id': ObjectId("")}, {
		# 		'$set': {'parentId': self.parentId, 'clusterheadId': self.clusterheadId,
		# 				 'hopcount': self.hopcount}}, upsert=False)
		# except Exception as e:
		# 	logger.error("Some error occurred while updating db in updateInternalVariablesAndSendJoin()")
		client.joinNewParent(self.id,self.size,raspberryPi_id_list.ID_IP_MAPPING[bestNodeId])

	def propagateNewClusterHeadToChildren(self):
		childIPs = [raspberryPi_id_list.ID_IP_MAPPING[childId] for childId in self.childListId]
		client.propagateNewClusterHeadToChildren(childIPs, self.id,self.clusterheadId)

	def informParentAboutNewSize(self,sizeIncrement):
		if self.parentId != None:
			client.informParentAboutNewSize(sizeIncrement,self.id,raspberryPi_id_list.ID_IP_MAPPING[self.parentId])

	def sayByeToParent(self):
		client.removeChildIdFromParent(self.id,raspberryPi_id_list.ID_IP_MAPPING[self.parentId])
		client.informParentAboutNewSize(-self.size,self.id,raspberryPi_id_list.ID_IP_MAPPING[self.parentId])

	def sendShiftCompleteToBothClusterHeads(self,oldClusterheadId, newClusterheadId):
		client.sendShiftCompleteToBothClusterHeads(raspberryPi_id_list.ID_IP_MAPPING[oldClusterheadId],\
												   raspberryPi_id_list.ID_IP_MAPPING[newClusterheadId],self.id)

	def startPhase2Clustering(self):
		self.bestNodeHopCount = self.hopcount
		logger.info("Node: %s - hopcount before Phase 2 clustering: %s"%(self.id,self.hopcount))
		# try:
		# 	db.spanningtree.update_one({"_id":ObjectId("")},{'$set':{'bestNodeHopCount':self.bestNodeHopCount}},upsert=False)
		# except Exception as e:
		# 	logger.error("Some error occurred while updating db in startPhase2Clustering()")
		# 	logger.error(e)
		logger.info("Node: %s - Starting phase 2 clustering"%(self.id))
		# if self.isClusterhead == 1:
		# 	logger.info("Node: %s is clusterhead. Not taking any action"%(self.id))
		# 	return

		rackIdRow = self.rackLocation.split(",")[0]
		rackIdCol = self.rackLocation.split(",")[1]

		myNeighborsRack = []
		myNeighborsRack.append("{},{}".format(int(rackIdRow)+1,rackIdCol))
		myNeighborsRack.append("{},{}".format(int(rackIdRow) - 1, rackIdCol))
		myNeighborsRack.append("{},{}".format(int(rackIdRow), int(rackIdCol)+1))
		myNeighborsRack.append("{},{}".format(int(rackIdRow), int(rackIdCol) - 1))
		myNeighborsRack.append("{},{}".format(int(rackIdRow)+1, int(rackIdCol) + 1))
		myNeighborsRack.append("{},{}".format(int(rackIdRow)-1, int(rackIdCol) - 1))
		myNeighborsRack.append("{},{}".format(int(rackIdRow)+1, int(rackIdCol) - 1))
		myNeighborsRack.append("{},{}".format(int(rackIdRow)-1, int(rackIdCol) + 1))
		HARDCODEDNEIGHBOURS_ID  = ['0','1','2','3','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
		for i in HARDCODEDNEIGHBOURS_ID:
			if i== self.id:
				continue
			# if i.find("C") != -1:
			# 	self.neighbourHelloArray.add(i)
			# 	continue
			resp = client.sendHello(self.id,i,raspberryPi_id_list.ID_IP_MAPPING[i],self.clusterheadId,self.hopcount,self.state)
			logger.info("Node :%s got reply %s from Node: %s after sendHello"%(self.id,resp,i,))




	# Connects to Raspberry Pi and registers its IP address on the central lookup
	# Can merge getIP and registerOnPi
	def registerOnPi(self):
		pass

	# Connects to Raspberry Pi (Central Service) and gets its IP address
	# Can merge getIP and registerOnPi
	def getIP(self):
		pass

	def getIPfromId(self,Id):
		ip = ""
		try:
			ip = raspberryPi_id_list.ID_IP_MAPPING[str(Id)]
		except Exception as e:
			logger.error("Error occurred while finding IP of {}".format(Id))
			logger.error(traceback.format_exc())
		return ip

	def sendJamSignal(self):
		childIpList=[]
		#send jam signal to children
		if(self.childListId!= None and len(self.childListId)!=0):
			for childId in self.childListId:
				childIpList.append(self.getIPfromId(childId))
			# call client
			logger.info("Node: {} - ChildIpList is {}".format(self.id,childIpList))
			client.sendJamSignal(childIpList, self.clusterheadId)
		else:
			return


	def sendShiftClusterRequest(self):
		'''calculate ip for the Cj cluster'''
		logger.info("Node: %s - Clusterhead sending ShiftClusterRequest to clusterheadId: %s"%(self.id,self.shiftNodeCluster))
		shiftNodeClusterIp = self.getIPfromId(self.shiftNodeCluster)
		client.sendShiftClusterRequest(self.clusterheadId,self.shiftNodeId,self.shiftNodeSum,shiftNodeClusterIp)

	def accept(self,senderClusterHeadId):
		'''send shift accept'''
		senderClusterHeadIp = self.getIPfromId(senderClusterHeadId)
		client.sendAccept(self.id,senderClusterHeadIp)

	def reject(self,senderClusterHeadId):
		senderClusterHeadIp = self.getIPfromId(senderClusterHeadId)
		client.sendReject(self.id,senderClusterHeadIp)

	def sendShiftStart(self):
		client.sendShiftStart(self.id,self.shiftNodeId,self.getIPfromId(self.shiftNodeId))

	def sendShiftFinished(self):
		client.sendShiftFinished(self.id,self.getIPfromId(self.shiftNodeCluster))

	def sendWakeup(self):
		childIpList=[]
		#send wakeup signal to children
		if(self.childListId!= None and len(self.childListId)!=0):
			for childId in self.childListId:
				childIpList.append(self.getIPfromId(childId))
			# call client
			client.sendWakeUp(childIpList, self.id)
		else:
			logger.info("Node: %s - No children found to wakeup. Returning"%(self.id))
			return

	def checkEnergy(self):
		initialEnergy = 0
		finalEnergy = 0
		shiftNode = db.spanningtree.find_one({})[self.shiftNodeId]
		shiftNodeInitialHopCount = shiftNode['hopcount']
		bestNode = db.spanningtree.find_one({})[self.shiftNodeId][shiftNode['bestNodeId']]
		shiftNodeFinalHopCount = db.spanningtree.find_one({})[bestNode['id']][bestNode['hopcount']] + 1

		shiftNodeCluster = db.spanningtree.find_one({})[self.shiftNodeCluster]
		childrenList1 = [i for i in self.childListId]
		childrenList2 = [i for i in shiftNodeCluster['childListId']]
		for childId in childrenList1:
			node = db.spanningtree.find_one({})[childId]
			weight = weightMatrix.matrix[childId][self.shiftNodeId]
			hops = node['hopcount']
			initialEnergy += weight*(hops+shiftNodeInitialHopCount)
			finalEnergy += weight*(hops+shiftNodeFinalHopCount)
			try:
				for child in node['childListId']:
					childrenList1.append(child)
			except KeyError as e:
				pass

		for childIdOtherCluster in childrenList2:
			node = db.spanningtree.find_one({})[childIdOtherCluster]
			weight = weightMatrix.matrix[childIdOtherCluster][self.shiftNodeId]
			hops = node['hopcount']
			initialEnergy += weight * (hops + shiftNodeInitialHopCount)
			finalEnergy += weight * (hops + shiftNodeFinalHopCount)
			try:
				for child in node['childListId']:
					childrenList2.append(child)
			except KeyError as e:
				pass

		return initialEnergy < finalEnergy

	def startCheckingEnergyDrain(self):
		childList = [c for c in self.childListId]
		hopCount = 0


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


