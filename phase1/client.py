

from __future__ import print_function
import sys
import grpc

import phase1_pb2
import phase1_pb2_grpc
import Node
import logging
import os
import logging.handlers
import datetime
from pymongo import MongoClient

con = MongoClient('mongodb://localhost:27017/')
db = con.spanningtreemap

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


# 169.254.172.23 - bhushan

#169.254.179.83 - seema
#169.254.28.146 - gurnoor
INITIALIZE_FLAG = False

def phaseOneClusterStart(node, serverIpAddress):
	channel = grpc.insecure_channel(serverIpAddress)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	sendSize(node, stub)

def run():
	## Add after both clusterings are complete!
	pass
	# global INITIALIZE_FLAG
	# ## sys.argv[1] is IP of server e.g. localhost:50051
	# print(sys.argv[1])
	# print("Client runs")
    #
	# thisNode = Node.Node(int(sys.argv[2]))
	# print("successfully created thisNode")
	# print(thisNode)
	# print(thisNode.size)
    #
	# # if (not INITIALIZE_FLAG) and len(thisNode.childListId) == 0:
	# INITIALIZE_FLAG = True
	# sendSize(thisNode, stub)
    #
	# # response = stub.SayHello(helloworld_pb2.HelloRequest(name='Vimanyu'))
	# response = stub.Handshake(phase1_pb2.RequestMessage(nodeId="12",destinationId="21",message="Hello Dear Server !"))
	# response1 = stub.SendPacket(phase1_pb2.RequestMessage(nodeId="12",destinationId="21",message="Hello Dear Server Please forward my request!"))
    #
	# print("client received: " + response.ackMessage+" from Node ID :"+response.nodeId)
	# print("client received from sendPacket: " + response1.ackMessage+" from Node ID :"+response1.nodeId)

def sendSize(node,stub):
	print(node.size)
	logger.info("Node: %s - Starting sendSize"%(node.id))

	sizeRPC = stub.Size(phase1_pb2.MySize(size=node.size,nodeId=node.id))
	logger.info("Node: %s - Successfully sent the size message of size %s to parentId: %s"%(str(node.id),str(node.size),str(node.parentId)))
	logger.info("Node: %s - Responded to Size RPC with reply: %s"%(str(node.parentId),sizeRPC.message))
	if sizeRPC.message=="Prune":
		logger.info("Node: %s - Got Prune"%(node.id))
		# Become a clusterhead and send Cluster RPC to children
		node.clusterheadId = node.id.encode('utf-8')
		node.parentId = None
		#set I am the cluster
		node.isClusterhead = 1
        
		node.state = "free"
		try:
			db.spanningtree.update_one({'nodeId': node.id}, {'$set': {'isClusterhead': node.isClusterhead,
        															'parentId':None,
                                                                    'clusterheadId': node.clusterheadId,
                                                                    'hopcount':0,
                                                                    'size':node.size,
                                                                    'state': node.state}}, upsert=False)
		except Exception as e:
			logger.error("Node: %s - not able to update db"%(node.id))
			logger.error(e)

		sendCluster(node)
	else:
		logger.info("Node: %s - Didn't get Prune "%(node.id))
		# Do nothing if the child is accepted into the current cluster
		## Might need to add cluster ID to the central lookup #Later
		pass

def sendJamSignal(childIpList,clusterHeadId):
	for ip in childIpList:
		channel = grpc.insecure_channel(ip)
		stub = phase1_pb2_grpc.MainServiceStub(channel)
		logger.info("Node: %s - Sending jam to childIp: %s"%(clusterHeadId,ip))
		clusterRPC = stub.Jam(phase1_pb2.JamRequest(nodeId=clusterHeadId))
		logger.info("Node: {} - Clusterhead got response {} after sending jam to child ip: {}".format(clusterHeadId,clusterRPC,ip))

def sendCluster(node):
	# newClusterId = "C"+str(node.id)
	newClusterId = str(node.id)
	hopCount=1
	if node.childListId is None:
		print("Node: %s - I am clusterhead with no children"%(node.id))
		logger.info("Node: %s - I am clusterhead with no children"%(node.id))
		return
	for child in node.childListId:
		childIP = node.getIPfromId(child)
		channel = grpc.insecure_channel(childIP)
		stub = phase1_pb2_grpc.MainServiceStub(channel)
		logger.info("Node: %s - Sending cluster message to child id: %s" %(str(node.id),str(child)))
		clusterRPC = stub.JoinCluster(phase1_pb2.JoinClusterRequest(clusterHeadName=newClusterId,hopcount=hopCount))
		print("Node: {} - Got Response: {} after sending cluster message to child id: {}".format(str(node.id),clusterRPC,str(child)))
		logger.info("Node: {} - Got Response: {} after sending cluster message to child id: {}".format(str(node.id),clusterRPC,str(child)))

def sendShiftNodeRequest(node,bestNodeClusterHeadId,clusterHeadIp):
	channel = grpc.insecure_channel(clusterHeadIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	clusterRPC = stub.ShiftNodeRequest(phase1_pb2.ShiftRequest(nodeId=node.id,sumOfweight=node.size,clusterHeadId=bestNodeClusterHeadId))
	## Add result after sending ShiftNodeRequest
	logger.info("Node: %s - Sent sendShiftNodeRequest about C:%s to clusterhead:%s"%(node.id,bestNodeClusterHeadId,clusterHeadIp))

def propogateClusterheadInfo(node,clusterName,hopCount):
	for child in node.childListId:
		childIP = node.getIPfromId(child)
		channel = grpc.insecure_channel(childIP)
		stub = phase1_pb2_grpc.MainServiceStub(channel)
		logger.info("Node: %s - Sending propagate cluster message to child id: %s"%(str(node.id),str(child)))
		clusterRPC = stub.JoinCluster(phase1_pb2.JoinClusterRequest(clusterHeadName=clusterName,hopcount=hopCount))
		print("Node: {} - Got Response: {} after sending cluster message to child id: {}".format(str(node.id),clusterRPC,str(child)))
		logger.info("Node: {} - Got Response: {} after sending cluster message to child id: {}".format(str(node.id),clusterRPC,str(child)))

def sendShiftClusterRequest(clusterheadId,shiftNodeId,shiftNodeSum,shiftNodeClusterIp):
	# send shift clusterRequest to Cj clusterhead
	channel = grpc.insecure_channel(shiftNodeClusterIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	logger.info("Node: %s - Clusterhead sending ShiftClusterRequest to ClusterheadIp: %s"%(clusterheadId,shiftNodeClusterIp))
	clusterRPC = stub.ShiftClusterRequest(phase1_pb2.ShiftClusterReq(senderClusterHeadId=clusterheadId,senderNodeId=shiftNodeId,sumOfweights=shiftNodeSum))
	logger.info("Node: {} - Got Response: {} after sending shift cluster request to Node ip: {}".format(clusterheadId, clusterRPC,shiftNodeClusterIp))


def sendAccept(clusterHeadId,senderClusterHeadIp):
	channel = grpc.insecure_channel(senderClusterHeadIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	logger.info("Node:%s  - Sending shift Accept to Node ip: %s" % (clusterHeadId, senderClusterHeadIp))
	clusterRPC = stub.Accept(phase1_pb2.AcceptRequest(clusterHeadId=clusterHeadId))
	logger.info("Node: {} - Got Response: {} after sending shift Accept to Node ip: {}".format(clusterHeadId, clusterRPC,senderClusterHeadIp))

def sendReject(clusterHeadId,senderClusterHeadIp):
	channel = grpc.insecure_channel(senderClusterHeadIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	clusterRPC = stub.Reject(phase1_pb2.RejectRequest(clusterHeadId=clusterHeadId))
	logger.info("Node: %s - Clusterhead sent shift reject to Node ip: %s" % (clusterHeadId,senderClusterHeadIp))
	logger.info(clusterRPC)
       		
def propagateJamToChildren(childIpList,jamId, nodeId):
	for cip in childIpList:
		channel = grpc.insecure_channel(cip)
		stub = phase1_pb2_grpc.MainServiceStub(channel)
		clusterRPC = stub.Jam(phase1_pb2.JamRequest(nodeId=jamId))
		logger.info("Node: {} - Got Response: {} after sending JAM to child ip: {}".format(nodeId,clusterRPC,cip))

def propagateWakeUp(childIpList, nodeId):
	for cip in childIpList:
		channel = grpc.insecure_channel(cip)
		stub = phase1_pb2_grpc.MainServiceStub(channel)
		clusterRPC = stub.WakeUp(phase1_pb2.wakeUpRequest(wakeywakey="wakeup"))
		logger.info("Node: {} - Got Response: {} after sending wake to child ip: {}".format(nodeId, clusterRPC,cip))

def joinNewParent(nodeId,nodeSize,newParentIp):
	channel = grpc.insecure_channel(newParentIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	clusterRPC = stub.JoinNewParent(phase1_pb2.JoinNewParentRequest(childSize=nodeSize, nodeId=str(nodeId)))
	logger.info("Node: {} - Got Response: {} after sending join request to new parent ip: {}".format(nodeId,clusterRPC, newParentIp))

def informParentAboutNewSize(sizeIncrement,nodeId,parentIp):
	channel = grpc.insecure_channel(parentIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	clusterRPC = stub.UpdateSize(phase1_pb2.UpdateSizeRequest(sizeIncrement=sizeIncrement))
	logger.info("Node: {} - Got Response: {} after sending updateSize request to existing parent ip: {}".format(nodeId,clusterRPC, parentIp))

def propagateNewClusterHeadToChildren(childIpList, nodeId,clusterheadId):
	for cip in childIpList:
		channel = grpc.insecure_channel(cip)
		stub = phase1_pb2_grpc.MainServiceStub(channel)
		clusterRPC = stub.UpdateClusterhead(phase1_pb2.UpdateClusterheadRequest(newClusterheadId=str(clusterheadId)))
		logger.info("Node: {} - Got Response: {} after sending newClusterhead to child ip: {}".format(nodeId,clusterRPC, cip))

def sendShiftCompleteToBothClusterHeads(oldClusterheadIp,newClusterheadIp,nodeId):
	channel = grpc.insecure_channel(oldClusterheadIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	clusterRPC = stub.ShiftComplete(phase1_pb2.SendShiftCompleteAck(id=str(nodeId),sendShiftCompleteAck="Departed"))
	logger.info("Node: {} - Got Response: {} after sending shiftComplete to old clusterhead ip: {}".format(nodeId,clusterRPC,oldClusterheadIp))

	channel = grpc.insecure_channel(newClusterheadIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	clusterRPC = stub.ShiftComplete(phase1_pb2.SendShiftCompleteAck(id=str(nodeId),sendShiftCompleteAck="Added"))
	logger.info("Node: {} - Got Response: {} after sending shiftComplete to new clusterhead ip: {}".format(nodeId, clusterRPC,newClusterheadIp))


def removeChildIdFromParent(nodeId,parentIp):
	channel = grpc.insecure_channel(parentIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	clusterRPC = stub.RemoveChildIdFromParent(phase1_pb2.RemoveChildIdFromParentRequest(departingChildId=str(nodeId)))
	logger.info("Node: {} - Got Response: {} after sending removeChildIdFromParent to (old) parent ip: {}".format(nodeId,clusterRPC,parentIp))

def sendShiftStart(nodeId, targetNodeId,targetNodeIp):
	channel = grpc.insecure_channel(targetNodeIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	clusterRPC = stub.ShiftStart(phase1_pb2.ShiftStartRequest(targetNodeId=str(targetNodeId)))
	logger.info("Node: {} - Got Response: {} after sending shift start to Node id: {}".format(nodeId,clusterRPC,targetNodeId))

def sendShiftFinished(nodeId,targetNodeIp):
	channel = grpc.insecure_channel(targetNodeIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	clusterRPC = stub.ShiftFinished(phase1_pb2.ShiftFinishedRequest(clusterHeadId=str(nodeId)))
	logger.info("Node: {} - Got Response: {} after sending ShiftFinished to Node ip: {}".format(nodeId,clusterRPC,targetNodeIp))

def sendWakeUp(ipList,nodeId):
	for cip in ipList:
		channel = grpc.insecure_channel(cip)
		stub = phase1_pb2_grpc.MainServiceStub(channel)
		logger.info("Node: %s - Sending wakeup to child ip: %s"%(nodeId,cip))
		clusterRPC = stub.WakeUp(phase1_pb2.wakeUpRequest(wakeywakey=str(nodeId)))
		logger.info("Node: {} - Got Response: {} after sending wakeup to child ip: {}".format(nodeId,clusterRPC,cip))

def sendHello(nodeId,i,neighbourIp,nodeClusterheadId,nodeHopcount,nodeState):
	channel = grpc.insecure_channel(neighbourIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	logger.info("Node: {} - sendng hello to IP: {} type: {}".format(nodeId,neighbourIp,type(neighbourIp)))
	logger.info("Node: {} - Sending Hello to node: {}".format(nodeId,i))
	logger.info("Node: {} - senderId: {} type: {}".format(nodeId,str(nodeId),type(str(nodeId))))
	logger.info("Node: {} - hopToSenderClusterhead: {} type: {}".format(nodeId, nodeHopcount,type(nodeHopcount)))
	logger.info("Node: {} - senderState: {} type: {}".format(nodeId, nodeState,type(nodeState)))
	logger.info("Node: {} - senderClusterheadId: {} type: {}".format(nodeId, nodeClusterheadId,type(nodeClusterheadId)))

	clusterRPC = stub.Hello(phase1_pb2.SendHello(senderId=str(nodeId),hopToSenderClusterhead=nodeHopcount,\
												 senderState=nodeState,senderClusterheadId=nodeClusterheadId))
	logger.info("Node: {} - Got Response: {} after sending Hello to id: {}".format(nodeId,clusterRPC, i))


if __name__ == '__main__':
	run()
