# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0busers.proto\"\"\n\x0fUsernameRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"&\n\x11\x43reateUserRequest\x12\x11\n\tuser_name\x18\x01 \x01(\t\"%\n\x0fGetUsersRequest\x12\x12\n\nmax_result\x18\x01 \x01(\x05\"K\n\x08UserData\x12\x11\n\tnick_name\x18\x01 \x01(\t\x12\x13\n\x0bnum_reviews\x18\x02 \x01(\x05\x12\x17\n\x0fnum_games_owned\x18\x03 \x01(\x05\")\n\rUsersDataList\x12\x18\n\x05users\x18\x01 \x03(\x0b\x32\t.UserData\"\x84\x02\n\x12\x43reateUserResponse\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x1c\n\x14user_num_games_owned\x18\x03 \x01(\x05\x12\x18\n\x10user_num_reviews\x18\x04 \x01(\x05\x12\x1d\n\x15user_playtime_forever\x18\x05 \x01(\x05\x12$\n\x1cuser_playtime_last_two_weeks\x18\x06 \x01(\x05\x12\x1f\n\x17user_playtime_at_review\x18\x07 \x01(\x05\x12\x1a\n\x12\x61uthor_last_played\x18\x08 \x01(\x05\x12\x10\n\x08user_pwd\x18\t \x01(\t2\x94\x01\n\x05Users\x12&\n\x07GetUser\x12\x10.UsernameRequest\x1a\t.UserData\x12\x35\n\nCreateUser\x12\x12.CreateUserRequest\x1a\x13.CreateUserResponse\x12,\n\x08GetUsers\x12\x10.GetUsersRequest\x1a\x0e.UsersDataListb\x06proto3')



_USERNAMEREQUEST = DESCRIPTOR.message_types_by_name['UsernameRequest']
_CREATEUSERREQUEST = DESCRIPTOR.message_types_by_name['CreateUserRequest']
_GETUSERSREQUEST = DESCRIPTOR.message_types_by_name['GetUsersRequest']
_USERDATA = DESCRIPTOR.message_types_by_name['UserData']
_USERSDATALIST = DESCRIPTOR.message_types_by_name['UsersDataList']
_CREATEUSERRESPONSE = DESCRIPTOR.message_types_by_name['CreateUserResponse']
UsernameRequest = _reflection.GeneratedProtocolMessageType('UsernameRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERNAMEREQUEST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:UsernameRequest)
  })
_sym_db.RegisterMessage(UsernameRequest)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

GetUsersRequest = _reflection.GeneratedProtocolMessageType('GetUsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERSREQUEST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:GetUsersRequest)
  })
_sym_db.RegisterMessage(GetUsersRequest)

UserData = _reflection.GeneratedProtocolMessageType('UserData', (_message.Message,), {
  'DESCRIPTOR' : _USERDATA,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:UserData)
  })
_sym_db.RegisterMessage(UserData)

UsersDataList = _reflection.GeneratedProtocolMessageType('UsersDataList', (_message.Message,), {
  'DESCRIPTOR' : _USERSDATALIST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:UsersDataList)
  })
_sym_db.RegisterMessage(UsersDataList)

CreateUserResponse = _reflection.GeneratedProtocolMessageType('CreateUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERRESPONSE,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:CreateUserResponse)
  })
_sym_db.RegisterMessage(CreateUserResponse)

_USERS = DESCRIPTOR.services_by_name['Users']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERNAMEREQUEST._serialized_start=15
  _USERNAMEREQUEST._serialized_end=49
  _CREATEUSERREQUEST._serialized_start=51
  _CREATEUSERREQUEST._serialized_end=89
  _GETUSERSREQUEST._serialized_start=91
  _GETUSERSREQUEST._serialized_end=128
  _USERDATA._serialized_start=130
  _USERDATA._serialized_end=205
  _USERSDATALIST._serialized_start=207
  _USERSDATALIST._serialized_end=248
  _CREATEUSERRESPONSE._serialized_start=251
  _CREATEUSERRESPONSE._serialized_end=511
  _USERS._serialized_start=514
  _USERS._serialized_end=662
# @@protoc_insertion_point(module_scope)
