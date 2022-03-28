# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: games.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bgames.proto\"J\n\tGamesData\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x03\x12\x10\n\x08\x61pp_name\x18\x02 \x01(\t\x12\x1b\n\x13game_reviews_number\x18\x03 \x01(\x03\"4\n\x0fGetGamesRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\"*\n\rGamesDataList\x12\x19\n\x05games\x18\x01 \x03(\x0b\x32\n.GamesData\"!\n\x0fGameByIdRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\"&\n\x12GamesByNameRequest\x12\x10\n\x08\x61pp_name\x18\x01 \x01(\t2\x92\x01\n\x05Games\x12,\n\x08GetGames\x12\x10.GetGamesRequest\x1a\x0e.GamesDataList\x12*\n\nSearchById\x12\x10.GameByIdRequest\x1a\n.GamesData\x12/\n\x0cSearchByName\x12\x13.GamesByNameRequest\x1a\n.GamesDatab\x06proto3')



_GAMESDATA = DESCRIPTOR.message_types_by_name['GamesData']
_GETGAMESREQUEST = DESCRIPTOR.message_types_by_name['GetGamesRequest']
_GAMESDATALIST = DESCRIPTOR.message_types_by_name['GamesDataList']
_GAMEBYIDREQUEST = DESCRIPTOR.message_types_by_name['GameByIdRequest']
_GAMESBYNAMEREQUEST = DESCRIPTOR.message_types_by_name['GamesByNameRequest']
GamesData = _reflection.GeneratedProtocolMessageType('GamesData', (_message.Message,), {
  'DESCRIPTOR' : _GAMESDATA,
  '__module__' : 'games_pb2'
  # @@protoc_insertion_point(class_scope:GamesData)
  })
_sym_db.RegisterMessage(GamesData)

GetGamesRequest = _reflection.GeneratedProtocolMessageType('GetGamesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGAMESREQUEST,
  '__module__' : 'games_pb2'
  # @@protoc_insertion_point(class_scope:GetGamesRequest)
  })
_sym_db.RegisterMessage(GetGamesRequest)

GamesDataList = _reflection.GeneratedProtocolMessageType('GamesDataList', (_message.Message,), {
  'DESCRIPTOR' : _GAMESDATALIST,
  '__module__' : 'games_pb2'
  # @@protoc_insertion_point(class_scope:GamesDataList)
  })
_sym_db.RegisterMessage(GamesDataList)

GameByIdRequest = _reflection.GeneratedProtocolMessageType('GameByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GAMEBYIDREQUEST,
  '__module__' : 'games_pb2'
  # @@protoc_insertion_point(class_scope:GameByIdRequest)
  })
_sym_db.RegisterMessage(GameByIdRequest)

GamesByNameRequest = _reflection.GeneratedProtocolMessageType('GamesByNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _GAMESBYNAMEREQUEST,
  '__module__' : 'games_pb2'
  # @@protoc_insertion_point(class_scope:GamesByNameRequest)
  })
_sym_db.RegisterMessage(GamesByNameRequest)

_GAMES = DESCRIPTOR.services_by_name['Games']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GAMESDATA._serialized_start=15
  _GAMESDATA._serialized_end=89
  _GETGAMESREQUEST._serialized_start=91
  _GETGAMESREQUEST._serialized_end=143
  _GAMESDATALIST._serialized_start=145
  _GAMESDATALIST._serialized_end=187
  _GAMEBYIDREQUEST._serialized_start=189
  _GAMEBYIDREQUEST._serialized_end=222
  _GAMESBYNAMEREQUEST._serialized_start=224
  _GAMESBYNAMEREQUEST._serialized_end=262
  _GAMES._serialized_start=265
  _GAMES._serialized_end=411
# @@protoc_insertion_point(module_scope)
