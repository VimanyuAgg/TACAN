

from __future__ import print_function

import grpc

import phase1_pb2
import phase1_pb2_grpc
import Node
# 169.254.172.23 - bhushan

#169.254.179.83 - seema
#169.254.28.146 - gurnoor
INITIALIZE_FLAG = False
def run():
	channel = grpc.insecure_channel('localhost:50051')
	stub = phase1_pb2_grpc.MainServiceStub(channel)
	thisNode = Node.Node(1)
	print("successfully created thisNode")
	print(thisNode)
	print(thisNode.size)

	# if (not INITIALIZE_FLAG) and len(thisNode.childListId) == 0:
	INITIALIZE_FLAG = True
	sendSize(thisNode, stub)

	# response = stub.SayHello(helloworld_pb2.HelloRequest(name='Vimanyu'))
	response = stub.Handshake(phase1_pb2.RequestMessage(nodeId="12",destinationId="21",message="Hello Dear Server !"))
	response1 = stub.SendPacket(phase1_pb2.RequestMessage(nodeId="12",destinationId="21",message="Hello Dear Server Please forward my request!"))

	print("client received: " + response.ackMessage+" from Node ID :"+response.nodeId)
	print("client received from sendPacket: " + response1.ackMessage+" from Node ID :"+response1.nodeId)

def sendSize(node,stub):
	print(node.size)
 	sizeRPC = stub.Size(phase1_pb2.MySize(size=node.size))
 	print("Node "+str(node.id)+" sent the size message of size "+str(node.size)+" to "+str(node.parentId))
  

if __name__ == '__main__':
	run()
