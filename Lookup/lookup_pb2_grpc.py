# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import lookup_pb2 as lookup__pb2


class MainServiceStub(object):
  """The Main service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Handshake = channel.unary_unary(
        '/lookup.MainService/Handshake',
        request_serializer=lookup__pb2.RequestMessage.SerializeToString,
        response_deserializer=lookup__pb2.ResponseMessage.FromString,
        )
    self.SendPacket = channel.unary_unary(
        '/lookup.MainService/SendPacket',
        request_serializer=lookup__pb2.RequestMessage.SerializeToString,
        response_deserializer=lookup__pb2.ResponseMessage.FromString,
        )
    self.Size = channel.unary_unary(
        '/lookup.MainService/Size',
        request_serializer=lookup__pb2.MySize.SerializeToString,
        response_deserializer=lookup__pb2.AccomodateChild.FromString,
        )
    self.Cluster = channel.unary_unary(
        '/lookup.MainService/Cluster',
        request_serializer=lookup__pb2.ClusterName.SerializeToString,
        response_deserializer=lookup__pb2.ClusterAck.FromString,
        )
    self.ShiftNodeRequest = channel.unary_unary(
        '/lookup.MainService/ShiftNodeRequest',
        request_serializer=lookup__pb2.ShiftRequest.SerializeToString,
        response_deserializer=lookup__pb2.ShiftResponse.FromString,
        )
    self.Jam = channel.unary_unary(
        '/lookup.MainService/Jam',
        request_serializer=lookup__pb2.JamRequest.SerializeToString,
        response_deserializer=lookup__pb2.JamResponse.FromString,
        )
    self.Hello = channel.unary_unary(
        '/lookup.MainService/Hello',
        request_serializer=lookup__pb2.sendHello.SerializeToString,
        response_deserializer=lookup__pb2.HelloResponse.FromString,
        )
    self.ShiftClusterRequest = channel.unary_unary(
        '/lookup.MainService/ShiftClusterRequest',
        request_serializer=lookup__pb2.ShiftClusterReq.SerializeToString,
        response_deserializer=lookup__pb2.ShiftClusterRes.FromString,
        )
    self.Accept = channel.unary_unary(
        '/lookup.MainService/Accept',
        request_serializer=lookup__pb2.AcceptRequest.SerializeToString,
        response_deserializer=lookup__pb2.AcceptResponse.FromString,
        )
    self.WakeUp = channel.unary_unary(
        '/lookup.MainService/WakeUp',
        request_serializer=lookup__pb2.wakeUpRequest.SerializeToString,
        response_deserializer=lookup__pb2.wakeUpResponse.FromString,
        )
    self.ShiftStart = channel.unary_unary(
        '/lookup.MainService/ShiftStart',
        request_serializer=lookup__pb2.ShiftStartRequest.SerializeToString,
        response_deserializer=lookup__pb2.ShiftStartResponse.FromString,
        )
    self.JoinNewParent = channel.unary_unary(
        '/lookup.MainService/JoinNewParent',
        request_serializer=lookup__pb2.JoinNewParentRequest.SerializeToString,
        response_deserializer=lookup__pb2.JoinNewParentResponse.FromString,
        )
    self.UpdateSize = channel.unary_unary(
        '/lookup.MainService/UpdateSize',
        request_serializer=lookup__pb2.UpdateSizeRequest.SerializeToString,
        response_deserializer=lookup__pb2.UpdateSizeResponse.FromString,
        )
    self.UpdateClusterhead = channel.unary_unary(
        '/lookup.MainService/UpdateClusterhead',
        request_serializer=lookup__pb2.UpdateClusterheadRequest.SerializeToString,
        response_deserializer=lookup__pb2.UpdateClusterheadResponse.FromString,
        )
    self.ShiftComplete = channel.unary_unary(
        '/lookup.MainService/ShiftComplete',
        request_serializer=lookup__pb2.SendShiftCompleteAck.SerializeToString,
        response_deserializer=lookup__pb2.ClusterheadAckSendShift.FromString,
        )
    self.RemoveChildIdFromParent = channel.unary_unary(
        '/lookup.MainService/RemoveChildIdFromParent',
        request_serializer=lookup__pb2.RemoveChildIdFromParentRequest.SerializeToString,
        response_deserializer=lookup__pb2.RemoveChildIdFromParentResponse.FromString,
        )
    self.Reject = channel.unary_unary(
        '/lookup.MainService/Reject',
        request_serializer=lookup__pb2.RejectRequest.SerializeToString,
        response_deserializer=lookup__pb2.RejectResponse.FromString,
        )
    self.ShiftFinished = channel.unary_unary(
        '/lookup.MainService/ShiftFinished',
        request_serializer=lookup__pb2.ShiftFinishedRequest.SerializeToString,
        response_deserializer=lookup__pb2.ShiftFinishedResponse.FromString,
        )
    self.Retrieve = channel.unary_unary(
        '/lookup.MainService/Retrieve',
        request_serializer=lookup__pb2.RedisRequest.SerializeToString,
        response_deserializer=lookup__pb2.ValAck.FromString,
        )
    self.Register = channel.unary_unary(
        '/lookup.MainService/Register',
        request_serializer=lookup__pb2.Params.SerializeToString,
        response_deserializer=lookup__pb2.RedisResponse.FromString,
        )


class MainServiceServicer(object):
  """The Main service definition.
  """

  def Handshake(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendPacket(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Size(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Cluster(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShiftNodeRequest(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Jam(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Hello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShiftClusterRequest(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Accept(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WakeUp(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShiftStart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def JoinNewParent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateSize(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateClusterhead(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShiftComplete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveChildIdFromParent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Reject(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShiftFinished(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Retrieve(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MainServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Handshake': grpc.unary_unary_rpc_method_handler(
          servicer.Handshake,
          request_deserializer=lookup__pb2.RequestMessage.FromString,
          response_serializer=lookup__pb2.ResponseMessage.SerializeToString,
      ),
      'SendPacket': grpc.unary_unary_rpc_method_handler(
          servicer.SendPacket,
          request_deserializer=lookup__pb2.RequestMessage.FromString,
          response_serializer=lookup__pb2.ResponseMessage.SerializeToString,
      ),
      'Size': grpc.unary_unary_rpc_method_handler(
          servicer.Size,
          request_deserializer=lookup__pb2.MySize.FromString,
          response_serializer=lookup__pb2.AccomodateChild.SerializeToString,
      ),
      'Cluster': grpc.unary_unary_rpc_method_handler(
          servicer.Cluster,
          request_deserializer=lookup__pb2.ClusterName.FromString,
          response_serializer=lookup__pb2.ClusterAck.SerializeToString,
      ),
      'ShiftNodeRequest': grpc.unary_unary_rpc_method_handler(
          servicer.ShiftNodeRequest,
          request_deserializer=lookup__pb2.ShiftRequest.FromString,
          response_serializer=lookup__pb2.ShiftResponse.SerializeToString,
      ),
      'Jam': grpc.unary_unary_rpc_method_handler(
          servicer.Jam,
          request_deserializer=lookup__pb2.JamRequest.FromString,
          response_serializer=lookup__pb2.JamResponse.SerializeToString,
      ),
      'Hello': grpc.unary_unary_rpc_method_handler(
          servicer.Hello,
          request_deserializer=lookup__pb2.sendHello.FromString,
          response_serializer=lookup__pb2.HelloResponse.SerializeToString,
      ),
      'ShiftClusterRequest': grpc.unary_unary_rpc_method_handler(
          servicer.ShiftClusterRequest,
          request_deserializer=lookup__pb2.ShiftClusterReq.FromString,
          response_serializer=lookup__pb2.ShiftClusterRes.SerializeToString,
      ),
      'Accept': grpc.unary_unary_rpc_method_handler(
          servicer.Accept,
          request_deserializer=lookup__pb2.AcceptRequest.FromString,
          response_serializer=lookup__pb2.AcceptResponse.SerializeToString,
      ),
      'WakeUp': grpc.unary_unary_rpc_method_handler(
          servicer.WakeUp,
          request_deserializer=lookup__pb2.wakeUpRequest.FromString,
          response_serializer=lookup__pb2.wakeUpResponse.SerializeToString,
      ),
      'ShiftStart': grpc.unary_unary_rpc_method_handler(
          servicer.ShiftStart,
          request_deserializer=lookup__pb2.ShiftStartRequest.FromString,
          response_serializer=lookup__pb2.ShiftStartResponse.SerializeToString,
      ),
      'JoinNewParent': grpc.unary_unary_rpc_method_handler(
          servicer.JoinNewParent,
          request_deserializer=lookup__pb2.JoinNewParentRequest.FromString,
          response_serializer=lookup__pb2.JoinNewParentResponse.SerializeToString,
      ),
      'UpdateSize': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateSize,
          request_deserializer=lookup__pb2.UpdateSizeRequest.FromString,
          response_serializer=lookup__pb2.UpdateSizeResponse.SerializeToString,
      ),
      'UpdateClusterhead': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateClusterhead,
          request_deserializer=lookup__pb2.UpdateClusterheadRequest.FromString,
          response_serializer=lookup__pb2.UpdateClusterheadResponse.SerializeToString,
      ),
      'ShiftComplete': grpc.unary_unary_rpc_method_handler(
          servicer.ShiftComplete,
          request_deserializer=lookup__pb2.SendShiftCompleteAck.FromString,
          response_serializer=lookup__pb2.ClusterheadAckSendShift.SerializeToString,
      ),
      'RemoveChildIdFromParent': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveChildIdFromParent,
          request_deserializer=lookup__pb2.RemoveChildIdFromParentRequest.FromString,
          response_serializer=lookup__pb2.RemoveChildIdFromParentResponse.SerializeToString,
      ),
      'Reject': grpc.unary_unary_rpc_method_handler(
          servicer.Reject,
          request_deserializer=lookup__pb2.RejectRequest.FromString,
          response_serializer=lookup__pb2.RejectResponse.SerializeToString,
      ),
      'ShiftFinished': grpc.unary_unary_rpc_method_handler(
          servicer.ShiftFinished,
          request_deserializer=lookup__pb2.ShiftFinishedRequest.FromString,
          response_serializer=lookup__pb2.ShiftFinishedResponse.SerializeToString,
      ),
      'Retrieve': grpc.unary_unary_rpc_method_handler(
          servicer.Retrieve,
          request_deserializer=lookup__pb2.RedisRequest.FromString,
          response_serializer=lookup__pb2.ValAck.SerializeToString,
      ),
      'Register': grpc.unary_unary_rpc_method_handler(
          servicer.Register,
          request_deserializer=lookup__pb2.Params.FromString,
          response_serializer=lookup__pb2.RedisResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'lookup.MainService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
