
from concurrent import futures
import time
import sys
import grpc

import phase1_pb2
import phase1_pb2_grpc
import raspberryPi_id_list

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class MainServer(phase1_pb2_grpc.MainServiceServicer):

  #
  # Initialize the node
  # Will be done by a script in future
  #
  # def __init__(self):
  #     #different for each node
  #     myId=int(sys.argv[2])
  #     # parentid=0
  #     # childList=[2,3]
  #     # dist=1
  #     # clusterheadid=0
  #     # subtreeList=[2,3]
  #     # neighbourList=[]
  #     # isClusterhead=False
  #     #default state 
  #     # state="active"
  #     print("i run i initialize")
  #     self.node = Node(myId)
      
  
  def Handshake(self, request , context):

    return phase1_pb2.ResponseMessage(nodeId="21",destinationId="12",ackMessage="Hello Dear Client")
  
  def SendPacket(self, request , context):
    #check if current node is the destination node 
    #else forward it to the destination node
    return phase1_pb2.ResponseMessage(nodeId="21",destinationId="12",ackMessage="Hello Dear Client")

  def Size(self, request, context):
    childSize = request.size
    print("Server Node current size is "+str(self.node.size))
    print("Child size is "+str(childSize))
    if self.node.size + childSize > raspberryPi_id_list.THRESHOLD_S:
      return phase1_pb2.AccomodateChild(message="Prune")
    else:
      return phase1_pb2.AccomodateChild(message="Accepted")

  def Cluster(self,request,context):
    clusterName = request.clusterName
    print("Server Node: "+self.node.id+" is now joining Clusterleader "+str(clusterName))
    return phase1_pb2.ClusterAck(clusterAck="Joined")


def serve(ipAddress):
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  phase1_pb2_grpc.add_MainServiceServicer_to_server(MainServer(), server)
 # server.add_insecure_port('[::]:'+)
  server.add_insecure_port(ipAddress)
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
