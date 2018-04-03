

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
	logger.info("sendSize starting on client.py for node: %s"%(node.id))

	sizeRPC = stub.Size(phase1_pb2.MySize(size=node.size))
	logger.info("Node "+str(node.id)+" sent the size message of size "+str(node.size)+" to "+str(node.parentId))
	logger.info("Node "+str(node.parentId)+": responded to Size RPC with reply: "+sizeRPC.message)
	if sizeRPC.message=="Prune":
		logger.info("Got Prune %s"%(node.id))
		# Become a clusterhead and send Cluster RPC to children
		node.clusterheadId = node.id
		node.parentId = None
		#set I am the cluster
		node.isClusterhead = 1
		node.state = "free"
		# fix below

		sendCluster(node)
	else:
		logger.info("Didn't get Prune Node: %s"%(node.id))
		# Do nothing if the child is accepted into the current cluster
		## Might need to add cluster ID to the central lookup #Later
		pass


def sendCluster(node):
	newClusterId = "C"+str(node.id)
	hopCount=1
	if node.childListId is None:
		print("I am the clusterhead")
		return
	for child in node.childListId:
		childIP = node.getIPfromId(child)
		channel = grpc.insecure_channel(childIP)
		stub = phase1_pb2_grpc.MainServiceStub(channel)
		clusterRPC = stub.Cluster(phase1_pb2.ClusterName(newClusterId,hopCount))
		print("Node "+str(node.id)+": sent cluster message to child id: "+str(child))
		print("Node "+str(node.id)+": got the reply: "+clusterRPC.ClusterAck+"from child id: "+str(child))

def sendShiftNodeRequest(node,bestNodeClusterHeadId,clusterHeadIp):
	channel = grpc.insecure_channel(clusterHeadIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	clusterRPC = stub.ShiftNodeRequest(phase1_pb2.ShiftRequest(node.id, node.size,bestNodeClusterHeadId))
	## Add result after sending ShiftNodeRequest
	logger.info("Node: %s sent sendShiftNodeRequest about C:%s to clusterhead:%s"%(node.id,bestNodeClusterHeadId,clusterHeadIp))

def propogateClusterheadInfo(node,clusterName,hopCount):
	for child in node.childListId:
		childIP = node.getIPfromId(child)
		channel = grpc.insecure_channel(childIP)
		stub = phase1_pb2_grpc.MainServiceStub(channel)
		clusterRPC = stub.Cluster(phase1_pb2.ClusterName(clusterName,hopCount))
		print("Node "+str(node.id)+": sent cluster message to child id: "+str(child))
		print("Node "+str(node.id)+": got the reply: "+clusterRPC.ClusterAck+"from child id: "+str(child))

def propagateJamToChildren(childIpList,jamId, nodeId):
	for cip in childIpList:
		channel = grpc.insecure_channel(cip)
		stub = phase1_pb2_grpc.MainServiceStub(channel)
		clusterRPC = stub.Jam(phase1_pb2.JamRequest(jamId))
		logger.info("Node: %s sent JAM to child ip: %s"%(nodeId,cip))
		logger.info(clusterRPC)

def propagateWakeUp(childIpList, nodeId):
	for cip in childIpList:
		channel = grpc.insecure_channel(cip)
		stub = phase1_pb2_grpc.MainServiceStub(channel)
		clusterRPC = stub.WakeUp(phase1_pb2.wakeUpRequest("wakeup"))
		logger.info("Node: %s sent wake to child ip: %s" % (nodeId, cip))
		logger.info(clusterRPC)

def joinNewParent(nodeId,nodeSize,newParentIp):
	channel = grpc.insecure_channel(newParentIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	clusterRPC = stub.JoinNewParent(phase1_pb2.JoinNewParentRequest(nodeSize, nodeId))
	logger.info("Node: %s sent join request to new parent ip: %s" % (nodeId, newParentIp))
	logger.info(clusterRPC)

def informParentAboutNewSize(sizeIncrement,nodeId,parentIp):
	channel = grpc.insecure_channel(parentIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	clusterRPC = stub.UpdateSize(phase1_pb2.UpdateSizeRequest(sizeIncrement))
	logger.info("Node: %s sent updateSize request to existing parent ip: %s" % (nodeId, parentIp))
	logger.info(clusterRPC)

def propagateNewClusterHeadToChildren(childIpList, nodeId,clusterheadId):
	for cip in childIpList:
		channel = grpc.insecure_channel(cip)
		stub = phase1_pb2_grpc.MainServiceStub(channel)
		clusterRPC = stub.UpdateClusterhead(phase1_pb2.UpdateClusterheadRequest(clusterheadId))
		logger.info("Node: %s sent change to newClusterhead to child ip: %s" % (nodeId, cip))
		logger.info(clusterRPC)

def sendShiftCompleteToBothClusterHeads(oldClusterheadIp,newClusterheadIp,nodeId):
	channel = grpc.insecure_channel(oldClusterheadIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	clusterRPC = stub.SendShiftComplete(phase1_pb2.SendShiftCompleteAck("Departed"))
	logger.info("Node: %s sent shiftComplete to old clusterhead ip: %s" % (nodeId,oldClusterheadIp))
	logger.info(clusterRPC)

	channel = grpc.insecure_channel(newClusterheadIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	clusterRPC = stub.SendShiftComplete(phase1_pb2.SendShiftCompleteAck("Added"))
	logger.info("Node: %s sent shiftComplete to new clusterhead ip: %s" % (nodeId, newClusterheadIp))
	logger.info(clusterRPC)


def removeChildIdFromParent(nodeId,parentIp):
	channel = grpc.insecure_channel(parentIp)
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	clusterRPC = stub.RemoveChildIdFromParent(phase1_pb2.RemoveChildIdFromParentRequest(nodeId))
	logger.info("Node: %s sent removeChildIdFromParent to (old) parent ip: %s" % (nodeId,parentIp))
	logger.info(clusterRPC)




if __name__ == '__main__':
	run()
