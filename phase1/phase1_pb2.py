# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: phase1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='phase1.proto',
  package='phase1',
  syntax='proto3',
  serialized_pb=_b('\n\x0cphase1.proto\x12\x06phase1\"o\n\tsendHello\x12\x10\n\x08senderId\x18\x01 \x01(\t\x12\x1e\n\x16hopToSenderClusterhead\x18\x02 \x01(\x05\x12\x13\n\x0bsenderState\x18\x03 \x01(\t\x12\x1b\n\x13senderClusterheadId\x18\x04 \x01(\t\"#\n\rHelloResponse\x12\x12\n\ninterested\x18\x01 \x01(\x05\"\x1c\n\nJamRequest\x12\x0e\n\x06nodeId\x18\x01 \x01(\x05\"\"\n\x0bJamResponse\x12\x13\n\x0bjamResponse\x18\x01 \x01(\t\"/\n\x0b\x43lusterName\x12\x13\n\x0b\x63lusterName\x18\x01 \x01(\t\x12\x0b\n\x03hop\x18\x02 \x01(\x05\" \n\nClusterAck\x12\x12\n\nclusterAck\x18\x01 \x01(\t\"\x16\n\x06MySize\x12\x0c\n\x04size\x18\x01 \x01(\x05\"\"\n\x0f\x41\x63\x63omodateChild\x12\x0f\n\x07message\x18\x01 \x01(\t\"H\n\x0eRequestMessage\x12\x0e\n\x06nodeId\x18\x01 \x01(\t\x12\x15\n\rdestinationId\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"L\n\x0fResponseMessage\x12\x0e\n\x06nodeId\x18\x01 \x01(\t\x12\x15\n\rdestinationId\x18\x02 \x01(\t\x12\x12\n\nackMessage\x18\x03 \x01(\t2\xde\x02\n\x0bMainService\x12>\n\tHandshake\x12\x16.phase1.RequestMessage\x1a\x17.phase1.ResponseMessage\"\x00\x12?\n\nSendPacket\x12\x16.phase1.RequestMessage\x1a\x17.phase1.ResponseMessage\"\x00\x12\x31\n\x04Size\x12\x0e.phase1.MySize\x1a\x17.phase1.AccomodateChild\"\x00\x12\x34\n\x07\x43luster\x12\x13.phase1.ClusterName\x1a\x12.phase1.ClusterAck\"\x00\x12\x30\n\x03Jam\x12\x12.phase1.JamRequest\x1a\x13.phase1.JamResponse\"\x00\x12\x33\n\x05Hello\x12\x11.phase1.sendHello\x1a\x15.phase1.HelloResponse\"\x00\x62\x06proto3')
)




_SENDHELLO = _descriptor.Descriptor(
  name='sendHello',
  full_name='phase1.sendHello',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='senderId', full_name='phase1.sendHello.senderId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hopToSenderClusterhead', full_name='phase1.sendHello.hopToSenderClusterhead', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='senderState', full_name='phase1.sendHello.senderState', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='senderClusterheadId', full_name='phase1.sendHello.senderClusterheadId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=135,
)


_HELLORESPONSE = _descriptor.Descriptor(
  name='HelloResponse',
  full_name='phase1.HelloResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='interested', full_name='phase1.HelloResponse.interested', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=172,
)


_JAMREQUEST = _descriptor.Descriptor(
  name='JamRequest',
  full_name='phase1.JamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodeId', full_name='phase1.JamRequest.nodeId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=202,
)


_JAMRESPONSE = _descriptor.Descriptor(
  name='JamResponse',
  full_name='phase1.JamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jamResponse', full_name='phase1.JamResponse.jamResponse', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=238,
)


_CLUSTERNAME = _descriptor.Descriptor(
  name='ClusterName',
  full_name='phase1.ClusterName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clusterName', full_name='phase1.ClusterName.clusterName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hop', full_name='phase1.ClusterName.hop', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=287,
)


_CLUSTERACK = _descriptor.Descriptor(
  name='ClusterAck',
  full_name='phase1.ClusterAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clusterAck', full_name='phase1.ClusterAck.clusterAck', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=321,
)


_MYSIZE = _descriptor.Descriptor(
  name='MySize',
  full_name='phase1.MySize',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='phase1.MySize.size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=323,
  serialized_end=345,
)


_ACCOMODATECHILD = _descriptor.Descriptor(
  name='AccomodateChild',
  full_name='phase1.AccomodateChild',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='phase1.AccomodateChild.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=347,
  serialized_end=381,
)


_REQUESTMESSAGE = _descriptor.Descriptor(
  name='RequestMessage',
  full_name='phase1.RequestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodeId', full_name='phase1.RequestMessage.nodeId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destinationId', full_name='phase1.RequestMessage.destinationId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='phase1.RequestMessage.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=383,
  serialized_end=455,
)


_RESPONSEMESSAGE = _descriptor.Descriptor(
  name='ResponseMessage',
  full_name='phase1.ResponseMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodeId', full_name='phase1.ResponseMessage.nodeId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destinationId', full_name='phase1.ResponseMessage.destinationId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ackMessage', full_name='phase1.ResponseMessage.ackMessage', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=457,
  serialized_end=533,
)

DESCRIPTOR.message_types_by_name['sendHello'] = _SENDHELLO
DESCRIPTOR.message_types_by_name['HelloResponse'] = _HELLORESPONSE
DESCRIPTOR.message_types_by_name['JamRequest'] = _JAMREQUEST
DESCRIPTOR.message_types_by_name['JamResponse'] = _JAMRESPONSE
DESCRIPTOR.message_types_by_name['ClusterName'] = _CLUSTERNAME
DESCRIPTOR.message_types_by_name['ClusterAck'] = _CLUSTERACK
DESCRIPTOR.message_types_by_name['MySize'] = _MYSIZE
DESCRIPTOR.message_types_by_name['AccomodateChild'] = _ACCOMODATECHILD
DESCRIPTOR.message_types_by_name['RequestMessage'] = _REQUESTMESSAGE
DESCRIPTOR.message_types_by_name['ResponseMessage'] = _RESPONSEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

sendHello = _reflection.GeneratedProtocolMessageType('sendHello', (_message.Message,), dict(
  DESCRIPTOR = _SENDHELLO,
  __module__ = 'phase1_pb2'
  # @@protoc_insertion_point(class_scope:phase1.sendHello)
  ))
_sym_db.RegisterMessage(sendHello)

HelloResponse = _reflection.GeneratedProtocolMessageType('HelloResponse', (_message.Message,), dict(
  DESCRIPTOR = _HELLORESPONSE,
  __module__ = 'phase1_pb2'
  # @@protoc_insertion_point(class_scope:phase1.HelloResponse)
  ))
_sym_db.RegisterMessage(HelloResponse)

JamRequest = _reflection.GeneratedProtocolMessageType('JamRequest', (_message.Message,), dict(
  DESCRIPTOR = _JAMREQUEST,
  __module__ = 'phase1_pb2'
  # @@protoc_insertion_point(class_scope:phase1.JamRequest)
  ))
_sym_db.RegisterMessage(JamRequest)

JamResponse = _reflection.GeneratedProtocolMessageType('JamResponse', (_message.Message,), dict(
  DESCRIPTOR = _JAMRESPONSE,
  __module__ = 'phase1_pb2'
  # @@protoc_insertion_point(class_scope:phase1.JamResponse)
  ))
_sym_db.RegisterMessage(JamResponse)

ClusterName = _reflection.GeneratedProtocolMessageType('ClusterName', (_message.Message,), dict(
  DESCRIPTOR = _CLUSTERNAME,
  __module__ = 'phase1_pb2'
  # @@protoc_insertion_point(class_scope:phase1.ClusterName)
  ))
_sym_db.RegisterMessage(ClusterName)

ClusterAck = _reflection.GeneratedProtocolMessageType('ClusterAck', (_message.Message,), dict(
  DESCRIPTOR = _CLUSTERACK,
  __module__ = 'phase1_pb2'
  # @@protoc_insertion_point(class_scope:phase1.ClusterAck)
  ))
_sym_db.RegisterMessage(ClusterAck)

MySize = _reflection.GeneratedProtocolMessageType('MySize', (_message.Message,), dict(
  DESCRIPTOR = _MYSIZE,
  __module__ = 'phase1_pb2'
  # @@protoc_insertion_point(class_scope:phase1.MySize)
  ))
_sym_db.RegisterMessage(MySize)

AccomodateChild = _reflection.GeneratedProtocolMessageType('AccomodateChild', (_message.Message,), dict(
  DESCRIPTOR = _ACCOMODATECHILD,
  __module__ = 'phase1_pb2'
  # @@protoc_insertion_point(class_scope:phase1.AccomodateChild)
  ))
_sym_db.RegisterMessage(AccomodateChild)

RequestMessage = _reflection.GeneratedProtocolMessageType('RequestMessage', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTMESSAGE,
  __module__ = 'phase1_pb2'
  # @@protoc_insertion_point(class_scope:phase1.RequestMessage)
  ))
_sym_db.RegisterMessage(RequestMessage)

ResponseMessage = _reflection.GeneratedProtocolMessageType('ResponseMessage', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEMESSAGE,
  __module__ = 'phase1_pb2'
  # @@protoc_insertion_point(class_scope:phase1.ResponseMessage)
  ))
_sym_db.RegisterMessage(ResponseMessage)



_MAINSERVICE = _descriptor.ServiceDescriptor(
  name='MainService',
  full_name='phase1.MainService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=536,
  serialized_end=886,
  methods=[
  _descriptor.MethodDescriptor(
    name='Handshake',
    full_name='phase1.MainService.Handshake',
    index=0,
    containing_service=None,
    input_type=_REQUESTMESSAGE,
    output_type=_RESPONSEMESSAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendPacket',
    full_name='phase1.MainService.SendPacket',
    index=1,
    containing_service=None,
    input_type=_REQUESTMESSAGE,
    output_type=_RESPONSEMESSAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Size',
    full_name='phase1.MainService.Size',
    index=2,
    containing_service=None,
    input_type=_MYSIZE,
    output_type=_ACCOMODATECHILD,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Cluster',
    full_name='phase1.MainService.Cluster',
    index=3,
    containing_service=None,
    input_type=_CLUSTERNAME,
    output_type=_CLUSTERACK,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Jam',
    full_name='phase1.MainService.Jam',
    index=4,
    containing_service=None,
    input_type=_JAMREQUEST,
    output_type=_JAMRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Hello',
    full_name='phase1.MainService.Hello',
    index=5,
    containing_service=None,
    input_type=_SENDHELLO,
    output_type=_HELLORESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAINSERVICE)

DESCRIPTOR.services_by_name['MainService'] = _MAINSERVICE

# @@protoc_insertion_point(module_scope)
