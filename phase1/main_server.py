
from concurrent import futures
import time
import sys
import grpc
import client
import phase1_pb2
import phase1_pb2_grpc
import raspberryPi_id_list
import thread

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
import datetime
import logging
import os
import logging.handlers

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


class MainServer(phase1_pb2_grpc.MainServiceServicer):

  #
  # Initialize the node
  # Will be done by a script in future
  #
  def __init__(self,node):
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
      print "Inside Mainserver __init__:"
      logger.info("Inside Mainserver __init__:")
      self.node = node
      self.bestNodeId = self.node.id
      self.bestNodeHopCount = self.node.hopcount
      self.bestNodeClusterHeadId = self.node.clusterheadId
      self.neighbourHelloArray = set()
      print("Node created inside __init__ Mainserver...")
      logger.info("Node created inside __init__ Mainserver...")

      
  
  def Handshake(self, request , context):

    return phase1_pb2.ResponseMessage(nodeId="21",destinationId="12",ackMessage="Hello Dear Client")
  
  def SendPacket(self, request , context):
    #check if current node is the destination node 
    #else forward it to the destination node
    return phase1_pb2.ResponseMessage(nodeId="21",destinationId="12",ackMessage="Hello Dear Client")

  def Size(self, request, context):
    childSize = request.size
    print("Server Node: %s current size is %s"%(self.node.id,self.node.size))
    logger.info("Server Node:%s current size is %s"%(self.node.id, self.node.size))
    logger.info ("Server Node:%s Child size is %s"%(self.node.id,childSize))
    try:
      if self.node.size + childSize > raspberryPi_id_list.THRESHOLD_S:
        logger.info("Sending Prune")
        return phase1_pb2.AccomodateChild(message="Prune")
      elif self.node.childListId != None and self.node.childRequestCounter == len(self.node.childListId):
        logger.info("All children responded. Sending size to parent")
        self.node.size += childSize
        self.node.childRequestCounter += 1
        self.node.sendSizeToParent()
        logger.info("Sending Accept")
        return phase1_pb2.AccomodateChild(message="Accepted")
      else:
        logger.info("Sending Accept")
        self.node.size += childSize
        self.node.childRequestCounter += 1
        return phase1_pb2.AccomodateChild(message="Accepted")



    except Exception as e:
      logger.error(e)



  def Cluster(self,request,context):
    clusterName = request.clusterName
    hopCount = request.hop
    # assign clusterhead id
    self.node.clusterheadid= clusterName
    self.node.state = "active"
    # assign isClusterhead as false
    self.node.hop= hopCount

    print("Server Node: "+self.node.id+" is now joining Clusterleader "+str(clusterName))
    #call the cluster message on all its children
    if(self.node.childListId != None):
      self.node.propogateClusterheadInfo(clusterName, hopCount)
    #call custer
    return phase1_pb2.ClusterAck(clusterAck="Joined")

  def ShiftNodeRequest(self,request,context):
    if self.node.isClusterhead and self.node.state == "free":
      #saving the info about this node
      self.node.state = "busy"
      self.node.shiftNodeId = request.nodeId
      self.node.shiftNodeSum = request.sumOfweight
      self.node.shiftNodeCluster = request.clusterHeadId
      #send jam request
      self.node.sendJamSignal()
      #send shift_cluster_request to Cj
      self.node.sendShiftClusterRequest()
      return phase1_pb2.ShiftResponse(message="Recieved")
    else:
      pass

      
  def Jam(self,request,context):
    jamId = request.nodeId
    if (self.node.isClusterhead != 1):
      self.node.state = "sleep"
      self.node.propagateJamToChildren(jamId)
    return phase1_pb2.JamResponse(jamResponse="jammed")

  def sendHello(self,request,context):
    if (self.node.state == "active"):
      self.neighbourHelloArray.add(request.senderId)
      if (self.bestNodeClusterHeadId != request.senderClusterheadId and self.bestNodeHopCount < request.hopToSenderClusterhead):
        self.bestNodeId = request.senderId
        self.bestNodeHopCount = request.hopToSenderClusterhead
        self.bestNodeClusterHeadId = request.senderClusterheadId

      if (len(self.neighbourHelloArray) == 8 and self.bestNodeId != self.node.id):
        ## May need to add self.bestNodeHopCount in the sendShiftRPC to update self.node.hopcount if request is accepted
        self.node.sendShiftNodeRequest(self.bestNodeClusterHeadId)

      # send interested +1
      return phase1_pb2.HelloResponse(interested=1)
    else:
      # send interested -1
      phase1_pb2.HelloResponse(interested=-1)

  def ShiftClusterRequest(self,request,context):
    if self.node.isClusterhead and self.node.state == "free":
      #check size bound condition
      if self.node.size + request.sumOfweights > raspberryPi_id_list.THRESHOLD_S:
        # send reject to Ci
        self.node.reject(request.senderClusterHeadId)
      else:
        # set state to busy
        self.node.state = "busy"
        #send jam to all nodes in cluster
        self.node.sendJamSignal()
        #accept to Ci
        self.node.accept(request.senderClusterHeadId)
    else:
      #send reject as shifting is already on
      self.node.reject(request.senderClusterHeadId)
       
  def wakeUp(self,request,context):
      if (self.node.state == "sleep"):
          self.node.state = "active"
          self.node.propagateWakeUp()
          return phase1_pb2.wakeUpResponse(wokenUp = "wokeup")
      else:
          self.node.propagateWakeUp()
          return phase1_pb2.wakeUpResponse(wokenUp = "already")

  def ShiftStart(self,request,context):
      if (self.node.id == request.targetNodeId and self.node.state == "sleep"):
          oldClusterheadId = self.node.clusterheadId
          self.node.sayByeToParent()
          self.node.updateInternalVariablesAndSendJoin(self.bestNodeId,self.bestNodeClusterHeadId,\
                                                       self.bestNodeHopCount + 1)
          self.node.propagateNewClusterHeadToChildren()
          # is sendShiftCompleteToBothClusterHeads it necessary - can remove if not needed
          self.node.sendShiftCompleteToBothClusterHeads(oldClusterheadId,self.node.clusterheadId)
          return phase1_pb2.ShiftStartResponse(shifStartResponse="byebye")
      else:
          return phase1_pb2.ShiftStartResponse(shifStartResponse="ShiftStart Sent to Wrong Node")


  # As a parent, add new child to myChild and update size
  # Also inform parents about size addition
  def JoinNewParent(self,request,context):
      self.node.childListId.append(request.nodeId)
      sizeIncrement = request.childSize
      self.node.size += request.childSize
      self.node.informParentAboutNewSize(sizeIncrement)
      return phase1_pb2.JoinNewParentResponse(joinResponse="welcome my new child")

  def UpdateSize(self,request,context):
      self.node.size += request.sizeIncrement
      self.node.informParentAboutNewSize(request.sizeIncrement)
      return phase1_pb2.UpdateSizeResponse(updateSizeResponse = "updated size")

  def UpdateClusterhead(self,request,context):
      self.node.clusterheadId = request.newClusterheadId
      self.node.propagateNewClusterHeadToChildren()
      return phase1_pb2.UpdateClusterheadResponse(updateClusterheadResponse = "clusterhead Updated")

  def SendShiftComplete(self,request,context):
      logger.info("ClusterheadId: %s got SendShiftComplete rpc with message:%s"%(self.node.id,request.sendShiftCompleteAck))
      return phase1_pb2.ClusterheadAckSendShift(clusterheadAckSendShift = "ClusterheadId: %s acknowledged shift.."%(self.node.id))

  def RemoveChildIdFromParent(self,request,context):
      logger.info("Parent: %s got RemoveChildIdFromParent rpc from Node:%s" % (self.node.id, request.departingChildId))
      logger.info("Parent: %s has below children before removal" % (self.node.id))
      logger.info(self.node.childListId)
      self.node.childListId.remove(request.departingChildId)
      logger.info("Parent: %s has below children after removal"%(self.node.id))
      logger.info(self.node.childListId)
      return phase1_pb2.RemoveChildIdFromParentResponse(removeChildIdFromParentResponse= "Removed")


def serve(node):
  logger.info("Server starting for Node: %s"%(node.id))
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  try:
    logger.info("Server Created")
    phase1_pb2_grpc.add_MainServiceServicer_to_server(MainServer(node), server)
    logger.info("Main Server init called successfully")
    server.add_insecure_port(raspberryPi_id_list.ID_IP_MAPPING[node.id])
    logger.info("Run port assigned")
    #  server.add_insecure_port('localhost:')
    thread.start_new_thread(server.start(),())

    logger.info("Server started successfully. Entering forever while below")
  except Exception as e:
    logger.error(e)
  try:
    while True:
      logger.info("Inside forever while....")
      print("Inside Forever while...")
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
