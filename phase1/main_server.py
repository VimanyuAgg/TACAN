
from concurrent import futures
import time
import grpc
import sys

import phase1_pb2
import phase1_pb2_grpc
from Node import Node
import raspberryPi_id_list
import spanning_tree_gurnoor as spanning_tree  # TODO: must

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class MainServer(phase1_pb2_grpc.MainServiceServicer):

  #
  # Initialize the node
  # Will be done by a script in future
  #
  def __init__(self, myId=1):
      #different for each node
      # myId = 1
      self.myId = myId
      # parentId=0
      # childList=[2,3]
      # dist=1
      # clusterheadid=0
      # subtreeList=[2,3]
      # neighbourList=[]
      # isClusterhead=False
      #default state
      # state="active"
      # self.node = Node(myId)
      print('myId', myId)


  def Handshake(self, request , context):
    return phase1_pb2.ResponseMessage(nodeId="21",destinationId="12",ackMessage="Hello Dear Client")

  def SendPacket(self, request , context):
    #check if current node is the destination node
    #else forward it to the destination node
    print('Inside SendPacket', request)
    print(self.myId, request.destinationId)

    if self.myId == int(request.destinationId):
        return phase1_pb2.ResponseMessage(nodeId=str(self.myId),
        destinationId="12",
        ackMessage="Hello Dear Client")
    else:
        return self.Forward(request, context)
  # end SendPacket

  def Forward(self, request, context):
      # request.hopIds += [self.myId]

      dest_clusterhead = self.getParentId(int(request.destinationId))
      if dest_clusterhead is None:
          # destination node is a clusterheadid
          dest_clusterhead = request.destinationId
      print('self.myId', self.myId)
      my_clusterhead = self.getParentId(self.myId)
      print('my_clusterhead', my_clusterhead)
      if my_clusterhead is None:
          my_clusterhead = self.myId
      print('dest_clusterhead', dest_clusterhead)
      print('my_clusterhead', my_clusterhead)
      if dest_clusterhead == my_clusterhead:
          # destination in same cluster
          dest_node_ip = self.getIp(request.destinationId)
      else:
          if self.myId == my_clusterhead:
              dest_node_ip = self.getIp(dest_clusterhead)
          else:
              dest_node_ip = self.getIp(my_clusterhead)

      print('dest_node_ip', dest_node_ip)
      channel = grpc.insecure_channel(dest_node_ip)
      stub = phase1_pb2_grpc.MainServiceStub(channel)
      response1 = stub.SendPacket(request)
      return response1



  def getIp(self, nodeId):
    # TODO
    nodeId = int(nodeId)
    ip_mapping = raspberryPi_id_list.ID_IP_MAPPING
    if nodeId not in ip_mapping:
      return 'Node %s does not exist in raspberryPi_id_list.py' % nodeId  # TODO custom Errors
    else:
      return ip_mapping[nodeId]


  def getParentId(self, nodeId):
    """
    returns: parentId if node and its parent exist
             None if clusterhead
             'Node does not exist' if nodeId not found
    """
    nodeId = int(nodeId)
    if nodeId not in spanning_tree.SPANNING_INFO:
      return 'Node %s does not exist in spanning_tree.py' % nodeId # TODO custom Errors
    else:
      return spanning_tree.SPANNING_INFO[nodeId]['parentId']




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


def serve(nodeId):
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  mainServer = MainServer(myId=nodeId)
  ip = mainServer.getIp(nodeId)
  phase1_pb2_grpc.add_MainServiceServicer_to_server(mainServer, server)
  print 'running on: %s ' % ip
  server.add_insecure_port(ip)
    # print 'running on default port 50051'
    # server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)


def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts


if __name__ == '__main__':
    opts = getopts(sys.argv)
    nodeId = int(opts['-p'])
    serve(nodeId)
