import os
import re

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from reviews_pb2_grpc import ReviewsStub
from reviews_pb2 import *

reviews_host = os.getenv("REVIEWS_HOST", "localhost")
reviews_channel = grpc.insecure_channel(f"{reviews_host}:50053")
reviews_client = ReviewsStub(reviews_channel)

def getReviewById(id):
    request = ReviewByIdRequest(review_id = id)  
    response = reviews_client.GetReview(request)
    return {"user_id": response.author_steam_id, 
    "app_id": response.app_id, 
    "review": response.review, 
    "recommended": response.recommended, 
    "votes_helpful": response.votes_helpful,
    "language": response.language,
    "timestamp_created": response.timestamp_created,
    "timestamp_updated": response.timestamp_updated}