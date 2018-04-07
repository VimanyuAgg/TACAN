

from __future__ import print_function
import sys
import grpc

import phase1_pb2
import phase1_pb2_grpc
import Node
import logging
from spanning_tree import SPANNING_INFO
import raspberryPi_id_list
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


def run():
    for key,value in raspberryPi_id_list.ID_IP_MAPPING.iteritems():
        channel = grpc.insecure_channel(value)
        stub = phase1_pb2_grpc.MainServiceStub(channel)
        clusterRPC = stub.StartPhase2Clustering(phase1_pb2.SendHello(nodeId, nodeHopcount, nodeState, nodeClusterheadId))
        logger.info("Node: %s got following response after sending Hello to child id: %s" % (nodeId, i))
        logger.info(clusterRPC)


if __name__ == '__main__':
	run()
