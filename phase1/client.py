

from __future__ import print_function

import grpc

import phase1_pb2
import phase1_pb2_grpc

# 169.254.172.23 - bhushan

#169.254.179.83 - seema
#169.254.28.146 - gurnoor
def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = phase1_pb2_grpc.MainServiceStub(channel)
 # response = stub.SayHello(helloworld_pb2.HelloRequest(name='Vimanyu'))
  response = stub.Handshake(phase1_pb2.RequestMessage(nodeId="12",destinationId="21",message="Hello Dear Server !"))
  response1 = stub.SendPacket(phase1_pb2.RequestMessage(nodeId="12",destinationId="21",message="Hello Dear Server Please forward my request!"))
  
  print("client received: " + response.ackMessage+" from Node ID :"+response.nodeId)
  print("client received from sendPacket: " + response1.ackMessage+" from Node ID :"+response1.nodeId)
  

if __name__ == '__main__':
	run()
