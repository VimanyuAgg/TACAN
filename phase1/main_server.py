
from concurrent import futures
import time

import grpc

import phase1_pb2
import phase1_pb2_grpc
from Node import Node
import raspberryPi_id_list

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class MainServer(phase1_pb2_grpc.MainServiceServicer):

  #
  # Initialize the node
  # Will be done by a script in future
  #
  def __init__(self):
      #different for each node
      myId=1
      # parentid=0
      # childList=[2,3]
      # dist=1
      # clusterheadid=0
      # subtreeList=[2,3]
      # neighbourList=[]
      # isClusterhead=False
      #default state 
      state="active"
      self.node = Node(myId)
      
  
  def Handshake(self, request , context):

    return phase1_pb2.ResponseMessage(nodeId="21",destinationId="12",ackMessage="Hello Dear Client")
  
  def SendPacket(self, request , context):
    #check if current node is the destination node 
    #else forward it to the destination node
    return phase1_pb2.ResponseMessage(nodeId="21",destinationId="12",ackMessage="Hello Dear Client")

  def Size(self, request, context):
    childSize = request.size
    if node.size + childSize > raspberryPi_id_list.THRESHOLD_S:
      return phase1_pb2.AccomodateChild(message="Prune")
    else:
      return phase1_pb2.AccomodateChild(message="Accepted")

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  phase1_pb2_grpc.add_MainServiceServicer_to_server(MainServer(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
