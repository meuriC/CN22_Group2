# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steam.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import users_pb2 as users__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bsteam.proto\x1a\x0busers.proto\")\n\x12\x41\x63tiveUsersRequest\x12\x13\n\x0bmax_results\x18\x01 \x01(\x05\"/\n\x13\x41\x63tiveUsersResponse\x12\x18\n\x05users\x18\x01 \x03(\x0b\x32\t.UserData2A\n\x05Steam\x12\x38\n\x0b\x41\x63tiveUsers\x12\x13.ActiveUsersRequest\x1a\x14.ActiveUsersResponseb\x06proto3')



_ACTIVEUSERSREQUEST = DESCRIPTOR.message_types_by_name['ActiveUsersRequest']
_ACTIVEUSERSRESPONSE = DESCRIPTOR.message_types_by_name['ActiveUsersResponse']
ActiveUsersRequest = _reflection.GeneratedProtocolMessageType('ActiveUsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVEUSERSREQUEST,
  '__module__' : 'steam_pb2'
  # @@protoc_insertion_point(class_scope:ActiveUsersRequest)
  })
_sym_db.RegisterMessage(ActiveUsersRequest)

ActiveUsersResponse = _reflection.GeneratedProtocolMessageType('ActiveUsersResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVEUSERSRESPONSE,
  '__module__' : 'steam_pb2'
  # @@protoc_insertion_point(class_scope:ActiveUsersResponse)
  })
_sym_db.RegisterMessage(ActiveUsersResponse)

_STEAM = DESCRIPTOR.services_by_name['Steam']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ACTIVEUSERSREQUEST._serialized_start=28
  _ACTIVEUSERSREQUEST._serialized_end=69
  _ACTIVEUSERSRESPONSE._serialized_start=71
  _ACTIVEUSERSRESPONSE._serialized_end=118
  _STEAM._serialized_start=120
  _STEAM._serialized_end=185
# @@protoc_insertion_point(module_scope)
