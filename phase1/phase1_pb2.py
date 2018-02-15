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
  serialized_pb=_b('\n\x0cphase1.proto\x12\x06phase1\"\"\n\x0b\x43lusterName\x12\x13\n\x0b\x63lusterName\x18\x01 \x01(\t\" \n\nClusterAck\x12\x12\n\nclusterAck\x18\x01 \x01(\t\"\x16\n\x06MySize\x12\x0c\n\x04size\x18\x01 \x01(\x05\"\"\n\x0f\x41\x63\x63omodateChild\x12\x0f\n\x07message\x18\x01 \x01(\t\"H\n\x0eRequestMessage\x12\x0e\n\x06nodeId\x18\x01 \x01(\t\x12\x15\n\rdestinationId\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"L\n\x0fResponseMessage\x12\x0e\n\x06nodeId\x18\x01 \x01(\t\x12\x15\n\rdestinationId\x18\x02 \x01(\t\x12\x12\n\nackMessage\x18\x03 \x01(\t2\xf7\x01\n\x0bMainService\x12>\n\tHandshake\x12\x16.phase1.RequestMessage\x1a\x17.phase1.ResponseMessage\"\x00\x12?\n\nSendPacket\x12\x16.phase1.RequestMessage\x1a\x17.phase1.ResponseMessage\"\x00\x12\x31\n\x04Size\x12\x0e.phase1.MySize\x1a\x17.phase1.AccomodateChild\"\x00\x12\x34\n\x07\x43luster\x12\x13.phase1.ClusterName\x1a\x12.phase1.ClusterAck\"\x00\x62\x06proto3')
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
  serialized_end=58,
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
  serialized_start=60,
  serialized_end=92,
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
  serialized_start=94,
  serialized_end=116,
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
  serialized_start=118,
  serialized_end=152,
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
  serialized_start=154,
  serialized_end=226,
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
  serialized_start=228,
  serialized_end=304,
)

DESCRIPTOR.message_types_by_name['ClusterName'] = _CLUSTERNAME
DESCRIPTOR.message_types_by_name['ClusterAck'] = _CLUSTERACK
DESCRIPTOR.message_types_by_name['MySize'] = _MYSIZE
DESCRIPTOR.message_types_by_name['AccomodateChild'] = _ACCOMODATECHILD
DESCRIPTOR.message_types_by_name['RequestMessage'] = _REQUESTMESSAGE
DESCRIPTOR.message_types_by_name['ResponseMessage'] = _RESPONSEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

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
  serialized_start=307,
  serialized_end=554,
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
])
_sym_db.RegisterServiceDescriptor(_MAINSERVICE)

DESCRIPTOR.services_by_name['MainService'] = _MAINSERVICE

# @@protoc_insertion_point(module_scope)
