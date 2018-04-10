
from concurrent import futures
import time
import sys
import grpc
import client
import phase1_pb2
import phase1_pb2_grpc
import raspberryPi_id_list
import threading

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
          self.node.childRequestCounter += 1

          ### DONE #####
          #### Move removing the child above sendSizeToParent as parent might send cluster but child needs to be removed
          ###### Case of Node 0 and Node 1 (12 node cluster)
          try:
              self.node.childListId.remove(request.nodeId)
          except Exception as e:
              logger.error("ERROR OCCURRED WHILE KICKING CHILDREN")
              logger.error("Node id: %s was kicking child %s from childList" % (self.node.id, request.nodeId))
          logger.info("Node id: %s removed child %s from childList" % (self.node.id, request.nodeId))

          logger.info("Node id: %s Sending Prune after checking if all children responded or not"%(self.node.id))
          if self.node.childRequestCounter == self.node.initialNodeChildLength:
              logger.info("Node id: %s All children responded. Sending size to parent"%(self.node.id))
              thread1 = threading.Thread(target=self.node.sendSizeToParent,args=())
              thread1.start()

          logger.info("Node: %s Sending Prune"%(self.node.id))
          return phase1_pb2.AccomodateChild(message="Prune")
      else:
        logger.info("Sending Accept after checking if all children responded or not")
        self.node.size += childSize
        logger.info("Node %s: new size is %s"%(self.node.id,self.node.size))
        self.node.childRequestCounter += 1
        if self.node.childListId != None and self.node.childRequestCounter == self.node.initialNodeChildLength:
            logger.info("All children responded. Sending size to parent")
            thread2 = threading.Thread(target=self.node.sendSizeToParent, args=())
            thread2.start()

        logger.info("Node: %s Sending accept to child" % (self.node.id))
        return phase1_pb2.AccomodateChild(message="Accepted")

    except Exception as e:
      logger.error(e)



  def JoinCluster(self, request, context):
      logger.debug("Got Cluster message as server Node:%s"%(self.node.id))
      clusterName = request.clusterHeadName
      hopCount = request.hopcount
      self.node.clusterheadId= clusterName
      self.node.state = "active"
      self.node.hopcount= hopCount
      print("Server Node: "+str(self.node.id)+" is now joining Clusterleader "+str(clusterName))
      logger.info("Server Node: "+str(self.node.id)+" is now joining Clusterleader "+str(clusterName))
      if(self.node.childListId != None):
          logger.info("Server Node:%s has children. Starting ClusterheadId Propagation"%(self.node.id))
          thread3 = threading.Thread(target=self.node.propogateClusterheadInfo,args=(clusterName, hopCount))
          thread3.start()
      else:
          logger.info("Server Node: has NO children.")
      return phase1_pb2.JoinClusterResponse(joinClusterResponse="Joined")

  def ShiftNodeRequest(self,request,context):
    logger.info("ClusterheadId: %s got ShiftNodeRequest from node id: %s"%(self.node.id,request.nodeId))
    if self.node.isClusterhead and self.node.state == "free":
      #saving the info about this node
      self.node.state = "busy"
      self.node.shiftNodeId = request.nodeId
      self.node.shiftNodeSum = request.sumOfweight
      self.node.shiftNodeCluster = request.clusterHeadId
      #send jam request
      logger.info("ClusterheadId: %s sending Jam Signal across its cluster"%(self.node.id))
      self.node.sendJamSignal()
      #send shift_cluster_request to Cj
      logger.info("ClusterheadId: %s successfully sent Jam Signal across its cluster" % (self.node.id))
      logger.info("ClusterheadId: %s now sending sendShiftClusterRequest" % (self.node.id))
      self.node.sendShiftClusterRequest()
      return phase1_pb2.ShiftResponse(message="Recieved ShiftNode Request")
    else:
      logger.info("ClusterheadId: %s is not free for accomodating ShiftNodeRequest from node id: %s" % (self.node.id, request.nodeId))
      return phase1_pb2.ShiftResponse(message="Not approving ShiftNode Request")

      
  def Jam(self,request,context):
    jamId = request.nodeId
    logger.info("Node: %s received Jam signal from clusterheadId: %s"%(self.node.id,jamId))
    if (self.node.isClusterhead != 1):
      logger.info("Node: %s going to sleep zzzzzzzz"%(self.node.id))
      self.node.state = "sleep"
      logger.info("Node: %s sending jam to all children" % (self.node.id))
      self.node.propagateJamToChildren(jamId)
      logger.info("Node: %s successfully propagated jam to all children" % (self.node.id))
    return phase1_pb2.JamResponse(jamResponse="jammed")

  def Hello(self,request,context):
    if (self.node.isClusterhead == 1):
      #do nothing
      logger.info("Node: %s got hello message from senderId: %s" % (self.node.id,request.senderId))
      logger.info("Node: %s I am clusterhead. Sending Not interested"%(self.node.id))
      return phase1_pb2.HelloResponse(interested=-1)
    if (self.node.state == "active"):
      logger.info("Node: %s is active"%(self.node.id))
      self.node.neighbourHelloArray.add(request.senderId)
      logger.info("Node %s printing neighbourHelloArray"%(self.node.id))
      logger.info(self.node.neighbourHelloArray)
      logger.info("Node: %s has hopCount=%d with bestHopCount: %d and senderId: %s has hopCount %d"%(self.node.id,\
                                                                                                    self.node.hopcount,\
                                                                                                    self.node.bestNodeHopCount,\
                                                                                                    request.senderId,request.hopToSenderClusterhead))
      if (self.node.clusterheadId != request.senderClusterheadId and self.node.bestNodeHopCount > request.hopToSenderClusterhead):
        logger.info("Node: %s updating bestNode as senderId: %s looks relevant choice as new parent"%(self.node.id,request.senderId))
        self.node.bestNodeId = request.senderId
        self.node.bestNodeHopCount = request.hopToSenderClusterhead
        self.node.bestNodeClusterHeadId = request.senderClusterheadId


        if (len(self.node.neighbourHelloArray) == 8 and self.node.bestNodeId != self.node.id):
            ## May need to add self.bestNodeHopCount in the sendShiftRPC to update self.node.hopcount if request is accepted
            logger.info("Node: %s got all helloes from neighbours. Sending shift node request to would be ex-clusterheadId:%s"%(self.node.id,self.node.clusterheadId))

            self.node.sendShiftNodeRequest(self.node.bestNodeClusterHeadId)
        logger.info("Node: %s sending interested response for senderId: %s"%(self.node.id,request.senderId))
        return phase1_pb2.HelloResponse(interested=1)

      if (len(self.node.neighbourHelloArray) == 8 and self.node.bestNodeId != self.node.id):
        ## May need to add self.bestNodeHopCount in the sendShiftRPC to update self.node.hopcount if request is accepted
        logger.info(
            "Node: %s got all helloes from neighbours. Sending shift node request to would be ex-clusterheadId:%s" % (
            self.node.id, self.node.bestNodeClusterHeadId))
        self.node.sendShiftNodeRequest(self.node.bestNodeClusterHeadId)

        # send interested -1
      logger.info("Node: %s sending NOT - interested response for senderId: %s" % (self.node.id, request.senderId))
      return phase1_pb2.HelloResponse(interested=-1)
    else:
      # send interested -1
      logger.info("Node: %s sending NOT - interested response for senderId: %s" % (self.node.id, request.senderId))
      phase1_pb2.HelloResponse(interested=-1)

  def ShiftClusterRequest(self,request,context):
    if self.node.isClusterhead and self.node.state == "free":
      #check size bound condition
      if self.node.size + request.sumOfweights > raspberryPi_id_list.THRESHOLD_S:
        # send reject to Ci
        logger.info("Node: %s is rejecting ShiftClusterRequest from \
        clusterheadId: %s regarding node: %s"%(self.node.id,request.senderClusterHeadId,request.senderNodeId))
        self.node.reject(request.senderClusterHeadId)
        return phase1_pb2.ShiftClusterRes(message= "Rejecting") 
      else:
        self.node.shiftNodeId=request.senderNodeId
        self.node.shiftNodeCluster=request.senderClusterHeadId
        self.node.shiftNodeSum=request.sumOfweights
        # set state to busy
        self.node.state = "busy"
        #send jam to all nodes in cluster
        self.node.sendJamSignal()
        #accept to Ci
        logger.info("Node: %s is accepting ShiftClusterRequest from clusterheadId: %s regarding node: %s" %(self.node.id, request.senderClusterHeadId, request.senderNodeId))
        self.node.accept(request.senderClusterHeadId)
        return phase1_pb2.ShiftClusterRes(message= "Accepting") 
    else:
      #send reject as shifting is already on
      self.node.reject(request.senderClusterHeadId)
      return phase1_pb2.ShiftClusterRes(message= "Rejecting")
       
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
          self.node.updateInternalVariablesAndSendJoin(self.node.bestNodeId,self.node.bestNodeClusterHeadId,\
                                                       self.node.bestNodeHopCount + 1)
          self.node.propagateNewClusterHeadToChildren()
          # is sendShiftCompleteToBothClusterHeads it necessary - can remove if not needed
          self.node.sendShiftCompleteToBothClusterHeads(oldClusterheadId,self.node.clusterheadId)
          return phase1_pb2.ShiftStartResponse(shifStartResponse="byebye")
      else:
          return phase1_pb2.ShiftStartResponse(shifStartResponse="ShiftStart Sent to Wrong Node")


  # As a parent, add new child to myChild and update size
  # Also inform parents about size addition
  def JoinNewParent(self,request,context):
    if self.node.state == "sleep":
      self.node.childListId.append(request.nodeId)
      sizeIncrement = request.childSize
      self.node.size += request.childSize
      self.node.informParentAboutNewSize(sizeIncrement)
    elif self.node.isClusterhead and self.node.state == "busy":
      self.node.childListId.append(request.nodeId)
      sizeIncrement = request.childSize
      self.node.size += request.childSize
    return phase1_pb2.JoinNewParentResponse(joinResponse="welcome my new child")

  def UpdateSize(self,request,context):
      self.node.size += request.sizeIncrement
      self.node.informParentAboutNewSize(request.sizeIncrement)
      return phase1_pb2.UpdateSizeResponse(updateSizeResponse = "updated size")

  def UpdateClusterhead(self,request,context):
      self.node.clusterheadId = request.newClusterheadId
      self.node.propagateNewClusterHeadToChildren()
      return phase1_pb2.UpdateClusterheadResponse(updateClusterheadResponse = "clusterhead Updated")

  def ShiftComplete(self,request,context):
      logger.info("ClusterheadId: %s got SendShiftComplete rpc with message:%s"%(self.node.id,request.sendShiftCompleteAck))
      self.node.sendWakeup()
      self.node.state ="free"
      return phase1_pb2.ClusterheadAckSendShift(clusterheadAckSendShift = "ClusterheadId: %s acknowledged shift.."%(self.node.id))

  def RemoveChildIdFromParent(self,request,context):
      logger.info("Parent: %s got RemoveChildIdFromParent rpc from Node:%s" % (self.node.id, request.departingChildId))
      logger.info("Parent: %s has below children before removal" % (self.node.id))
      logger.info(self.node.childListId)
      self.node.childListId.remove(request.departingChildId)
      logger.info("Parent: %s has below children after removal"%(self.node.id))
      logger.info(self.node.childListId)
      return phase1_pb2.RemoveChildIdFromParentResponse(removeChildIdFromParentResponse= "Removed")

  def Accept(self,request,context):
      if self.node.state == "busy":
        logger.info("Accept Request recieved from clusterhead " % (request.clusterHeadId))
      # send shift start to the i node if energy matric reduces
      #   if energyvalue < currentValue:
        if True:
          self.node.sendShiftStart()
          return phase1_pb2.AcceptResponse(message= "Starting Shift Start")
        else:
          self.node.sendWakeup()
          self.node.sendShiftFinished()
          self.node.state ="free"
          return phase1_pb2.AcceptResponse(message= "Starting Shift Finished")
      else:
        return phase1_pb2.AcceptResponse(message= "Not in busy state for now !")


  def Reject(self,request,context):
    if self.node.state=="busy":
      #send wakeup to all nodes in cluster
      self.node.state="free"
      self.node.sendWakeup()
      return phase1_pb2.RejectResponse(message= "Thanks for Rejecting")
    else:
      return phase1_pb2.RejectResponse(message= "Not in busy state for now !")

  def ShiftFinished(self,request,context):
    if self.node.state=="busy":
      self.node.sendWakeup()
      self.node.state ="free"
    return phase1_pb2.ShiftFinishedResponse(message= "Finished")

  def StartPhase2Clustering(self,request,context):
      logger.info("Node: %s got StartPhase2Clustering"%(self.node.id))
      self.node.startPhase2Clustering()
      response = "Node: %s done with phase2 clustering"%self.node.id
      return phase1_pb2.StartedPhase2ClusteringResponse(startedPhase2ClusteringResponse = response)

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
    server.start()
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
