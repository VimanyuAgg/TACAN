from concurrent import futures
import time
import sys
import grpc
import lookup_pb2
import lookup_pb2_grpc
import thread

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


# import datetime
# import logging
# import os
# import logging.handlers

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# today_date = str(datetime.datetime.now()).split(" ")[0]
# current_path = os.path.dirname(os.path.realpath(__file__))


# debug_handler = logging.handlers.RotatingFileHandler(os.path.join(current_path+"/logs/", today_date+'-debug.log'),maxBytes=30000000,backupCount=40)
# debug_handler.setLevel(logging.DEBUG)

# info_handler = logging.handlers.RotatingFileHandler(os.path.join(current_path+"/logs/", today_date+'-info.log'),maxBytes=30000000,backupCount=40)
# info_handler.setLevel(logging.INFO)

# error_handler = logging.handlers.RotatingFileHandler(os.path.join(current_path+"/logs/", today_date+'-error.log'),maxBytes=300000,backupCount=40)
# error_handler.setLevel(logging.ERROR)

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# info_handler.setFormatter(formatter)
# error_handler.setFormatter(formatter)
# debug_handler.setFormatter(formatter)

# logger.addHandler(info_handler)
# logger.addHandler(error_handler)
# logger.addHandler(debug_handler)


class LookUpServer(lookup_pb2_grpc.MainServiceServicer):
  def __init__(self, lookup):
    self.lookup = lookup

  def Retrieve(self, request, context):
    result = lookup.retrive(request.key)
    return lookup_pb2.ValAck(value=result)

  def Register(self, request, context):
    resp = lookup.register(request.id, request.ip)
    return lookup_pb2.ResponseMessage(msg=resp)


def serve(lookup):
  print "inside serve"
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  print "thread created"
  try:
    lookup_pb2_grpc.add_MainServiceServicer_to_server(LookUpServer(lookup), server)
    print "MainServiceServicer_to_server"
    # update with ip of lookup
    server.add_insecure_port('[::]:50051')
    print "after insecure port"
    #  server.add_insecure_port('localhost:')
    # thread.start_new_thread(server.start(),())
    print "started"
    server.start()


  except Exception as e:
    print e
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)


if __name__ == '__main__':
  serve()
