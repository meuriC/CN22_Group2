# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reviews.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rreviews.proto\"&\n\x11ReviewByIdRequest\x12\x11\n\treview_id\x18\x01 \x01(\t\";\n\x14ReviewsByGameRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\"Q\n\x17UpdateReviewByIdRequest\x12\x11\n\treview_id\x18\x01 \x01(\t\x12\x0e\n\x06review\x18\x02 \x01(\t\x12\x13\n\x0brecommended\x18\x03 \x01(\t\"L\n UpdateHelpfulOnReviewByIdRequest\x12\x11\n\treview_id\x18\x01 \x01(\t\x12\x15\n\rvotes_helpful\x18\x02 \x01(\t\"A\n\x18ReviewsByLanguageRequest\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\"F\n\x16ReviewsByUserIdRequest\x12\x17\n\x0f\x61uthor_steam_id\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\"E\n\x17ReviewsByHelpfulRequest\x12\x15\n\rvotes_helpful\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\"\xcc\x01\n\nReviewData\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\x12\x11\n\treview_id\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\t\x12\x0e\n\x06review\x18\x04 \x01(\t\x12\x19\n\x11timestamp_created\x18\x05 \x01(\t\x12\x19\n\x11timestamp_updated\x18\x06 \x01(\t\x12\x13\n\x0brecommended\x18\x07 \x01(\t\x12\x15\n\rvotes_helpful\x18\x08 \x01(\t\x12\x17\n\x0f\x61uthor_steam_id\x18\t \x01(\t\"2\n\x12ReviewDataResponse\x12\x1c\n\x07reviews\x18\x01 \x03(\x0b\x32\x0b.ReviewData\"&\n\x14\x44\x65leteReviewResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x32\xf8\x03\n\x07Reviews\x12,\n\tGetReview\x12\x12.ReviewByIdRequest\x1a\x0b.ReviewData\x12<\n\x0eGetGameReviews\x12\x15.ReviewsByGameRequest\x1a\x13.ReviewDataResponse\x12\x32\n\tPutReview\x12\x18.UpdateReviewByIdRequest\x1a\x0b.ReviewData\x12\x39\n\x0c\x44\x65leteReview\x12\x12.ReviewByIdRequest\x1a\x15.DeleteReviewResponse\x12\x42\n\x10PutHelpfulReview\x12!.UpdateHelpfulOnReviewByIdRequest\x1a\x0b.ReviewData\x12\x46\n\x14GetReviewsByLanguage\x12\x19.ReviewsByLanguageRequest\x1a\x13.ReviewDataResponse\x12@\n\x10GetReviewsByUser\x12\x17.ReviewsByUserIdRequest\x1a\x13.ReviewDataResponse\x12\x44\n\x13GetReviewsByHelpful\x12\x18.ReviewsByHelpfulRequest\x1a\x13.ReviewDataResponseb\x06proto3')



_REVIEWBYIDREQUEST = DESCRIPTOR.message_types_by_name['ReviewByIdRequest']
_REVIEWSBYGAMEREQUEST = DESCRIPTOR.message_types_by_name['ReviewsByGameRequest']
_UPDATEREVIEWBYIDREQUEST = DESCRIPTOR.message_types_by_name['UpdateReviewByIdRequest']
_UPDATEHELPFULONREVIEWBYIDREQUEST = DESCRIPTOR.message_types_by_name['UpdateHelpfulOnReviewByIdRequest']
_REVIEWSBYLANGUAGEREQUEST = DESCRIPTOR.message_types_by_name['ReviewsByLanguageRequest']
_REVIEWSBYUSERIDREQUEST = DESCRIPTOR.message_types_by_name['ReviewsByUserIdRequest']
_REVIEWSBYHELPFULREQUEST = DESCRIPTOR.message_types_by_name['ReviewsByHelpfulRequest']
_REVIEWDATA = DESCRIPTOR.message_types_by_name['ReviewData']
_REVIEWDATARESPONSE = DESCRIPTOR.message_types_by_name['ReviewDataResponse']
_DELETEREVIEWRESPONSE = DESCRIPTOR.message_types_by_name['DeleteReviewResponse']
ReviewByIdRequest = _reflection.GeneratedProtocolMessageType('ReviewByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWBYIDREQUEST,
  '__module__' : 'reviews_pb2'
  # @@protoc_insertion_point(class_scope:ReviewByIdRequest)
  })
_sym_db.RegisterMessage(ReviewByIdRequest)

ReviewsByGameRequest = _reflection.GeneratedProtocolMessageType('ReviewsByGameRequest', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWSBYGAMEREQUEST,
  '__module__' : 'reviews_pb2'
  # @@protoc_insertion_point(class_scope:ReviewsByGameRequest)
  })
_sym_db.RegisterMessage(ReviewsByGameRequest)

UpdateReviewByIdRequest = _reflection.GeneratedProtocolMessageType('UpdateReviewByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREVIEWBYIDREQUEST,
  '__module__' : 'reviews_pb2'
  # @@protoc_insertion_point(class_scope:UpdateReviewByIdRequest)
  })
_sym_db.RegisterMessage(UpdateReviewByIdRequest)

UpdateHelpfulOnReviewByIdRequest = _reflection.GeneratedProtocolMessageType('UpdateHelpfulOnReviewByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEHELPFULONREVIEWBYIDREQUEST,
  '__module__' : 'reviews_pb2'
  # @@protoc_insertion_point(class_scope:UpdateHelpfulOnReviewByIdRequest)
  })
_sym_db.RegisterMessage(UpdateHelpfulOnReviewByIdRequest)

ReviewsByLanguageRequest = _reflection.GeneratedProtocolMessageType('ReviewsByLanguageRequest', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWSBYLANGUAGEREQUEST,
  '__module__' : 'reviews_pb2'
  # @@protoc_insertion_point(class_scope:ReviewsByLanguageRequest)
  })
_sym_db.RegisterMessage(ReviewsByLanguageRequest)

ReviewsByUserIdRequest = _reflection.GeneratedProtocolMessageType('ReviewsByUserIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWSBYUSERIDREQUEST,
  '__module__' : 'reviews_pb2'
  # @@protoc_insertion_point(class_scope:ReviewsByUserIdRequest)
  })
_sym_db.RegisterMessage(ReviewsByUserIdRequest)

ReviewsByHelpfulRequest = _reflection.GeneratedProtocolMessageType('ReviewsByHelpfulRequest', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWSBYHELPFULREQUEST,
  '__module__' : 'reviews_pb2'
  # @@protoc_insertion_point(class_scope:ReviewsByHelpfulRequest)
  })
_sym_db.RegisterMessage(ReviewsByHelpfulRequest)

ReviewData = _reflection.GeneratedProtocolMessageType('ReviewData', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWDATA,
  '__module__' : 'reviews_pb2'
  # @@protoc_insertion_point(class_scope:ReviewData)
  })
_sym_db.RegisterMessage(ReviewData)

ReviewDataResponse = _reflection.GeneratedProtocolMessageType('ReviewDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWDATARESPONSE,
  '__module__' : 'reviews_pb2'
  # @@protoc_insertion_point(class_scope:ReviewDataResponse)
  })
_sym_db.RegisterMessage(ReviewDataResponse)

DeleteReviewResponse = _reflection.GeneratedProtocolMessageType('DeleteReviewResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREVIEWRESPONSE,
  '__module__' : 'reviews_pb2'
  # @@protoc_insertion_point(class_scope:DeleteReviewResponse)
  })
_sym_db.RegisterMessage(DeleteReviewResponse)

_REVIEWS = DESCRIPTOR.services_by_name['Reviews']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REVIEWBYIDREQUEST._serialized_start=17
  _REVIEWBYIDREQUEST._serialized_end=55
  _REVIEWSBYGAMEREQUEST._serialized_start=57
  _REVIEWSBYGAMEREQUEST._serialized_end=116
  _UPDATEREVIEWBYIDREQUEST._serialized_start=118
  _UPDATEREVIEWBYIDREQUEST._serialized_end=199
  _UPDATEHELPFULONREVIEWBYIDREQUEST._serialized_start=201
  _UPDATEHELPFULONREVIEWBYIDREQUEST._serialized_end=277
  _REVIEWSBYLANGUAGEREQUEST._serialized_start=279
  _REVIEWSBYLANGUAGEREQUEST._serialized_end=344
  _REVIEWSBYUSERIDREQUEST._serialized_start=346
  _REVIEWSBYUSERIDREQUEST._serialized_end=416
  _REVIEWSBYHELPFULREQUEST._serialized_start=418
  _REVIEWSBYHELPFULREQUEST._serialized_end=487
  _REVIEWDATA._serialized_start=490
  _REVIEWDATA._serialized_end=694
  _REVIEWDATARESPONSE._serialized_start=696
  _REVIEWDATARESPONSE._serialized_end=746
  _DELETEREVIEWRESPONSE._serialized_start=748
  _DELETEREVIEWRESPONSE._serialized_end=786
  _REVIEWS._serialized_start=789
  _REVIEWS._serialized_end=1293
# @@protoc_insertion_point(module_scope)
